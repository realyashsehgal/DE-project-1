class Sessions:
    def __init__(self):
        self.m_curr_weather = None
        self.m_curr_tracktemp = None
        self.m_curr_airtemp = None
        self.m_totallaps = None
        self.m_track_len = None
        self.m_session_type = None
        self.m_track_id = None
        self.m_formula = None

        self.m_session_time_left = None
        self.m_session_duration = None
        self.m_pit_speed_limit = None
        self.m_game_paused = None
        self.m_is_spec = None
        self.m_spec_car_index = None
        self.m_sli_pro_native_supp = None
        self.m_num_mar_zone = None
        self.marshal_Zones = None
        self.safety_car_status = None   
        self.network_game = None
        self.num_weather_forecastsample = None
        self.weatherforecast_samples = None
        self.m_forecast_accuracy = None
        self.m_ai_diff = None
        self.m_seasonlink_id = None
        self.m_weekendlink_id = None
        self.m_sessionlink_id = None
        self.m_pitstopwindow_ideallap = None
        self.m_pitstopwindow_latestlap = None
        self.pitstop_rejoin_pos = None
        self.steer_assist = None
        self.braking_assist = None
        self.gearbox_assist = None
        self.pit_assist = None
        self.pitrelease_assist = None
        self.ers_assist = None
        self.drs_assist = None
        self.dynamic_racingline = None
        self.dynamic_racingline_type = None
        self.game_mode = None
        self.rules_set = None
        self.timeofday = None
        self.session_length = None
        self.m_speedunits_leadplayer = None
        self.m_tempratureunits_leadplayer = None
        self.m_speeduntis_secondaryplayer = None
        self.m_tempratureunits_secondaryplayer = None
        self.m_numsafetycar_periods = None
        self.m_numVirtualsafetycar_periods = None
        self.m_numredflag_periods = None
        self.m_equalcar_performance = None
        self.m_recoverymode = None
        self.m_flashback_limit = None
        self.surface_type = None
        self.m_low_feul_mode = None
        self.m_race_starts = None
        self.m_tyretemp = None
        self.m_pitlane_tyretemp_sim = None
        self.m_carDamage = None
        self.m_cardamage_rate = None
        self.m_collisions = None
        self.collisionoff_forfirstlap = None
        self.mpUnsafe_pitrelease = None
        self.mpoff_forgreifing = None
        self.corner_cutting_stringency = None
        self.parcferme_rules = None
        self.pitstop_experience = None
        self.m_safetycar = None #how much it can come 
        self.m_safetycar_experience = None
        self.m_formation_lap = None
        self.m_formation_lap_experience = None
        self.m_redflag = None
        self.m_affects_Licenselevel = None
        self.m_affects_Licenselevel_MP = None
        self.m_numsessions_Inweekend = None
        self.WeekednStructure = None
        self.sector2Lap_distancestart = None
        self.sector3Lap_distancestart = None
    def parse_session(self, values):
        self.m_curr_weather = values[0]
        self.m_curr_tracktemp = values[1]
        self.m_curr_airtemp = values[2]
        self.m_totallaps = values[3]
        self.m_track_len = values[4]
        self.m_session_type = values[5]
        self.m_track_id = values[6]
        self.m_formula = values[7]

        self.m_session_time_left = values[8]
        self.m_session_duration = values[9]
        self.m_pit_speed_limit = values[10]
        self.m_game_paused = values[11]
        self.m_is_spec = values[12]
        self.m_spec_car_index = values[13]
        self.m_sli_pro_native_supp = values[14]

        # Marshal zones: values 15 → 56
        self.m_num_mar_zone = values[56]

        self.safety_car_status = values[57]
        self.network_game = values[58]
        self.num_weather_forecastsample = values[59]

        # WeatherForecastSamples: values 60 → 571

        self.m_forecast_accuracy = values[572]
        self.m_ai_diff = values[573]
        self.m_seasonlink_id = values[574]
        self.m_weekendlink_id = values[575]
        self.m_sessionlink_id = values[576]

        self.m_pitstopwindow_ideallap = values[577]
        self.m_pitstopwindow_latestlap = values[578]
        self.pitstop_rejoin_pos = values[579]
        self.steer_assist = values[580]
        self.braking_assist = values[581]
        self.gearbox_assist = values[582]
        self.pit_assist = values[583]
        self.pitrelease_assist = values[584]
        self.ers_assist = values[585]
        self.drs_assist = values[586]
        self.dynamic_racingline = values[587]
        self.dynamic_racingline_type = values[588]
        self.game_mode = values[589]
        self.rules_set = values[590]

        self.timeofday = values[591]

        self.session_length = values[592]
        self.m_speedunits_leadplayer = values[593]
        self.m_tempratureunits_leadplayer = values[594]
        self.m_speeduntis_secondaryplayer = values[595]
        self.m_tempratureunits_secondaryplayer = values[596]
        self.m_numsafetycar_periods = values[597]
        self.m_numVirtualsafetycar_periods = values[598]
        self.m_numredflag_periods = values[599]
        self.m_equalcar_performance = values[600]
        self.m_recoverymode = values[601]
        self.m_flashback_limit = values[602]
        self.surface_type = values[603]
        self.m_low_feul_mode = values[604]
        self.m_race_starts = values[605]
        self.m_tyretemp = values[606]
        self.m_pitlane_tyretemp_sim = values[607]
        self.m_carDamage = values[608]
        self.m_cardamage_rate = values[609]
        self.m_collisions = values[610]
        self.collisionoff_forfirstlap = values[611]
        self.mpUnsafe_pitrelease = values[612]
        self.mpoff_forgreifing = values[613]
        self.corner_cutting_stringency = values[614]
        self.parcferme_rules = values[615]
        self.pitstop_experience = values[616]
        self.m_safetycar = values[617]
        self.m_safetycar_experience = values[618]
        self.m_formation_lap = values[619]
        self.m_formation_lap_experience = values[620]
        self.m_redflag = values[621]
        self.m_affects_Licenselevel = values[622]
        self.m_affects_Licenselevel_MP = values[623]

        self.m_numsessions_Inweekend = values[624]

        # WeekendStructure: values 625 → 636
        self.sector2Lap_distancestart = values[637]
        self.sector3Lap_distancestart = values[638]
class MarshalZone(Sessions):
    def __init__(self):
        self.m_zonestart = None
        self.m_zoneflag = None
    def parse_marshal_zones(self, values, index):
        self.m_zonestart = values[index]
        self.m_zoneflag = values[index + 1]


class WeatherForecastSample(Sessions):
    def __init__(self):
        self.session_type = None #unkown
        self.tiemoffset = None #Time in minutes the forecast is for
        self.weather = None # 0 = clear, 1 = light cloud, 2 = overcast, 3 = light rain, 4 = heavy rain, 5 = storm
        self.track_temp = None #in celsius
        self.track_temp_change = None #track temp change 0 = up, 1 = down 2 = no change
        self.air_temp = None #Air temp in celsius
        self.air_temp_change = None #same as track temp
        self.rain_perc =None  #Percentage of rain 0 - 100

    def parse_weather_forcast(self, values, index):
        self.session_type = values[index] #unkown
        self.tiemoffset = values[index + 1] #Time in minutes the forecast is for
        self.weather = values[index + 2] # 0 = clear, 1 = light cloud, 2 = overcast, 3 = light rain, 4 = heavy rain, 5 = storm
        self.track_temp = values[index + 3] #in celsius
        self.track_temp_change = values[index + 4] #track temp change 0 = up, 1 = down 2 = no change
        self.air_temp = values[index + 5] #Air temp in celsius
        self.air_temp_change = values[index + 6] #same as track temp
        self.rain_perc =values[index + 7]  #Percentage of rain 0 - 100

#YASH CREATE DIFFRENT CLASSES FOR EACH STRUCT 


#AND EVERY STRUCT SHALL BE A TABLE WITH FRAME AS COMMON RELATIONSHIP
