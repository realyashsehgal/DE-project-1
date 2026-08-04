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
LAPDATA_FORMAT = "<IIHBHBHBHBfffBBBBBBBBBBBBBBBHHBfB"
LAPDATA_SIZE = struct.calcsize(LAPDATA_FORMAT)

#Race state class to hold the telemetry data
class RaceState:
    def __init__(self):
        #Inputting telemetry data from pack id 6
        self.speed = 0
        self.throttle = 0.0
        self.steer = 0.0
        self.brake = 0.0
        self.gear = 0
        self.rpm = 0
        self.drs = 0
        self.rev_light_perc = 0
        self.brake_temp={
            "FL":0,
            "FR":0,
            "RL":0,
            "RR":0
        }
        self.tyre_surf_temp={
            "FL":0,
            "FR":0,
            "RL":0,
            "RR":0
        }
        self.tyre_inner_temp={
            "FL":0,
            "FR":0,
            "RL":0,
            "RR":0
        }
        self.engine_temp = 0
        self.tyre_pressure = {
            "FL":0,
            "FR":0,
            "RL":0,
            "RR":0
        }
        self.surface_type = 0
        
        #inputting the data from packet 2 -> Lap data
        self.last_lap_time = 0
        self.current_lap_time = 0
        self.sector1_time = 0
        self.sector2_time = 0
        self.sector3_time = self.current_lap_time - self.sector1_time - self.sector2_time
        self.delta_to_car_infront = 0
        
        
        
    #Function to update the telemetry data
    def update_telemetry(self,telemetry):
        self.speed = telemetry["speed"]
        self.throttle = telemetry["throttle"]
        self.steer = telemetry["steer"]
        self.brake = telemetry["brake"]
        self.gear = telemetry["gear"]
        self.rpm = telemetry["rpm"]
        self.drs = telemetry["drs"]
        self.rev_light_perc = telemetry["rev_light_perc"]
        self.brake_temp = telemetry["brake_temp"]
        self.tyre_surf_temp = telemetry["tyre_surf_temp"]
        self.tyre_inner_temp = telemetry["tyre_inner_temp"]
        self.engine_temp = telemetry["engine_temp"]
        self.tyre_pressure = telemetry["tyre_pressure"]
        self.surface_type = telemetry["surface_type"]
    
    #Updating lap data from packet 2
    def update_lap_data(self,lapdata):
        self.last_lap_time = lapdata["Last Lap Time"]
        self.current_lap_time = lapdata["Current Lap Time"]
        self.sector1_time = lapdata["Sector 1 Time"]
        self.sector2_time = lapdata["Sector 2 Time"]
        self.sector3_time = lapdata["Sector 3 Time"]
        self.delta_to_car_infront = lapdata["Delta to Car in Front"]
#Function to print the telemetry data
from rich.table import Table
#Temporary dashboard feature to identify the telemetry data being received
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
    # table.add_row("Rev Lights", f"{race_state.rev_light_perc}%")
    # table.add_row("Brake Temperature (FL)", f"{race_state.brake_temp['FL']} °C")
    # table.add_row("Brake Temperature (FR)", f"{race_state.brake_temp['FR']} °C")
    # table.add_row("Brake Temperature (RL)", f"{race_state.brake_temp['RL']} °C")
    # table.add_row("Brake Temperature (RR)", f"{race_state.brake_temp['RR']} °C")
    # table.add_row("Tyre Surface Temperature (FL)", f"{race_state.tyre_surf_temp['FL']} °C")
    # table.add_row("Tyre Surface Temperature (FR)", f"{race_state.tyre_surf_temp['FR']} °C")
    # table.add_row("Tyre Surface Temperature (RL)", f"{race_state.tyre_surf_temp['RL']} °C")
    # table.add_row("Tyre Surface Temperature (RR)", f"{race_state.tyre_surf_temp['RR']} °C")
    # table.add_row("Tyre Inner Temperature (FL)", f"{race_state.tyre_inner_temp['FL']} °C")
    # table.add_row("Tyre Inner Temperature (FR)", f"{race_state.tyre_inner_temp['FR']} °C")
    # table.add_row("Tyre Inner Temperature (RL)", f"{race_state.tyre_inner_temp['RL']} °C")
    # table.add_row("Tyre Inner Temperature (RR)", f"{race_state.tyre_inner_temp['RR']} °C")
    # table.add_row("Engine Temperature", f"{race_state.engine_temp} °C")
    # table.add_row("Tyre Pressure (FL)", f"{race_state.tyre_pressure['FL']}")
    # table.add_row("Tyre Pressure (FR)", f"{race_state.tyre_pressure['FR']}")
    # table.add_row("Tyre Pressure (RL)", f"{race_state.tyre_pressure['RL']}")
    # table.add_row("Tyre Pressure (RR)", f"{race_state.tyre_pressure['RR']}")
    table.add_row("Last lap time", f"{race_state.last_lap_time}")
    


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

#Receiving the the packets and parsing the header
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

#Parsing the car telemetry data from th recieved packets
def parse_car_telemetry(data):
    telemetry = struct.unpack(TELEMETRY_FORMAT, data[HEADER_SIZE:HEADER_SIZE + TELEMETRY_SIZE])
    speed = telemetry[0]
    throttle = telemetry[1]
    steer = telemetry[2]
    brake = telemetry[3]
    gear = telemetry[5]
    rpm = telemetry[6]
    drs = telemetry[7]
    rev_light_perc = telemetry[8]
    brake_temp ={
        "FL": telemetry[10],
        "FR": telemetry[11],
        "RL": telemetry[12],
        "RR": telemetry[13]
    }
    tyre_surf_temp = {
        "FL": telemetry[14],
        "FR": telemetry[15],
        "RL": telemetry[16],
        "RR": telemetry[17]
    }
    tyre_inner_temp = {
        "FL": telemetry[18],
        "FR": telemetry[19],
        "RL": telemetry[20],
        "RR": telemetry[21]
    }
    engine_temp = telemetry[22]
    tyre_pressure = {
        "FL": telemetry[23],
        "FR": telemetry[24],
        "RL": telemetry[25],
        "RR": telemetry[26]
    }
    surface_type = telemetry[27]
    return{
        "speed":speed,
        "throttle":throttle,
        "steer":steer,
        "brake":brake,
        "gear":gear,
        "rpm":rpm,
        "drs":drs,
        "rev_light_perc":rev_light_perc,
        "brake_temp" : brake_temp,
        "tyre_surf_temp" : tyre_surf_temp,
        "tyre_inner_temp" : tyre_inner_temp,
        "engine_temp" : engine_temp,
        "tyre_pressure" : tyre_pressure,
        "surface_type" : surface_type
    } 
    
def parse_lap_data(data):
    lapdata = struct.unpack(LAPDATA_FORMAT, data[HEADER_SIZE:HEADER_SIZE + LAPDATA_SIZE])
    last_lap_time = lapdata[0]
    current_lap_time = lapdata[1]
    sector1_time = lapdata[2]
    sector2_time = lapdata[4]
    delta_to_car_infront = lapdata[6]
    return{
        "Last Lap Time": last_lap_time,
        "Current Lap Time": current_lap_time,
        "Sector 1 Time": sector1_time,
        "Sector 2 Time": sector2_time,
        "Sector 3 Time": current_lap_time - sector1_time - sector2_time,
        "Delta to Car in Front": delta_to_car_infront
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
        race_state.update_telemetry(telemetry)
    elif header["packet_id"] == 2:
        lapdata = parse_lap_data(data)
        race_state.update_lap_data(lapdata)
    
