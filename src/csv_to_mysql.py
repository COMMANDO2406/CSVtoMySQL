import sys

if len(sys.argv) != 5:
    print("Usage: python csv_to_mysql.py <database_name> <table_name> <column_names> <csv_file>")
    sys.exit(1)

database_name = sys.argv[1]
table_name = sys.argv[2]
header = sys.argv[3].split(",")
csv_file = sys.argv[4]


import mysql.connector
import csv
from config import host,user,password

con = mysql.connector.connect(
    host = host,
    user = user,
    password = password
)

cur = con.cursor()

if con.is_connected():
    print("Connected successfully")
else:
    print("Not connected")

# Check if the database exists and create it if it doesn't
cur.execute(f"SHOW DATABASES LIKE '{database_name}'")
result = cur.fetchone()

if not result:
    cur.execute(f"CREATE DATABASE {database_name}")
    print(f"Database '{database_name}' created successfully")
else:
    print(f"Database '{database_name}' already exists")

# Connect to the newly created or existing database
con.database = database_name

with open(csv_file, "r") as file:
    reader = csv.reader(file)
    # this is the reader object from the csv module
    next(reader)

    columns = []
    for column_name in header:
        columns.append(f"{column_name} varchar(255)")
    
    # print(columns)

    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
    # print(create_table_query)

    # this is a create query and it works by using the join funtion on the column names so that they are seperated by commas
    # over here the query is required to be in uppercase as during testing the code would throw an error if it wasn't 

    cur.execute(create_table_query)

    for row in reader:
        insert_query = f"INSERT INTO {table_name} ({', '.join(header)}) values ({', '.join(['%s'] * len(row))})"
        # this is the query creation part of the code, it works by using a formated string to insert the variables
        # the %s is used instead of a variable as it is required for mysql 
        # and it dosent work if the variable is directly put into the formatted str.

        values = tuple(row)

        # print(insert_query,values)
        cur.execute(insert_query, values)
        # the cur.execute function requires the query with the %s and a tuple contaning the varaibles in the above format

con.commit()
con.close()
print("Data imported successfully.")
