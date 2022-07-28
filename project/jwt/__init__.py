from project.persistence.users_dao import get_user, get_user_by_passoword
from project import app
from flask_jwt_extended import create_access_token
from flask import request, jsonify


@app.route("/api/v1/token", methods=["POST"])
def create_token():
    # print(request.json)
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    # Query your database for username and password
    user = get_user_by_passoword(email, password)
    # print(user)
    if user is None:
        # the user was not found on the database
        return jsonify({"msg": "Bad username or password"}), 401
    
    # create a new token with the user id inside
    access_token = create_access_token(identity=user['id'])
    return jsonify({ "token": access_token, "user_id": user['id'] })