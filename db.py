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
        database="python_db"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cursor = conn.cursor()

first_name = "harry"
last_name = "potter"

try:
    cursor.execute(
        "INSERT INTO employees (first_name,last_name) VALUES (?, ?)", 
        (first_name, last_name))
except mariadb.Error as e:
    print(f"Error: {e}")

conn.commit() 