from abc import ABC, abstractmethod
from src.database.connection import db_manager

class BaseRepository(ABC):
    def __init__(self):
        self.db = db_manager

    def _execute_query(self, query, params=None, fetch=False):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(query, params or ())
            if fetch:
                result = cursor.fetchall()
                return result
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            conn.rollback()
            print(f"QUERY ERROR: {query}")
            print(f"PARAMS: {params}")
            print(f"EXCEPTION: {e}")
            raise
        finally:
            cursor.close()

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass
