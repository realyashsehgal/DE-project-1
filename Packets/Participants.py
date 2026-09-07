class LiveryColor:
    def __init__(self):
        self.red = None
        self.green = None
        self.blue = None

    def parse_liverycolor(self,values,index):
        self.red = values[index]
        self.green = values[index + 1]
        self.blue = values[index + 2]

class ParticipantsData:
    def __init__(self):
        self.m_aicontrolled = None
        self.m_driver_id = None
        self.m_network_id = None
        self.m_team_id = None
        self.m_my_teamid = None
        self.m_race_num = None
        self.m_nationality = None
        self.m_name = None
        self.m_telemetry = None
        self.m_showonlinename = None
        self.m_tech_level = None
        self.m_platform = None
        self.m_numcolors = None
        self.liverycolors = []

    def parse_participantdata(self, values, index):
        self.m_aicontrolled = values[index ]
        self.m_driver_id = values[index + 1]
        self.m_network_id = values[index + 2]
        self.m_team_id = values[index + 3]
        self.m_my_teamid = values[index + 4]
        self.m_race_num = values[index + 5]
        self.m_nationality = values[index + 6]
        self.m_name = values[index + 7]
        self.m_telemetry = values[index + 8]
        self.m_showonlinename = values[index + 9]
        self.m_tech_level = values[index + 10]
        self.m_platform = values[index + 11]
        self.m_numcolors = values[index + 12]