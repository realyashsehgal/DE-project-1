import struct
import socket
import time
import os


HOST = "127.0.0.1"
PORT = 20777


#Packets size/formats written
HEADER_FORMAT = "<HBBBBBQfIIBB"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
TELEMETRY_FORMAT = "<HfffBbHBBHHHHHBBBBBBBBHffffBBBB"
TELEMETRY_SIZE = struct.calcsize(TELEMETRY_FORMAT)
LAPDATA_FORMAT = "<IIHBHBHBHBfffBBBBBBBBBBBBBBBHHBfB"
LAPDATA_SIZE = struct.calcsize(LAPDATA_FORMAT)
SESSION_FORMAT = SESSION_FORMAT = "<HBBBBBQfIIBBBbbBHBbBHHBBBBBBfbfbfbfbfbfbfbfbfbfbfbfbfbfbfbfbfbfbfbfbfbBBBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBIIIBBBBBBBBBBBBBBIBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBff"
SESSION_SIZE = struct.calcsize(SESSION_FORMAT)

#Race state class to store the data from the race
class RaceState:
    def __init__(self):
        #Session data
        self.session_id = 0
        self.session_type = 0
        self.weather = 0
        self.track_temp = 0
        self.total_laps = 0
        self.track_length = 0
        self.track_id = 0
        self.time_left = 0

        #Lap data
        self.last_lap = 0
        self.current_lap = 0
        self.sector1 = 0
        self.sector2 = 0
        self.sector3 = 0
        self.delta_front = 0
        self.lap_distance = 0
        self.car_pos = 0
        self.curr_sector = 0

        #Telemetry data
        self.speed = 0
        self.throttle = 0
        self.steer = 0
        self.brake = 0
        self.gear = 0
        self.rpm = 0
        self.drs = 0
        self.brake_temp = {
            "RL" : 0,
            "RR" : 0,
            "FL" : 0,
            "FR" : 0
        }
        self.tyre_surf_temp = {
            "RL" : 0,
            "RR" : 0,
            "FL" : 0,
            "FR" : 0
        }
        self.tyre_inner_temp= {
            "RL" : 0,
            "RR" : 0,
            "FL" : 0,
            "FR" : 0
        }
        self.engine_temp = 0
        self.tyre_pressure = {
            "RL" : 0,
            "RR" : 0,
            "FL" : 0,
            "FR" : 0
        }
        self.surface_type = {
            "RL" : 0,
            "RR" : 0,
            "FL" : 0,
            "FR" : 0
        }

    def update_session(self,session,header):
        self.session_id = header['session_uid']
        self.session_type = session["session_type"]
        self.weather = session["weather"]
        self.track_temp = session["track_temprature"]
        self.total_laps = session["total_laps"]
        self.track_length = session["track_length"]
        self.track_id = session["track_id"]
        self.time_left = session["time_left"]

       
    def update_telemetry(self,telemetry,header):
        self.speed = telemetry["speed"]
        self.throttle = telemetry["throttle"]
        self.steer = telemetry["steer"]
        self.brake = telemetry["brake"]
        self.gear = telemetry["gear"]
        self.rpm = telemetry["rpm"]
        self.drs = telemetry["drs"]
        self.brake_temp = telemetry["brake_temp"]
        self.tyre_surf_temp = telemetry["tyre_surf_temp"]
        self.tyre_inner_temp= telemetry["tyre_inner_temp"]
        self.engine_temp = telemetry["engine_temp"]
        self.tyre_pressure = telemetry["tyre_pressure"]
        self.surface_type = telemetry["surface_type"]    


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

#Parser for session


def parse_session(data):
    session = struct.unpack(SESSION_FORMAT, data[:SESSION_SIZE])
    return{
        "session_type" :session[2],
        "weather" :session[4],
        "track_temprature": session[5],
        "total_laps": session[14],
        "track_length": session[15],
        "track_id": session[17],
        "time_left": session[19]
    }
    

#Parser for car telemetry
def parse_car_telemetry(data):
    telemetry = struct.unpack(TELEMETRY_FORMAT, data[HEADER_SIZE:HEADER_SIZE + TELEMETRY_SIZE])
    speed = telemetry[0]
    throttle = telemetry[1]
    steer = telemetry[2]
    brake = telemetry[3]
    gear = telemetry[5]
    rpm = telemetry[6]
    drs = telemetry[7]
    brake_temp ={
        "RL": telemetry[10],
        "RR": telemetry[11],
        "FL": telemetry[12],
        "FR": telemetry[13]
    }
    tyre_surf_temp = {
        "RL": telemetry[14],
        "RR": telemetry[15],
        "FL": telemetry[16],
        "FR": telemetry[17]
    }
    tyre_inner_temp = {
        "RL": telemetry[18],
        "RR": telemetry[19],
        "FL": telemetry[20],
        "FR": telemetry[21]
    }
    engine_temp = telemetry[22]
    tyre_pressure = {
        "RL": telemetry[23],
        "RR": telemetry[24],
        "FL": telemetry[25],
        "FR": telemetry[26]
    }
    surface_type = {
        "RL": telemetry[27],
        "RR": telemetry[28],
        "FL": telemetry[29],
        "FR": telemetry[30]
    }
    return{
        "speed":speed,
        "throttle":throttle,
        "steer":steer,
        "brake":brake,
        "gear":gear,
        "rpm":rpm,
        "drs":drs,
        "brake_temp" : brake_temp,
        "tyre_surf_temp" : tyre_surf_temp,
        "tyre_inner_temp" : tyre_inner_temp,
        "engine_temp" : engine_temp,
        "tyre_pressure" : tyre_pressure,
        "surface_type" : surface_type
    } 

#Parsing lap DATA
def parse_lap_data(data):
    lapdata = struct.unpack(LAPDATA_FORMAT, data[HEADER_SIZE:HEADER_SIZE + LAPDATA_SIZE])
    last_lap_time = lapdata[0]
    current_lap_time = lapdata[1]
    sector1_time = lapdata[2]
    sector2_time = lapdata[4]
    delta_to_car_infront = lapdata[6]
    lap_distance = lapdata[9]
    car_position = lapdata[12]
    current_sector = lapdata[16]

    return{
        "Last Lap Time": last_lap_time,
        "Current Lap Time": current_lap_time,
        "Sector 1 Time": sector1_time,
        "Sector 2 Time": sector2_time,
        "Sector 3 Time": current_lap_time - sector1_time - sector2_time,
        "Delta to Car in Front": delta_to_car_infront,
        "lap distance": lap_distance,
        "car position": car_position,
        "current sector": current_sector
    }

#Creating socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST,PORT))


while True:
    data, addr = sock.recvfrom(2048)

    header = parse_header(data)

    if header['packet_id'] == 1:
        # session = parse
        pass