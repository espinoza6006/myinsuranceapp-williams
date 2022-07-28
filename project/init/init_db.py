import sqlite3
import datetime as dt

connection = sqlite3.connect('./database/database.db')

# USERS
with open('./project/init/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Users (fullname, email, birthdate, country, city, address, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('John doe', 'jd@myinsuranceapp.com', '2005-01-24',
             'Spain', 'Madrid', 'B Street 1', 'passwordjd')
            )

cur.execute("INSERT INTO Users (fullname, email, birthdate, country, city, address, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Ann Smith', 'as@myinsuranceapp.com', '2010-07-02',
             'England', 'London', 'C Street 1', 'passwordas')
            )

# PRODUCTS
cur.execute("INSERT INTO Products (name , description , cost, is_active) VALUES (?, ?, ?, ?)",
            ('Property & Casualty Insurance', 'Whether you’re looking to protect your personal property, like your home or automobile, or to cover your personal liability, we’re here to help you plan your future (or your next adventure) from birth to retirement. Our individual, retail and corporate clients enjoy an extensive line of products and services in all insurance business lines, designed to protect them against risks.', 50, True)
            )

cur.execute("INSERT INTO Products (name , description , cost, is_active) VALUES (?, ?, ?, ?)",
            ('Health & Life Insurance', 'As your life changes, our solutions change with you— giving you the confidence you need to look after the ones you love. Addressing the health and wellbeing protection needs of our clients worldwide, we offer international health, life and disability insurance, as well as a wide range of health and protection services to private individuals, families, organizations and partners.', 20, True)
            )

cur.execute("INSERT INTO Products (name , description , cost, is_active) VALUES (?, ?, ?, ?)",
            ('Life & Disability Insurance', 'Our Life and Disability plans are aimed to safeguard the future of your employees and their families, no matter what the future holds.', 100, True)
            )

cur.execute("INSERT INTO Products (name , description , cost, is_active) VALUES (?, ?, ?, ?)",
            ('COVID-19 support', 'We cover treatment for COVID-19. Vaccination costs are also covered if you have this benefit within your policy. Please note, cover is subject to terms and conditions, benefit limits and area of cover of the policy and costs must be reasonable and customary.', 0, True)
            )

# USER-PRODUCTS
cur.execute("INSERT INTO product_users (product_id, user_id) VALUES (?, ?)",
            (1, 1))

cur.execute("INSERT INTO product_users (product_id, user_id) VALUES (?, ?)",
            (2, 1))            

cur.execute("INSERT INTO product_users (product_id, user_id) VALUES (?, ?)",
            (1, 2))
            
connection.commit()
connection.close()
