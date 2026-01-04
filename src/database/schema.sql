-- E-shop Database Schema

-- Table 1: Categories
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Table 2: Products
-- Includes: Float (price), Boolean (is_active)
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price FLOAT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Table 3: Customers
-- Includes: String (email), DateTime (created_at)
CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table 4: Orders
-- Includes: Enum (via check constraint), DateTime (order_date)
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) NOT NULL CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')),
    total_price FLOAT DEFAULT 0.0,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Table 5: Order Items (M:N Relationship between Products and Orders)
-- Includes: Float (unit_price)
CREATE TABLE order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price FLOAT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id),
    CONSTRAINT unique_order_product UNIQUE (order_id, product_id)
);

-- View 1: Product Details (Joins products and categories)
CREATE VIEW view_product_details AS
SELECT 
    p.id, 
    p.name AS product_name, 
    c.name AS category_name, 
    p.price, 
    p.is_active
FROM products p
LEFT JOIN categories c ON p.category_id = c.id;

-- View 2: Order Summaries (Joins orders and customers)
CREATE VIEW view_order_summary AS
SELECT 
    o.id AS order_id,
    o.order_date,
    o.status,
    o.total_price,
    c.first_name,
    c.last_name,
    c.email
FROM orders o
JOIN customers c ON o.customer_id = c.id;
