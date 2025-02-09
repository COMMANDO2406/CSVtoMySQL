# CSV to MySQL

[![Build Status](https://img.shields.io/github/actions/workflow/status/COMMANDO2406/CSVtoMySQL/test.yml?branch=main)](https://github.com/COMMANDO2406/CSVtoMySQL/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

# Demo
![image](https://github.com/user-attachments/assets/e012b8b9-b0fb-4d0c-a07c-b0c9cf3f0bc8)



# Outdated docs
CSV to MySQL is a simple Python utility that allows you to import data from a CSV file into a MySQL database. This tool checks if the specified database exists and creates it if it doesn't, then creates a table and imports the data from the CSV file.
- https://commando2406.github.io/CSVtoMySQL/
## Features

- Connect to MySQL database
- Check and create database if it doesn't exist
- Create table based on CSV header
- Import CSV data into MySQL table

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x
- MySQL server
- `mysql-connector-python` library

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/COMMANDO2406/CSVtoMySQL.git
   cd CSVtoMySQL
   ```

2. Install the required Python packages:

   ```bash
   pip install mysql-connector-python
   ```

3. Create a `config.py` file:

   ```python
   # config.py
   host = 'your_mysql_host'
   user = 'your_mysql_user'
   password = 'your_mysql_password'
   ```

4. Prepare your CSV file:
   Ensure you have a CSV file named `main.csv` in the same directory as the script. The CSV file should have a header row with column names matching the ones you will specify in the script.

# Usage

1. **Run the script:**

   ```bash
   python csv_to_mysql.py
   ```

2. **Enter the required information when prompted:**
   - **Database name:** Enter the name of the database you want to use. If it doesn't exist, it will be created.
   - **Table name:** Enter the name of the table where the data will be imported.
   - **Column names:** Enter the column names separated by commas. These should match the columns in your CSV file.

## Example

Here is an example of how to use the script:

1. **Prepare your CSV file (`main.csv`):**

   ```csv
   name,age,city
   Alice,30,New York
   Bob,25,Los Angeles
   ```

2. **Run the script:**

   ```bash
   python csv_to_mysql.py
   ```

3. **Enter the following when prompted:**

   ```
   Enter database name: my_database
   Enter table name: people
   Enter column names (Separated by commas): name,age,city
   ```

4. **The script will output:**

   ```
   Connected successfully
   Database 'my_database' created successfully
   Data imported successfully.
   ```
