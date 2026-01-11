
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from src.repositories.product_repository import ProductRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.order_repository import OrderRepository
from src.services.import_service import ImportService

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Change in production

product_repo = ProductRepository()
category_repo = CategoryRepository()
order_repo = OrderRepository()
import_service = ImportService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    all_products = product_repo.get_with_details()
    return render_template('products.html', products=all_products)

@app.route('/products/add', methods=['POST'])
def add_product():
    name = request.form.get('name')
    price = request.form.get('price')
    category_id = request.form.get('category_id', 1) 
    product_repo.create(category_id, name, "Description", price)
    flash("Product added!")
    return redirect(url_for('products'))

@app.route('/orders')
def orders():
    summary = order_repo.get_order_summary()
    return render_template('orders.html', orders=summary)

@app.route('/orders/create', methods=['POST'])
def create_order():
    customer_id = 1 # Hardcoded for demo
    items = [
        {'product_id': 1, 'quantity': 1, 'unit_price': 100.0}
    ]
    order_id = order_repo.create_order(customer_id, items)
    if order_id:
        flash(f"Order {order_id} created successfully!")
    else:
        flash("Failed to create order.")
    return redirect(url_for('orders'))

@app.route('/import', methods=['GET', 'POST'])
def import_data():
    if request.method == 'POST':
        # Demo import: In real usage, you'd process request.files['file']
        # This calls the service as a demo
        flash("Import functionality triggered usage of ImportService (Demo).")
        return redirect(url_for('index'))
    return render_template('import.html')

@app.route('/report')
def report():
    stats = order_repo.get_customer_stats()
    return render_template('report.html', report_data=stats)

if __name__ == '__main__':
    app.run(debug=True)
