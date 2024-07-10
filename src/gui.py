import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, QVBoxLayout, QHBoxLayout
import mysql.connector
import csv
from config import host, user, password

class CsvToMysqlApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('CSV to MySQL Importer')

        # Database Name
        db_label = QLabel('Database Name:')
        self.db_name = QLineEdit()

        # Table Name
        table_label = QLabel('Table Name:')
        self.table_name = QLineEdit()

        # Column Names
        columns_label = QLabel('Column Names (comma separated):')
        self.columns = QLineEdit()

        # CSV File Path
        csv_label = QLabel('CSV File Path:')
        self.csv_path = QLineEdit()
        browse_button = QPushButton('Browse')
        browse_button.clicked.connect(self.browse_file)

        # Import Button
        import_button = QPushButton('Import')
        import_button.clicked.connect(self.import_data)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(db_label)
        layout.addWidget(self.db_name)
        layout.addWidget(table_label)
        layout.addWidget(self.table_name)
        layout.addWidget(columns_label)
        layout.addWidget(self.columns)
        layout.addWidget(csv_label)

        csv_layout = QHBoxLayout()
        csv_layout.addWidget(self.csv_path)
        csv_layout.addWidget(browse_button)
        layout.addLayout(csv_layout)

        layout.addWidget(import_button)

        self.setLayout(layout)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")
        if file_path:
            self.csv_path.setText(file_path)

    def import_data(self):
        database_name = self.db_name.text()
        table_name = self.table_name.text()
        column_names = self.columns.text()
        csv_file_path = self.csv_path.text()

        if not database_name or not table_name or not column_names or not csv_file_path:
            QMessageBox.warning(self, 'Error', 'All fields are required')
            return

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

            columns = [f"{col.strip()} varchar(255)" for col in column_names.split(",")]
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
            cur.execute(create_table_query)

            with open(csv_file_path, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    insert_query = f"INSERT INTO {table_name} ({', '.join(column_names.split(','))}) values ({', '.join(['%s'] * len(row))})"
                    values = tuple(row)
                    cur.execute(insert_query, values)

            con.commit()
            con.close()
            QMessageBox.information(self, 'Success', 'Data imported successfully.')
        except mysql.connector.Error as err:
            QMessageBox.critical(self, 'Error', f"Error: {err}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CsvToMysqlApp()
    ex.show()
    sys.exit(app.exec_())
