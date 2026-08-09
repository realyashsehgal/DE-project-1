import sqlite3

DB_PATH = "telementary\\data\\pitwall.db"


def get_connection():
    return  sqlite3.connect(DB_PATH)



def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions(
        )


    """)


    connection.commit()
    connection.close()



if __name__ == "__main__":
    initialize_database()
    print("db active")