import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "Database1"
)

cur = con.cursor()

if con.is_connected():
    print("Connected")
else:
    print("Not connected")