# import sqlite3

# DB_PATH = "telementary\\data\\pitwall.db"

# connection = sqlite3.connect(DB_PATH)
# cursor = connection.cursor()

# cursor.execute("SELECT * FROM sessions")

# # Get column names
# columns = [description[0] for description in cursor.description]

# print(columns)

# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# connection.close()
import sqlite3

DB_PATH = "telementary\\data\\pitwall.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute("SELECT * FROM telemetry")

columns = [description[0] for description in cursor.description]

for row in cursor.fetchall():
    print("-" * 50)

    for column, value in zip(columns, row):
        print(f"{column}: {value}")

connection.close()