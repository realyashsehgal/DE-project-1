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


    connection.commit()
    connection.close()



if __name__ == "__main__":
    initialize_database()
    print("db active")