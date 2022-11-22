import mysql.connector
import os

class ConnectionDB:

    def __init__(self):
        pass

    def conn(self):
        db = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "db-comprehend.crfvyq6er0ts.us-east-1.rds.amazonaws.com"),
            user=os.environ.get("DB_USER" ,"root"),
            password=os.environ.get("DB_PASS", "ttcc2022"),
            database=os.environ.get("DB_NAME", "dbinteligencia")
        )
        cursor = db.cursor()
        return db, cursor