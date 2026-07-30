import socket
import struct

HOST = "127.0.0.1"
PORT = 20777

HEADER_FORMAT = "<HBBBBBQfIIBB"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
TELEMETRY_FORMAT = "<HfffBbHBBHHHHHBBBBBBBBHffffBBBB"
TELEMETRY_SIZE = struct.calcsize(TELEMETRY_FORMAT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(HEADER_SIZE)
print(TELEMETRY_SIZE)

sock.bind((HOST, PORT))
print("Waiting for packets")


def parse_header(data):
    header = struct.unpack(HEADER_FORMAT, data[:HEADER_SIZE])
    return {
        "packet_format": header[0],
        "game_year": header[1],
        "major_version": header[2],
        "minor_version": header[3],
        "packet_version": header[4],
        "packet_id": header[5],
        "session_uid": header[6],
        "session_time": header[7],
        "frame_identifier": header[8],
        "overall_frame_identifier": header[9],
        "player_car_index": header[10],
        "secondary_player_car_index": header[11]
    }


def parse_car_telemetry(data):
    telemetry = struct.unpack(TELEMETRY_FORMAT, data[HEADER_SIZE:HEADER_SIZE + TELEMETRY_SIZE])
    speed = telemetry[0]
    throttle = telemetry[1]
    steer = telemetry[2]
    brake = telemetry[3]
    gear = telemetry[5]
    rpm = telemetry[6]
    drs = telemetry[7]
    return{
        "speed":speed,
        "throttle":throttle,
        "steer":steer,
        "brake":brake,
        "gear":gear,
        "rpm":rpm,
        "drs":drs
    }
# while (True):
    
#     data, addr = sock.recvfrom(2048)
#     # print(len(data),": pack num",i)
#     # i += 1
#     print(type(data))
#     print(len(data))
#     print(data[:24])
#     break

# for i in range(10):
#     data, addr = sock.recvfrom(2048)
#     print(len(data),": pack num", i)
#     header = struct.unpack(HEADER_FORMAT,data[:29])
    
#     (
#     packet_format,
#     game_year,
#     major_version,
#     minor_version,
#     packet_version,
#     packet_id,
#     session_uid,
#     session_time,
#     frame_identifier,
#     overall_frame_identifier,
#     player_car_index,
#     secondary_player_car_index
#     ) = header
#     print(packet_id)
#     print()
while True:
    data, addr = sock.recvfrom(2048)

    header = parse_header(data)

    if header["packet_id"] == 6:
        telemetry = parse_car_telemetry(data)
        print(telemetry)
    