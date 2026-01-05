import mysql.connector
from mysql.connector import Error
from src.config import config

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self):
        if self.connection and self.connection.is_connected():
            return self.connection

        db_config = config.get_db_config()
        try:
            self.connection = mysql.connector.connect(
                host=db_config.get("host"),
                user=db_config.get("user"),
                password=db_config.get("password"),
                database=db_config.get("database"),
                port=db_config.get("port", 3306)
            )
            return self.connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed.")

db_connection = DatabaseConnection()
