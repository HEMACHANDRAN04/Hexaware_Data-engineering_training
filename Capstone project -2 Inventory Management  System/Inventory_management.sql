CREATE DATABASE inventory_management;

USE inventory_management;

CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(100),
    contact_number VARCHAR(15),
    city VARCHAR(50)
);


CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    reorder_level INT,
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

CREATE TABLE warehouses (
    warehouse_id INT PRIMARY KEY,
    warehouse_name VARCHAR(100),
    location VARCHAR(100)
);

CREATE TABLE stock_movements (
    movement_id INT PRIMARY KEY,
    product_id INT,
    warehouse_id INT,
    movement_type VARCHAR(20),
    quantity INT,
    movement_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);

INSERT INTO suppliers VALUES
(1,'ABC Traders','9876543210','Chennai'),
(2,'Tech Supplies','9876543211','Coimbatore'),
(3,'Fresh Mart','9876543212','Madurai'),
(4,'Global Goods','9876543213','Salem'),
(5,'Vision Suppliers','9876543214','Erode'),
(6,'NextGen Traders','9876543215','Trichy'),
(7,'Prime Suppliers','9876543216','Vellore'),
(8,'Mega Mart','9876543217','Tirunelveli'),
(9,'Fast Supply','9876543218','Karur'),
(10,'Smart Traders','9876543219','Namakkal');

INSERT INTO products VALUES
(101,'Laptop','Electronics',55000,10,1),
(102,'Mouse','Electronics',500,20,2),
(103,'Keyboard','Electronics',1200,15,3),
(104,'Monitor','Electronics',9000,8,4),
(105,'Printer','Electronics',15000,5,5),
(106,'Scanner','Electronics',7000,6,6),
(107,'Speaker','Electronics',3000,12,7),
(108,'Router','Electronics',2500,10,8),
(109,'Hard Disk','Electronics',4500,7,9),
(110,'Pendrive','Electronics',800,25,10);

INSERT INTO warehouses VALUES
(1,'Central Warehouse','Chennai'),
(2,'North Warehouse','Coimbatore'),
(3,'South Warehouse','Madurai'),
(4,'East Warehouse','Salem'),
(5,'West Warehouse','Erode'),
(6,'Main Storage','Trichy'),
(7,'Backup Storage','Vellore'),
(8,'City Warehouse','Tirunelveli'),
(9,'Tech Warehouse','Karur'),
(10,'Retail Warehouse','Namakkal');

INSERT INTO stock_movements VALUES
(1,101,1,'IN',50,'2026-05-01'),
(2,102,2,'IN',30,'2026-05-01'),
(3,103,3,'OUT',5,'2026-05-02'),
(4,104,4,'IN',20,'2026-05-02'),
(5,105,5,'OUT',2,'2026-05-03'),
(6,106,6,'IN',15,'2026-05-03'),
(7,107,7,'OUT',4,'2026-05-04'),
(8,108,8,'IN',40,'2026-05-04'),
(9,109,9,'OUT',3,'2026-05-05'),
(10,110,10,'IN',60,'2026-05-05');

SELECT * FROM suppliers;
SELECT * FROM products;
SELECT * FROM warehouses;
SELECT * FROM stock_movements;

INSERT INTO products VALUES
(111, "Webcam", "Electronics", 2500, 8, 2);

INSERT INTO products VALUES
(112,'Headphones','Electronics',2000,12,3),
(113,'Charger','Electronics',1500,15,4);

SELECT * FROM products;

UPDATE products 
SET price=600
WHERE product_id=102;

UPDATE products
SET price=70000
WHERE product_id=101;

DELETE FROM products 
WHERE product_id=112;

DELETE FROM products
WHERE product_id=113;

DELETE FROM products
WHERE product_id=111;

ALTER TABLE products
ADD current_stock INT;

UPDATE products SET current_stock = 50 WHERE product_id = 101;
UPDATE products SET current_stock = 30 WHERE product_id = 102;
UPDATE products SET current_stock = 5 WHERE product_id = 103;
UPDATE products SET current_stock = 20 WHERE product_id = 104;
UPDATE products SET current_stock = 2 WHERE product_id = 105;
UPDATE products SET current_stock = 15 WHERE product_id = 106;
UPDATE products SET current_stock = 4 WHERE product_id = 107;
UPDATE products SET current_stock = 40 WHERE product_id = 108;
UPDATE products SET current_stock = 3 WHERE product_id = 109;
UPDATE products SET current_stock = 60 WHERE product_id = 110;

SELECT * FROM products;

DELIMITER //

CREATE PROCEDURE low_stock_products()
BEGIN

SELECT 
    product_id,
    product_name,
    current_stock,
    reorder_level
FROM products
WHERE current_stock < reorder_level;

END //

DELIMITER ;

CALL low_stock_products();

