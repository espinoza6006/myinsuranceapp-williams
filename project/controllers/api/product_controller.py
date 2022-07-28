# -*- coding: utf-8 -*-
__version__ = '0.1'

from itertools import product
from project import app
from flask import jsonify, request
from project.persistence.products_dao import *
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route('/api/v1/products/', methods=['GET'])
@jwt_required()
def api_get_products():
    # print(get_jwt_identity)
    products = get_products()
    return jsonify(products)


@app.route('/api/v1/products/<id>', methods=['GET'])
@jwt_required()
def api_get_product(id):
    # print(get_jwt_identity)
    product = get_product(id)
    return jsonify(product)


@app.route('/api/v1/products/<id>', methods=['POSt'])
@jwt_required()
def api_update_product(id):
    # print(get_jwt_identity)
    product = request.json
    ok = edit_product(product["name"], product["description"],
                        product["cost"], product["is_active"], id)

    return jsonify({'ok': ok})

@app.route('/api/v1/products/<id>', methods=['DELETE'])
@jwt_required()
def api_delete_product(id):
    # print(get_jwt_identity)
    ok = delete_product(id)
    return jsonify({'ok': ok})


@app.route('/api/v1/products/', methods=['POST'])
@jwt_required()
def api_post_products():
    # print(get_jwt_identity)
    product = request.json
    # print(product)
    ok = create_product(product["name"], product["description"],
                        product["cost"], product["is_active"])
    return jsonify({'ok': ok})
