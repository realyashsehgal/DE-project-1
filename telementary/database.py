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
            current_sector INTEGER

            FOREIGN KEY (session_id) REFERENCES session(session_id)
        )
    """)

    connection.commit()
    connection.close()



if __name__ == "__main__":
    initialize_database()
    print("db active")