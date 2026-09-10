class Lap:
    def __init__(self):
        self.last_lap_time_ms = None
        self.current_lap_time_ms = None

        self.sector1_time_ms_part = None
        self.sector1_time_minutes_part = None
        self.sector2_time_ms_part = None
        self.sector2_time_minutes_part = None

        self.delta_to_car_in_front_ms_part = None
        self.delta_to_car_in_front_minutes_part = None
        self.delta_to_race_leader_ms_part = None
        self.delta_to_race_leader_minutes_part = None

        self.lap_distance = None
        self.total_distance = None
        self.safety_car_delta = None

        self.car_position = None
        self.current_lap_num = None
        self.pit_status = None
        self.num_pit_stops = None
        self.sector = None
        self.current_lap_invalid = None

        self.penalties = None
        self.total_warnings = None
        self.corner_cutting_warnings = None
        self.num_unserved_drive_through_pens = None
        self.num_unserved_stop_go_pens = None

        self.grid_position = None
        self.driver_status = None
        self.result_status = None

        self.pit_lane_timer_active = None
        self.pit_lane_time_in_lane_ms = None
        self.pit_stop_timer_ms = None
        self.pit_stop_should_serve_pen = None

        self.speed_trap_fastest_speed = None
        self.speed_trap_fastest_lap = None

    def parse_lap_data(self, values, index):
        self.last_lap_time_ms = values[index]
        self.current_lap_time_ms = values[index + 1]

        self.sector1_time_ms_part = values[index + 2]
        self.sector1_time_minutes_part = values[index + 3]

        self.sector2_time_ms_part = values[index + 4]
        self.sector2_time_minutes_part = values[index + 5]

        self.delta_to_car_in_front_ms_part = values[index + 6]
        self.delta_to_car_in_front_minutes_part = values[index + 7]

        self.delta_to_race_leader_ms_part = values[index + 8]
        self.delta_to_race_leader_minutes_part = values[index + 9]

        self.lap_distance = values[index + 10]
        self.total_distance = values[index + 11]
        self.safety_car_delta = values[index + 12]

        self.car_position = values[index + 13]
        self.current_lap_num = values[index + 14]
        self.pit_status = values[index + 15]
        self.num_pit_stops = values[index + 16]
        self.sector = values[index + 17]
        self.current_lap_invalid = values[index + 18]

        self.penalties = values[index + 19]
        self.total_warnings = values[index + 20]
        self.corner_cutting_warnings = values[index + 21]
        self.num_unserved_drive_through_pens = values[index + 22]
        self.num_unserved_stop_go_pens = values[index + 23]

        self.grid_position = values[index + 24]
        self.driver_status = values[index + 25]
        self.result_status = values[index + 26]

        self.pit_lane_timer_active = values[index + 27]
        self.pit_lane_time_in_lane_ms = values[index + 28]
        self.pit_stop_timer_ms = values[index + 29]
        self.pit_stop_should_serve_pen = values[index + 30]

        self.speed_trap_fastest_speed = values[index + 31]
        self.speed_trap_fastest_lap = values[index + 32]