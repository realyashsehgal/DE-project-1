import socket
import struct
import os
import time
from rich.live import Live
from rich.table import Table
import time
import threading

HOST = "127.0.0.1"
PORT = 20777

HEADER_FORMAT = "<HBBBBBQfIIBB"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
TELEMETRY_FORMAT = "<HfffBbHBBHHHHHBBBBBBBBHffffBBBB"
TELEMETRY_SIZE = struct.calcsize(TELEMETRY_FORMAT)


#Race state class to hold the telemetry data
class RaceState:
    def __init__(self):
        self.speed = 0
        self.throttle = 0.0
        self.steer = 0.0
        self.brake = 0.0
        self.gear = 0
        self.rpm = 0
        self.drs = 0
        
    #Function to update the telemetry data
    def update(self,telemetry):
        self.speed = telemetry["speed"]
        self.throttle = telemetry["throttle"]
        self.steer = telemetry["steer"]
        self.brake = telemetry["brake"]
        self.gear = telemetry["gear"]
        self.rpm = telemetry["rpm"]
        self.drs = telemetry["drs"]
        
#Function to print the telemetry data
from rich.table import Table

def create_dashboard(race_state):
    table = Table(title="My feed design (MFD)")

    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Speed", f"{race_state.speed} km/h")
    table.add_row("Gear", str(race_state.gear))
    table.add_row("RPM", str(race_state.rpm))
    table.add_row("Throttle", f"{race_state.throttle*100:.0f}%")
    table.add_row("Brake", f"{race_state.brake*100:.0f}%")
    table.add_row("Steering", f"{race_state.steer:.2f}")
    table.add_row("DRS", "ON" if race_state.drs else "OFF")

    return table
def dashboard():
    with Live(create_dashboard(race_state),
              refresh_per_second=30,
              screen=True) as live:

        while True:
            live.update(create_dashboard(race_state))
            time.sleep(0.01)

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

#Race state object to hold the telemetry data 
race_state = RaceState()
dashboard_thread = threading.Thread(target=dashboard, daemon=True)
dashboard_thread.start()


while True:
    
    data, addr = sock.recvfrom(2048)
    header = parse_header(data)

    if header["packet_id"] == 6:
        telemetry = parse_car_telemetry(data)
        race_state.update(telemetry)
        
    
