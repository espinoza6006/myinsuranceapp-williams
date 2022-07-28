# -*- coding: utf-8 -*-
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_db_connection():
    conn = sqlite3.connect('./database/database.db')
    conn.row_factory = dict_factory
    # conn.row_factory = sqlite3.Row
    return conn
