
from src.repositories.base_repository import BaseRepository

class ProductRepository(BaseRepository):
    def __init__(self):
        super().__init__('products')

    def create(self, category_id, name, description, price, is_active=True):
        """Create a new product."""
        query = """
            INSERT INTO products (category_id, name, description, price, is_active) 
            VALUES (%s, %s, %s, %s, %s)
        """
        return self._execute_query(query, (category_id, name, description, price, is_active))

    def update(self, product_id, category_id, name, description, price, is_active):
        """Update an existing product."""
        query = """
            UPDATE products 
            SET category_id = %s, name = %s, description = %s, price = %s, is_active = %s 
            WHERE id = %s
        """
        return self._execute_query(query, (category_id, name, description, price, is_active, product_id))
    
    def get_with_details(self):
        """Fetch all products with category names (using a View is also an option, or JOIN here)."""
        # Using the View defined in schema.sql
        try:
            conn = self.db.connect()
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM view_product_details"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(f"Error fetching product details: {e}")
            return []
