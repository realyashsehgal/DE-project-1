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



#Race state class to store the data from the race
class RaceState:
    def __init__(self):
        #Session data
        self.session_id = 0
        self.track_id = 0
        self.session_type = 0
        self.time = 0
        self.weather = 0
        self.track_temp = 0
        self.track_length = 0
        self.total_laps = 0

        #Lap data
        self.current_lap = 0
        self.last_lap = 0
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

