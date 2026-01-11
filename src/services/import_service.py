
import csv
import json
import os
from src.repositories.product_repository import ProductRepository
from src.repositories.category_repository import CategoryRepository

class ImportService:
    def __init__(self):
        self.product_repo = ProductRepository()
        self.category_repo = CategoryRepository()

    def import_categories_from_csv(self, file_path):
        """Import categories from a CSV file (format: name)."""
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return False
        
        count = 0
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader, None)  # Skip header if present
                for row in reader:
                    if row:
                        self.category_repo.create(row[0])
                        count += 1
            print(f"Imported {count} categories from CSV.")
            return True
        except Exception as e:
            print(f"Error importing categories: {e}")
            return False

    def import_products_from_json(self, file_path):
        """Import products from a JSON file."""
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return False

        count = 0
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                products = json.load(f)
                for p in products:
                    # Basic validation or lookup could go here
                    self.product_repo.create(
                        category_id=p.get('category_id'),
                        name=p.get('name'),
                        description=p.get('description'),
                        price=p.get('price'),
                        is_active=p.get('is_active', True)
                    )
                    count += 1
            print(f"Imported {count} products from JSON.")
            return True
        except Exception as e:
            print(f"Error importing products: {e}")
            return False
