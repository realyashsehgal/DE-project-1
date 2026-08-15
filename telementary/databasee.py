import sqlite3
DB_PATH = "telementary\\data\\pitwall.db"


def get_connection():
    return  sqlite3.connect(DB_PATH)



def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    #Saving session data like 

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions(
            session_id TEXT,  
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
            session_id TEXT,
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
        session_id TEXT,
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

def insert_session(race_state):
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
    str(race_state.session_id), 
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

def insert_lap(race_state):
    connection =  get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO laps(
            session_id,
            last_lap,
            current_lap,
            sector1_time,
            sector2_time,
            sector3_time,
            delta_front,
            lap_distance,
            car_pos,
            current_sector
        )
        VALUES(?,?,?,?,?,?,?,?,?,?)
    """,
    (
        str(race_state.session_id), 
        race_state.last_lap,
        race_state.current_lap,
        race_state.sector1,
        race_state.sector2,
        race_state.sector3,
        race_state.delta_front,
        race_state.lap_distance,
        race_state.car_pos ,
        race_state.curr_sector       
    ))

    connection.commit()
    connection.close()

def insert_telemetry(race_state):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO telemetry(
        session_id,
        speed,
        throttle,
        steer,
        brake,
        gear,
        rpm,
        drs,
        RL_brake_temp,
        RR_brake_temp,
        FL_brake_temp,
        FR_brake_temp,
        RL_tyre_surface_temp,
        RR_tyre_surface_temp,
        FL_tyre_surface_temp,
        FR_tyre_surface_temp,
        RL_tyre_inner_temp,
        RR_tyre_inner_temp,
        FL_tyre_inner_temp,
        FR_tyre_inner_temp,
        engine_temp,
        RL_tyre_pressure,
        RR_tyre_pressure,
        FL_tyre_pressure,
        FR_tyre_pressure,
        RL_surface_type,
        RR_surface_type,
        FL_surface_type,
        FR_surface_type
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """,
    (
    str(race_state.session_id),
    race_state.speed,
    race_state.throttle,
    race_state.steer,
    race_state.brake,
    race_state.gear,
    race_state.rpm,
    race_state.drs,

    race_state.brake_temp["RL"],
    race_state.brake_temp["RR"],
    race_state.brake_temp["FL"],
    race_state.brake_temp["FR"],

    race_state.tyre_surf_temp["RL"],
    race_state.tyre_surf_temp["RR"],
    race_state.tyre_surf_temp["FL"],
    race_state.tyre_surf_temp["FR"],

    race_state.tyre_inner_temp["RL"],
    race_state.tyre_inner_temp["RR"],
    race_state.tyre_inner_temp["FL"],
    race_state.tyre_inner_temp["FR"],

    race_state.engine_temp,

    race_state.tyre_pressure["RL"],
    race_state.tyre_pressure["RR"],
    race_state.tyre_pressure["FL"],
    race_state.tyre_pressure["FR"],

    race_state.surface_type["RL"],
    race_state.surface_type["RR"],
    race_state.surface_type["FL"],
    race_state.surface_type["FR"]
    ))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_database()
    print("db active")