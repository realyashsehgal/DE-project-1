import sqlite3
from udp_reader import race_state
DB_PATH = "telementary\\data\\pitwall.db"


def get_connection():
    return  sqlite3.connect(DB_PATH)



def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    #Saving session data like 

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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS laps(
            session_id INTEGER,
            last_lap INTEGER,
            current_lap INTEGER,
            sector1_time INTEGER,
            sector2_time INTEGER,
            sector3_time INTEGER,
            delta_front INTEGER,
            lap_distance REAL,
            car_pos INTEGER,
            current_sector INTEGER,

            FOREIGN KEY (session_id) REFERENCES sessions(session_id)
        )
    """)

    #now in the data below we will insert lap time and curr lap number from diffrent packets

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS telemetry(
        session_id INTEGER,
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

def insert_session():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO sessions(
        
            session_id,  
            track_id ,
            session_type ,
            time ,
            weather ,
            track_temp ,
            track_length,
            total_laps 
        )
        VALUES(?,?,?,?,?,?,?,?)
    """,
    (
    race_state.session_id, 
    race_state.track_id ,
    race_state.session_type, 
    race_state.time_left ,
    race_state.weather ,
    race_state.track_temp, 
    race_state.track_length, 
    race_state.total_laps 
    ))


    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_database()
    print("db active")