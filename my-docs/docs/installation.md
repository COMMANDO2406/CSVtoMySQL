# Installation

## Prerequisites

1. Python 3.x
2. `mysql-connector-python` library
3. MySQL server

## Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/COMMANDO2406/CSVtoMySQL.git
   cd CSVtoMySQL
   ```

2. **Install the required Python packages:**

   ```bash
   pip install mysql-connector-python
   ```

3. **Create a `config.py` file:**

   ```python
   # config.py
   host = 'your_mysql_host'
   user = 'your_mysql_user'
   password = 'your_mysql_password'
   ```

4. **Prepare your CSV file:**
   Ensure you have a CSV file named `main.csv` in the same directory as the script. The CSV file should have a header row with column names matching the ones you will specify in the script.
