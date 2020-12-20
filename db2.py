# Module Imports
import mariadb
import sys

'SET GLOBAL connect_timeout=86400';
'SET GLOBAL wait_timeout=86400';
'SET GLOBAL interactive_timeout=86400'; 

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="web27_kayhaseeb",
        password="!kayhaseeb!2020",
        host="python.web27.ws2.speedit.info",
        port=3306,
        database="web27_python"

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
        "create table students(first_name VARCHAR(20), last_name VARCHAR(20)) ")
except mariadb.Error as e:
    print(f"Error: {e}")

conn.commit() 