# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="python"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cursor = conn.cursor()

first_name = "shams"
last_name = "sadi"
try:
    cursor.execute(
        "INSERT INTO employees (first_name,last_name) VALUES (?, ?)", 
        (first_name, last_name))
except mariadb.Error as e:
    print(f"Error: {e}")

conn.commit() 