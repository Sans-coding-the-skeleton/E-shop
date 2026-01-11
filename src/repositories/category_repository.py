

from src.repositories.base_repository import BaseRepository

class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__('categories')

    def create(self, name):
        """Create a new category."""
        query = "INSERT INTO categories (name) VALUES (%s)"
        return self._execute_query(query, (name,))

    def update(self, category_id, name):
        """Update an existing category."""
        query = "UPDATE categories SET name = %s WHERE id = %s"
        return self._execute_query(query, (name, category_id))
