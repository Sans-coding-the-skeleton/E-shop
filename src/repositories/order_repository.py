
from src.repositories.base_repository import BaseRepository
from mysql.connector import Error

class OrderRepository(BaseRepository):
    def __init__(self):
        super().__init__('orders')

    def create_order(self, customer_id, items):
        """
        Create a new order with items in a single transaction.
        items: list of dicts {'product_id': int, 'quantity': int, 'unit_price': float}
        """
        conn = None
        cursor = None
        try:
            conn = self.db.connect()
            conn.start_transaction()
            cursor = conn.cursor()

            # Calculate total price
            total_price = sum(item['quantity'] * item['unit_price'] for item in items)

            # 1. Insert Order
            query_order = """
                INSERT INTO orders (customer_id, status, total_price) 
                VALUES (%s, 'pending', %s)
            """
            cursor.execute(query_order, (customer_id, total_price))
            order_id = cursor.lastrowid

            # 2. Insert Order Items
            query_item = """
                INSERT INTO order_items (order_id, product_id, quantity, unit_price)
                VALUES (%s, %s, %s, %s)
            """
            for item in items:
                cursor.execute(query_item, (
                    order_id, 
                    item['product_id'], 
                    item['quantity'], 
                    item['unit_price']
                ))

            conn.commit()
            print(f"Order {order_id} created successfully with {len(items)} items.")
            return order_id

        except Error as e:
            if conn:
                conn.rollback()
            print(f"Transaction failed, rolled back. Error: {e}")
            return None
        finally:
            if cursor:
                cursor.close()

    def get_order_summary(self):
        """Fetch aggregated order data using the View."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM view_order_summary"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print(f"Error fetching order summary: {e}")
            return []

    def get_customer_stats(self):
        """
        Fetch aggregated statistics: Customers -> Orders -> Items.
        Satisfies requirement: Aggregated data from at least 3 tables.
        """
        try:
            conn = self.db.connect()
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT 
                    c.id, c.email, 
                    COUNT(DISTINCT o.id) as order_count, 
                    COALESCE(SUM(oi.quantity), 0) as total_items,
                    COALESCE(SUM(oi.quantity * oi.unit_price), 0) as total_spent
                FROM customers c
                JOIN orders o ON c.id = o.customer_id
                JOIN order_items oi ON o.id = oi.order_id
                GROUP BY c.id, c.email
            """
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print(f"Error fetching customer stats: {e}")
            return []
