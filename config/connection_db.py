import mysql.connector
import os

class ConnectionDB:

    def __init__(self):
        pass

    def conn(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="dbinteligencia",
        )
        cursor = db.cursor()
        return db, cursor

        # host=os.environ.get("DB_HOST", "localhost"),
        #     user=os.environ.get("DB_USER" ,"root"),
        #     password=os.environ.get("DB_PASS", "root"),
        #     database=os.environ.get("DB_NAME", "dbinteligencia")