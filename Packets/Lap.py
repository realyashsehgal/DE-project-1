class Lap:
    def __init__(self):
        self.m_lastlaptime = None
        self.m_currentlaptime = None
        self.m_sector1time = None
        self.m_sector1time_minutespart = None
        self.m_sector2time = None
        self.m_sector2time_minutespart = None
        self.m_deltato_carinfront = None
        self.m_deltato_carinfront_minutes = None
        self.m_deltato_raceleader = None
        self.m_deltato_raceleader_minutes = None
        self.m_lapdistance = None #Current car