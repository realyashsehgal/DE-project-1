import sqlite3

DB_PATH = "telementary\\data\\pitwall.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

for table in ["sessions", "laps", "telemetry"]:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    print(table, cursor.fetchone()[0])

connection.close()