
from src.database.connection import db_connection
from mysql.connector import Error

class BaseRepository:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db = db_connection

    def get_all(self):
        """Fetch all records from the table."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print(f"Error fetching all from {self.table_name}: {e}")
            return []

    def get_by_id(self, item_id):
        """Fetch a single record by its ID."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name} WHERE id = %s"
            cursor.execute(query, (item_id,))
            result = cursor.fetchone()
            cursor.close()
            return result
        except Error as e:
            print(f"Error fetching by id from {self.table_name}: {e}")
            return None

    def delete(self, item_id):
        """Delete a record by its ID."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            query = f"DELETE FROM {self.table_name} WHERE id = %s"
            cursor.execute(query, (item_id,))
            conn.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error deleting from {self.table_name}: {e}")
            return False

    def _execute_query(self, query, params=None):
        """Helper method to execute a query (insert/update) and return the ID/rowcount."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            conn.commit()
            last_row_id = cursor.lastrowid
            row_count = cursor.rowcount
            cursor.close()
            return last_row_id if last_row_id else row_count
        except Error as e:
            print(f"Error executing query on {self.table_name}: {e}")
            return None
