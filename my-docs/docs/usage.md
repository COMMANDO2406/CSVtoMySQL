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
