import sqlite3

DB_PATH = "telementary\\data\\pitwall.db"


def get_connection():
    return  sqlite3.connect(DB_PATH)



def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    #Saving session data like 
    #Session id  =====>>>>> this is in the header of the packet
    #rest of the data is available in session packet
    #Track id
    #Session type
    #data/time
    #weather
    #Track info
    #laps
    #duration
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions(
            session_id INTEGER PRIMARY KEY,  
            track_id INTEGER,
            session_type INTEGER,
            time INTEGER,
            weather INTEGER,
            track_temp INTEGER,
            track_length INTEGER,
            total_laps INTEGER
        )
    """)

    #Lap data creation
    #Session id foreign key 
    #current lap num
    #last lap time
    #sector 1 lap time
    #sector 2 lap time
    #sector 3 lap time
    #delta front
    #lap distance
    #Car position
    #Current sector
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS laps(
            session_id INTEGER,
            current_lap INTEGER,
            last_lap INTEGER,
            sector1_time INTEGER,
            sector2_time INTEGER,
            sector3_time INTEGER,
            delta_front INTEGER,
            lap_distance REAL,
            car_pos INTEGER,
            current_sector INTEGER,

            FOREIGN KEY (session_id) REFERENCES session(session_id)
        )
    """)

    #Telemetry data creation
    #session id
    #speed
    #throttle
    #steer
    #brake
    #gear
    #rpm
    #drs
    #brake temp (FL,FR,RL,RR)
    #tyre surface temp (FL,FR,RL,RR)
    #tyre inner temp (FL,FR,RL,RR)
    #engine temp
    #tyre press (FL,FR,RL,RR)
    #surface type


    #now in the data below we will insert lap time and curr lap number from diffrent packets

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS telemetry(
        session_id INTEGER,
        curr_lap INTEGER,
        lap_time INTEGER,
        speed INTEGER,
        throttle REAL,
        steer REAL,
        brake REAL,
        gear INTEGER,
        rpm INTEGER,
        drs INTEGER,
        RL_brake_temp INTEGER,
        RR_brake_temp INTEGER,
        FL_brake_temp INTEGER,
        FR_brake_temp INTEGER,
        RL_tyre_surface_temp INTEGER,
        RR_tyre_surface_temp INTEGER,
        FL_tyre_surface_temp INTEGER,
        FR_tyre_surface_temp INTEGER,
        RL_tyre_inner_temp INTEGER,
        RR_tyre_inner_temp INTEGER,
        FL_tyre_inner_temp INTEGER,
        FR_tyre_inner_temp INTEGER,
        engine_temp INTEGER,
        RL_tyre_pressure REAL,
        RR_tyre_pressure REAL,
        FL_tyre_pressure REAL,
        FR_tyre_pressure REAL,
        RL_surface_type INTEGER,
        RR_surface_type INTEGER,
        FL_surface_type INTEGER,
        FR_surface_type INTEGER
        )
    """)
    connection.commit()
    connection.close()



if __name__ == "__main__":
    initialize_database()
    print("db active")