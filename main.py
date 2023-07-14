import mysql.connector
import csv

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

table_name = "NewTable"

header = input("Enter column names (comma-separated): ").split(",")

csv_file = "blank.csv"
with open(csv_file, "r") as file:
    reader = csv.reader(file)

    next(reader)

    column_defs = []
    for column_name in header:
        column_defs.append(f"{column_name} VARCHAR(255)")

    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_defs)})"
    cur.execute(create_table_query)

    for row in reader:
        insert_query = f"INSERT INTO {table_name} ({', '.join(header)}) VALUES ({', '.join(['%s'] * len(row))})"
        values = tuple(row)

        cur.execute(insert_query, values)

con.commit()
con.close()
print("Data imported successfully.")