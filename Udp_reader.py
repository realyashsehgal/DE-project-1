import socket
import struct

from Packets.Final import FinalClassificationData
from Packets.Header import Header
from Packets.Lap import Lap
from Packets.Lobby import LobbyInfoData
from Packets.Participants import ParticipantsData
from Packets.Session import MarshalZone, Sessions, WeatherForecastSample
from Packets.Telemetry import CarTelemetryData


HOST = "127.0.0.1"
PORT = 20777
MAX_CARS = 22

HEADER_FORMAT = "<HBBBBBQfIIBB"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)

SESSION_FORMAT = (
    "<BbbBHBbBHHBBBBBB"
    + "fB" * 21
    + "BBB"
    + "BBBbbbbB" * 64
    + "BBIII"
    + "B" * 14
    + "I"
    + "B" * 33
    + "B" * 12
    + "ff"
)
LAP_FORMAT = "<IIHBHBHBHBfff" + "B" * 15 + "HHBfB"
TELEMETRY_FORMAT = "<HfffBbHBBHHHHHBBBBBBBBHffffBBBB"
PARTICIPANT_FORMAT = "<7B48s5B12B"
FINAL_CLASSIFICATION_FORMAT = "<3Bf3BIf3B24B"
LOBBY_PLAYER_FORMAT = "<4B48s5B"

SESSION_SIZE = struct.calcsize(SESSION_FORMAT)
LAP_SIZE = struct.calcsize(LAP_FORMAT)
TELEMETRY_SIZE = struct.calcsize(TELEMETRY_FORMAT)
PARTICIPANT_SIZE = struct.calcsize(PARTICIPANT_FORMAT)
FINAL_CLASSIFICATION_SIZE = struct.calcsize(FINAL_CLASSIFICATION_FORMAT)
LOBBY_PLAYER_SIZE = struct.calcsize(LOBBY_PLAYER_FORMAT)


def _payload(data):
    if len(data) < HEADER_SIZE:
        raise ValueError(
            f"Packet is too short for the header: {len(data)} bytes"
        )
    return data[HEADER_SIZE:]


def _records(payload, record_format, record_size, count, packet_name):
    required_size = record_size * count
    if len(payload) < required_size:
        raise ValueError(
            f"{packet_name} payload is too short: expected at least "
            f"{required_size} bytes, received {len(payload)}"
        )
    return [
        struct.unpack_from(record_format, payload, index * record_size)
        for index in range(count)
    ]


def parse_session_packet(payload):
    if len(payload) < SESSION_SIZE:
        raise ValueError(
            f"Session payload is too short: expected {SESSION_SIZE} bytes, "
            f"received {len(payload)}"
        )

    values = struct.unpack_from(SESSION_FORMAT, payload)
    session = Sessions()
    session.parse_session(values)

    session.marshal_Zones = []
    for index in range(16, 58, 2):
        zone = MarshalZone()
        zone.parse_marshal_zones(values, index)
        session.marshal_Zones.append(zone)

    session.weatherforecast_samples = []
    for index in range(61, 573, 8):
        forecast = WeatherForecastSample()
        forecast.parse_weather_forcast(values, index)
        session.weatherforecast_samples.append(forecast)

    return session


def parse_lap_packet(payload):
    records = _records(
        payload, LAP_FORMAT, LAP_SIZE, MAX_CARS, "Lap data"
    )
    laps = []
    for values in records:
        lap = Lap()
        lap.parse_lap_data(values, 0)
        laps.append(lap)
    return laps


def parse_participants_packet(payload):
    if not payload:
        raise ValueError("Participants payload does not contain the car count")

    count = payload[0]
    if count > MAX_CARS:
        raise ValueError(f"Invalid participant count: {count}")

    records = _records(
        payload[1:],
        PARTICIPANT_FORMAT,
        PARTICIPANT_SIZE,
        count,
        "Participants",
    )
    participants = []
    for values in records:
        participant = ParticipantsData()
        participant.parse_participantdata(values, 0)
        participants.append(participant)
    return participants


def parse_telemetry_packet(payload):
    records = _records(
        payload, TELEMETRY_FORMAT, TELEMETRY_SIZE, MAX_CARS, "Telemetry"
    )
    telemetry = []
    for values in records:
        car = CarTelemetryData()
        car.parse_car_telemetry(values, 0)
        telemetry.append(car)
    return telemetry


def parse_final_classification_packet(payload):
    if not payload:
        raise ValueError("Final classification payload is empty")

    count = payload[0]
    if count > MAX_CARS:
        raise ValueError(f"Invalid classification count: {count}")

    records = _records(
        payload[1:],
        FINAL_CLASSIFICATION_FORMAT,
        FINAL_CLASSIFICATION_SIZE,
        count,
        "Final classification",
    )
    classifications = []
    for values in records:
        classification = FinalClassificationData()
        classification.parse_final_classification(values, 0)
        classifications.append(classification)
    return classifications


def parse_lobby_packet(payload):
    if not payload:
        raise ValueError("Lobby payload does not contain the car count")

    count = payload[0]
    if count > MAX_CARS:
        raise ValueError(f"Invalid lobby player count: {count}")

    records = _records(
        payload[1:],
        LOBBY_PLAYER_FORMAT,
        LOBBY_PLAYER_SIZE,
        count,
        "Lobby",
    )
    players = []
    for values in records:
        player = LobbyInfoData()
        player.parse_lobby_player(values, 0)
        players.append(player)
    return players


def decode_packet(data):
    if len(data) < HEADER_SIZE:
        raise ValueError(
            f"Packet is too short for the header: {len(data)} bytes"
        )

    header_values = struct.unpack_from(HEADER_FORMAT, data)
    header = Header()
    header.parse_head(header_values)
    payload = _payload(data)

    if header.packet_id == 1:
        packet = parse_session_packet(payload)
    elif header.packet_id == 2:
        packet = parse_lap_packet(payload)
    elif header.packet_id == 4:
        packet = parse_participants_packet(payload)
    elif header.packet_id == 6:
        packet = parse_telemetry_packet(payload)
    elif header.packet_id == 8:
        packet = parse_final_classification_packet(payload)
    elif header.packet_id == 9:
        packet = parse_lobby_packet(payload)
    else:
        packet = None
    return header, packet


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((HOST, PORT))
        while True:
            data, _ = sock.recvfrom(4096)
            try:
                header, packet = decode_packet(data)
            except (struct.error, ValueError) as error:
                print(f"Invalid packet: {error}")
                continue

            print("Packet ID:", header.packet_id)
            if header.packet_id == 1:
                print("Session packet")
            elif header.packet_id == 2:
                print(f"Lap Data packet ({len(packet)} cars)")
            elif header.packet_id == 4:
                print(f"Participants packet ({len(packet)} cars)")
            elif header.packet_id == 6:
                print(f"Car Telemetry packet ({len(packet)} cars)")
            elif header.packet_id == 8:
                print(f"Final Classification packet ({len(packet)} cars)")
            elif header.packet_id == 9:
                print(f"Lobby Info packet ({len(packet)} players)")
            else:
                print("Unsupported packet")


if __name__ == "__main__":
    main()
