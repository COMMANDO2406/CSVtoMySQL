import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
import csv
from config import host, user, password

def connect_to_database(database_name, table_name, header, csv_file):
    try:
        con = mysql.connector.connect(
            host=host,
            user=user,
            password=password
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

        columns = [f"{col.strip()} varchar(255)" for col in header.split(",")]
        
        # this is a create query and it works by using the join funtion on the column names so that they are seperated by commas
        # over here the query is required to be in uppercase as during testing the code would throw an error if it wasn't 
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        cur.execute(create_table_query)

        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            # this is the reader object from the csv module
            next(reader)

            for row in reader:
                insert_query = f"INSERT INTO {table_name} ({', '.join(header.split(','))}) values ({', '.join(['%s'] * len(row))})"
                # this is the query creation part of the code, it works by using a formated string to insert the variables
                # the %s is used instead of a variable as it is required for mysql 
                # and it dosent work if the variable is directly put into the formatted str.
                values = tuple(row)
                cur.execute(insert_query, values)
                # the cur.execute function requires the query with the %s and a tuple contaning the varaibles in the above format

        con.commit()
        con.close()
        messagebox.showinfo("Success", "Data imported successfully.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    csv_path_entry.delete(0, tk.END)
    csv_path_entry.insert(0, file_path)

app = tk.Tk()
app.title("CSV to MySQL Importer")

tk.Label(app, text="Database Name:").grid(row=0, column=0, padx=10, pady=10)
db_name_entry = tk.Entry(app)
db_name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Table Name:").grid(row=1, column=0, padx=10, pady=10)
table_name_entry = tk.Entry(app)
table_name_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text="Column Names (comma separated):").grid(row=2, column=0, padx=10, pady=10)
column_names_entry = tk.Entry(app)
column_names_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(app, text="CSV File Path:").grid(row=3, column=0, padx=10, pady=10)
csv_path_entry = tk.Entry(app)
csv_path_entry.grid(row=3, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=browse_file).grid(row=3, column=2, padx=10, pady=10)

def on_import():
    database_name = db_name_entry.get()
    table_name = table_name_entry.get()
    column_names = column_names_entry.get()
    csv_file_path = csv_path_entry.get()

    if not database_name or not table_name or not column_names or not csv_file_path:
        messagebox.showerror("Error", "All fields are required")
        return

    connect_to_database(database_name, table_name, column_names, csv_file_path)

tk.Button(app, text="Import", command=on_import).grid(row=4, column=0, columnspan=3, padx=10, pady=10)

app.mainloop()
