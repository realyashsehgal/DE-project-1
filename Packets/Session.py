class Sessions:
    def __init__(self):
        self.m_zonestart = 0 #Marhsal zone start 0 - 1 
        self.m_zoneflag = 0 #Flag zone wise 0 = none 1 = green 2 = blue 3 = yellow

        self.session_type = 0 #unkown
        self.tiemoffset = 0 #Time in minutes the forecast is for
        self.weather = 0 # 0 = clear, 1 = light cloud, 2 = overcast, 3 = light rain, 4 = heavy rain, 5 = storm
        self.track_temp = 0 #in celsius
        self.track_temp_change = 0 #track temp change 0 = up, 1 = down 2 = no change
        self.air_temp = 0 #Air temp in celsius
        self.air_temp_change = 0 #same as track temp
        self.rain_perc = 0 #Percentage of rain 0 - 1


#YASH CREATE DIFFRENT CLASSES FOR EACH STRUCT 


#AND EVERY STRUCT SHALL BE A TABLE WITH FRAME AS COMMON RELATIONSHIP
