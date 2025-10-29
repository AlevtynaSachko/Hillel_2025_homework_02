DROP DATABASE IF EXISTS hair_cosmetics_shop;
CREATE DATABASE hair_cosmetics_shop WITH ENCODING 'UTF8';
\c hair_cosmetics_shop

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    price NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    category_id INT NOT NULL REFERENCES categories(id) ON DELETE RESTRICT
);

INSERT INTO categories (name) VALUES
('Shampoos'),
('Conditioners'),
('Masks'),
('Hair Sprays'),
('Hair Colors');

INSERT INTO products (name, description, price, category_id) VALUES
('Shampoo Repair & Shine 300ml', 'For damaged hair, keratin + argan oil', 289.00,
 (SELECT id FROM categories WHERE name = 'Shampoos')),
('Shampoo Volume Boost 250ml', 'Gentle cleansing, root volume effect', 245.00,
 (SELECT id FROM categories WHERE name = 'Shampoos')),
('Conditioner Silky Smooth 250ml', 'Softens and makes combing easier', 265.00,
 (SELECT id FROM categories WHERE name = 'Conditioners')),
('Mask Deep Recovery 200ml', 'Intensive hair recovery, use 1-2 times a week', 349.00,
 (SELECT id FROM categories WHERE name = 'Masks')),
('Thermal Protection Spray 150ml', 'Protects up to 220°C, anti-frizz effect', 310.00,
 (SELECT id FROM categories WHERE name = 'Hair Sprays')),
('Shine Spray 100ml', 'Light finish without weighing hair down', 299.00,
 (SELECT id FROM categories WHERE name = 'Hair Sprays')),
('Hair Color 6.0 Dark Blonde', 'Permanent coloring + care complex', 199.00,
 (SELECT id FROM categories WHERE name = 'Hair Colors')),
('Hair Color 9.1 Ash Blonde', '100% gray coverage, long-lasting color', 219.00,
 (SELECT id FROM categories WHERE name = 'Hair Colors'));




SELECT
    p.id,
    p.name AS product_name,
    p.price,
    c.name AS category_name
FROM products p
JOIN categories c ON p.category_id = c.id
ORDER BY c.name, p.name;

