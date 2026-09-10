class FinalClassificationData:
    def __init__(self):
        self.position = None
        self.num_laps = None
        self.grid_position = None
        self.points = None
        self.num_pit_stops = None
        self.result_status = None
        self.result_reason = None
        self.best_lap_time_ms = None
        self.total_race_time = None
        self.penalties_time = None
        self.num_penalties = None
        self.num_tyre_stints = None

        # Maximum 8 tyre stints
        self.tyre_stints_actual = []
        self.tyre_stints_visual = []
        self.tyre_stints_end_laps = []

    def parse_final_classification(self, values, index):
        self.position = values[index]
        self.num_laps = values[index + 1]
        self.grid_position = values[index + 2]
        self.points = values[index + 3]
        self.num_pit_stops = values[index + 4]
        self.result_status = values[index + 5]
        self.result_reason = values[index + 6]
        self.best_lap_time_ms = values[index + 7]
        self.total_race_time = values[index + 8]
        self.penalties_time = values[index + 9]
        self.num_penalties = values[index + 10]
        self.num_tyre_stints = values[index + 11]

        index += 12

        # Actual tyres used
        for i in range(8):
            self.tyre_stints_actual.append(values[index])
            index += 1

        # Visual tyres used
        for i in range(8):
            self.tyre_stints_visual.append(values[index])
            index += 1

        # Lap each tyre stint ended
        for i in range(8):
            self.tyre_stints_end_laps.append(values[index])
            index += 1