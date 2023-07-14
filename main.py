import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user='your_username',
    password='your_password',
    database='your_database'
)

cur = con.cursor()

if con.is_connected():
    print("Connected")
else:
    print("Not connected")