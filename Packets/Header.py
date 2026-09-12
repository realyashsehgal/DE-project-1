class Header:
    def __init__(self):
        self.pack_format = None
        self.game_year = None
        self.major_version = None
        self.minor_version = None
        self.packet_version = None
        self.packet_id = None
        self.session_uid = None
        self.session_time = None
        self.frame_id = None
        self.overallframe_id = None
        self.player_carid = None
        self.second_carid = None

    def parse(self, values):
        self.pack_format = values[0]
        self.game_year = values[1]
        self.major_version = values[2]
        self.minor_version = values[3]
        self.packet_version = values[4]
        self.packet_id = values[5]
        self.session_uid = values[6]
        self.session_time = values[7]
        self.frame_id = values[8]
        self.overallframe_id = values[9]
        self.player_carid = values[10]
        self.second_carid = values[11]