import sys
import os
import mysql.connector

# Ensure the config.py can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import host, user, password

def test_database_connection():
    con = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    assert con.is_connected(), "Failed to connect to the database"
    con.close()

def test_database_creation():
    database_name = "test_db"
    con = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    cur = con.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")
    cur.execute(f"SHOW DATABASES LIKE '{database_name}'")
    result = cur.fetchone()
    assert result, "Database creation failed"
    cur.execute(f"DROP DATABASE {database_name}")
    con.close()
