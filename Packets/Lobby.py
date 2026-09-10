class LobbyInfoData:
    def __init__(self):
        self.ai_controlled = None
        self.team_id = None
        self.nationality = None
        self.platform = None
        self.name = None
        self.car_number = None
        self.your_telemetry = None
        self.show_online_names = None
        self.tech_level = None
        self.ready_status = None

    def parse_lobby_player(self, values, index):
        self.ai_controlled = values[index]
        self.team_id = values[index + 1]
        self.nationality = values[index + 2]
        self.platform = values[index + 3]
        self.name = values[index + 4].decode("utf-8").rstrip("\x00")
        self.car_number = values[index + 5]
        self.your_telemetry = values[index + 6]
        self.show_online_names = values[index + 7]
        self.tech_level = values[index + 8]
        self.ready_status = values[index + 9]