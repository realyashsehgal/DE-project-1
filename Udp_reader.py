import struct
import socket
import time
import os

from Packets.Header import Header
from Packets.Session import Sessions
from Packets.Lap import Lap
from Packets.Participants import ParticipantsData
from Packets.Telemetry import CarTelemetryData
from Packets.Final import FinalClassificationData
from Packets.Lobby import LobbyInfoData


HOST = "127.0.0.1"
PORT = 20777

# Creating socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))


# Header
HEADER_FORMAT = "<HBBBBBQfIIBB"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)


while True:

    # Receive packet
    data, addr = sock.recvfrom(2048)

    # ---------------- HEADER ----------------

    header_values = struct.unpack(
        HEADER_FORMAT,
        data[:HEADER_SIZE]
    )

    header = Header()
    header.parse_head(header_values)

    print("Packet ID:", header.packet_id)

    # ---------------- PACKET ----------------

    if header.packet_id == 1:
        print("Session packet")

        # packet-specific unpacking will go here
        # session = Sessions()
        # values = struct.unpack(SESSION_FORMAT, data[HEADER_SIZE:])
        # session.parse(values)


    elif header.packet_id == 2:
        print("Lap Data packet")

        # lap = LapData()
        # values = struct.unpack(LAP_FORMAT, data[HEADER_SIZE:])
        # lap.parse(values)


    elif header.packet_id == 4:
        print("Participants packet")

        # participants = ParticipantData()
        # values = struct.unpack(PARTICIPANTS_FORMAT, data[HEADER_SIZE:])
        # participants.parse(values)


    elif header.packet_id == 6:
        print("Car Telemetry packet")

        # telemetry = CarTelemetryData()
        # values = struct.unpack(TELEMETRY_FORMAT, data[HEADER_SIZE:])
        # telemetry.parse(values)


    elif header.packet_id == 8:
        print("Final Classification packet")

        # classification = FinalClassificationData()
        # values = struct.unpack(CLASSIFICATION_FORMAT, data[HEADER_SIZE:])
        # classification.parse(values)


    elif header.packet_id == 9:
        print("Lobby Info packet")

        # lobby = LobbyInfoData()
        # values = struct.unpack(LOBBY_FORMAT, data[HEADER_SIZE:])
        # lobby.parse(values)