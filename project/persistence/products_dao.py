# -*- coding: utf-8 -*-
from werkzeug.exceptions import abort
from project.persistence import get_db_connection

def get_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return products

def get_product(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?',
                        (product_id,)).fetchone()
    conn.close()
    if product is None:
        abort(404)
    return product

def create_product(name, description, cost, is_active):
    conn = get_db_connection()
    conn.execute('INSERT INTO products (name, description, cost, is_active) VALUES (?, ?, ?, ?)',
                         (name, description, cost, is_active))
    conn.commit()
    conn.close()
    return True

def edit_product(name, description, cost, is_active, id):
    conn = get_db_connection()
    conn.execute('UPDATE products SET name = ?, description = ?, cost=?, is_active=?'
                         ' WHERE id = ?',
                         (name, description, cost, is_active, id))
    conn.commit()
    conn.close()
    return True

def delete_product(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return True
