from flask import Blueprint, request, jsonify
from flask_login import login_user
from app import db, bcrypt
from app.models import User

auth = Blueprint("auth", __name__)


@auth.route("/test")
def test():
    return jsonify({
        "message": "Back conn"
    })



@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)

        return jsonify({
            "success":True,
            "username": user.username,
            "email": user.email
        })
    
    return jsonify({
        "success":False,
        "message": "Invalid email or password"
    }), 401