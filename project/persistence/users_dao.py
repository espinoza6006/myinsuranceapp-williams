# -*- coding: utf-8 -*-
from werkzeug.exceptions import abort
from project.persistence import get_db_connection


def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return users


def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?',
                        (user_id,)).fetchone()
    conn.close()
    return user


def get_user_by_passoword(email, password):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE email = ? AND password = ?',
                        (email, password,)).fetchone()
    conn.close()
    return user


def create_user(fullname, email, birthdate, country, city, address, password):
    conn = get_db_connection()
    conn.execute('INSERT INTO users (fullname, email, birthdate, country, city, address,password) VALUES (?, ?, ?, ?, ? , ?,?  )',
                 (fullname, email, birthdate, country, city, address, password))
    conn.commit()
    conn.close()
    return True


def edit_user(fullname, email, birthdate, country, city, address, password, id):
    conn = get_db_connection()
    conn.execute('UPDATE users SET fullname = ?, email = ?, birthdate=?, country=?, city=?, address=?,password=? '
                 ' WHERE id = ?',
                 (fullname, email, birthdate, country, city, address, password, id))
    conn.commit()
    conn.close()
    return True


def delete_user(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return True

def get_user_products(user_id):
    conn = get_db_connection()
    products = conn.execute('SELECT products.* from products, product_users WHERE products.id=product_users.product_id AND product_users.user_id=?',
                        (user_id,)).fetchall()
    conn.close()
    return products

def add_product_for_user(user_id, product_id):
    conn = get_db_connection()
    conn.execute('INSERT INTO product_users (product_id, user_id) VALUES (?, ?)',
                 (product_id, user_id))
    conn.commit()
    conn.close()
    return True
