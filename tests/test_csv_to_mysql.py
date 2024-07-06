import sys
import os
import mysql.connector
import requests

def test_mysql_connector_import():
    try:
        con = mysql.connector.connect(
            host="fake_host",
            user="fake_user",
            password="fake_password"
        )
    except mysql.connector.Error as err:
        # Since this is not real, we expect a connection error
        assert isinstance(err, mysql.connector.Error)
        print(f"mysql.connector is working: {err}")
    else:
        # If no exception was raised, it means something is wrong because it should fail
        assert False, "Expected a connection error but did not get one"
    finally:
        if 'con' in locals() and con.is_connected():
            con.close()

if __name__ == "__main__":
    test_mysql_connector_import()
