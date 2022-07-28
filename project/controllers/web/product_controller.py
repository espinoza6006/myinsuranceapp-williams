# -*- coding: utf-8 -*-
__version__ = '0.1'

from project import app
from flask import render_template, request, url_for, flash, redirect, session
from project.persistence.products_dao import *


@app.route('/products/')
def products():
    if not session.get("id"):
        return redirect(url_for('login'))
    products = get_products()
    return render_template('product/products.html', products=products)


@app.route('/products/<int:product_id>')
def product(product_id):
    if not session.get("id"):
        return redirect(url_for('login'))
    theproduct = get_product(product_id)
    return render_template('product/product.html', product=theproduct)


@app.route('/products/create', methods=('GET', 'POST'))
def createproduct():
    if not session.get("id"):
        return redirect(url_for('login'))
    if request.method == 'POST':
        app.logger.info(request.form)
        name = request.form['name']
        description = request.form['description']
        cost = request.form['cost']
        is_active = request.form['is_active']

        if not name:
            flash('name is required!')
        else:
            create_product(name, description, cost, is_active)
            return redirect(url_for('products'))

    return render_template('product/create.html', product=product)


@app.route('/products/<int:id>/edit', methods=('GET', 'POST'))
def editproduct(id):
    if not session.get("id"):
        return redirect(url_for('login'))
    product = get_product(id)

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        cost = request.form['cost']
        is_active = request.form['is_active']

        if not name:
            flash('Full name is required!')
        else:
            edit_product(name, description, cost, is_active, id)
            return redirect(url_for('products'))

    return render_template('product/edit.html', product=product)


@app.route('/products/<int:id>/delete', methods=('POST',))
def deleteproduct(id):
    if not session.get("id"):
        return redirect(url_for('login'))
    product = get_product(id)
    ok = delete_product(id)
    flash('"{}" was successfully deleted!'.format(product['name']))
    return redirect(url_for('products'))
