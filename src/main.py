from src.database.connection import db_connection

def main():
    print("Testing Database Connection...")
    try:
        conn = db_connection.connect()
        if conn.is_connected():
            print("Successfully connected to the database!")
            db_connection.close()
    except Exception as e:
        print(f"Failed to connect: {e}")

if __name__ == "__main__":
    main()
