# CSV to MySQL Data Importer
This Python script enables you to import data from a CSV file into a MySQL database. It provides a straightforward interface to input the database name, table name, and column names for the table. The script creates the table dynamically based on the provided column names and their data types. It then reads the CSV file, skipping the header row, and inserts the data into the MySQL table.

## Prerequisites
Python 3.x
MySQL Server

## Installation
Clone this repository or download the script file directly.

Install the required dependencies using pip:

```python
pip install mysql-connector-python
```

## Usage
Make sure you have a MySQL server installed and running.

Open the script file (csv_to_mysql.py) in a text editor.

Provide the MySQL server connection details in the script:

host: The hostname or IP address of the MySQL server.
user: The username for the MySQL server.
password: The password for the MySQL server.
database_name: The name of the database to use.

## Run the script:

``` python
python csv_to_mysql.py
```

Follow the prompts to input the table name and column names. Separate the column names with commas.

The script will read the CSV file (main.csv by default), skipping the header row, and import the data into the MySQL table.

After the script finishes executing, check your MySQL database to verify that the data has been successfully imported.

## Notes:
The CSV file should be located in the same directory as the script file.

The script assumes that the CSV file does not have any quotes around the values.

The script creates the table with each column having a VARCHAR data type and a length of 255 characters. You can modify this.

Feel free to customize the description and README to provide additional information or instructions based on your project's needs.
