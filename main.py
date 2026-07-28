import socket
import struct

HOST = "127.0.0.1"
PORT = 20777

HEADER_FORMAT = "<HBBBBBQfIIBB"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((HOST, PORT))
print("Waiting for packets")
i = 0
# while (True):
    
#     data, addr = sock.recvfrom(2048)
#     # print(len(data),": pack num",i)
#     # i += 1
#     print(type(data))
#     print(len(data))
#     print(data[:24])
#     break

for i in range(10):
    data, addr = sock.recvfrom(2048)
    print(len(data),": pack num", i)
    header = struct.unpack(HEADER_FORMAT,data[:29])
    
    (
    packet_format,
    game_year,
    major_version,
    minor_version,
    packet_version,
    packet_id,
    session_uid,
    session_time,
    frame_identifier,
    overall_frame_identifier,
    player_car_index,
    secondary_player_car_index
    ) = header
    print(packet_id)
    print()