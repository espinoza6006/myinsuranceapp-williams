# -*- coding: utf-8 -*-
__version__ = '0.1'

from project import app
from flask import jsonify, request
from project.persistence.users_dao import *
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route('/api/v1/users/', methods=['GET'])
@jwt_required()
def api_get_users():
    # print(get_jwt_identity)
    users = get_users()
    return jsonify(users)


@app.route('/api/v1/users/<id>', methods=['GET'])
@jwt_required()
def api_get_user(id):
    # print(get_jwt_identity)
    user = get_user(id)
    return jsonify(user)


@app.route('/api/v1/users/<id>', methods=['POSt'])
@jwt_required()
def api_update_user(id):
    # print(get_jwt_identity)
    user = request.json
    ok = edit_user(user["fullname"], user["email"], user["birthdate"], user["country"], user["city"], user["address"], user["password"], id)

    return jsonify({'ok': ok})


@app.route('/api/v1/users/<id>', methods=['DELETE'])
@jwt_required()
def api_delete_user(id):
    # print(get_jwt_identity)
    ok = delete_user(id)
    return jsonify({'ok': ok})


@app.route('/api/v1/users/', methods=['POST'])
def api_create_user():
    # print(get_jwt_identity)
    user = request.json
    print(user)
    ok = create_user(user["fullname"], user["email"], user["birthdate"],
                     user["country"], user["city"], user["address"], user["password"])
    return jsonify({'ok': ok})

@app.route('/api/v1/users/<id>/products', methods=['GET'])
@jwt_required()
def api_get_user_products(id):
    # print(get_jwt_identity)
    products = get_user_products(id)
    return jsonify(products)

@app.route('/api/v1/users/<id>/products', methods=['POST'])
@jwt_required()
def api_add_product_for_user(id):
    # print(get_jwt_identity)
    product = request.json
    ok = add_product_for_user(id, product["id"])
    products = get_user_products(id)
    return jsonify(products)
