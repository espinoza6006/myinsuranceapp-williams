DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS product_users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fullname TEXT NOT NULL,
    email TEXT NOT NULL,
    birthdate TIMESTAMP ,
    country TEXT ,
    city TEXT ,
    address TEXT, 
    password TEXT
);


CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    name TEXT ,
    description TEXT,
    cost float ,
    is_active boolean
);

CREATE TABLE product_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY(product_id) REFERENCES products(id),
    FOREIGN KEY(user_id) REFERENCES users(id)
);