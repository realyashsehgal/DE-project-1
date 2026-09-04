import sqlite3
import csv

DB_PATH = "telementary\\data\\pitwall.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

tables = ["sessions", "laps", "telemetry"]

for table in tables:
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    columns = [description[0] for description in cursor.description]

    with open(f"{table}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(columns)

        for row in rows:
            formatted_row = [
                f"{value:.3f}" if isinstance(value, float) else value
                for value in row
            ]
            writer.writerow(formatted_row)

connection.close()

print("CSV files created.")