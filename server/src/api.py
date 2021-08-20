from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from src.models import db, UserModel

bp = Blueprint("api", __name__)


@bp.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    error = None

    if not username:
        error = "Username is required."
    elif not password:
        error = "Password is required."
    elif UserModel.query.filter_by(username=username).first() is not None:
        error = f"User {username} is already registered."

    if error is None:
        new_user = UserModel(username, generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return (
            jsonify(
                status="success",
                data={"username": username},
                message="user created successfully",
            ),
            200,
        )
    else:
        return (
            jsonify(
                status="failed",
                data={username: username},
                message="User was not created",
                error=error,
            ),
            418,
        )


@bp.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    error = None
    user = UserModel.query.filter_by(username=username).first()

    if user is None:
        error = "Incorrect username."
    elif not check_password_hash(user.password, password):
        error = "Incorrect password."

    if error is None:
        return (
            jsonify(
                status="success",
                data={"username": user.username},
                message="Login Successful",
            ),
            200,
        )
    else:
        return (
            jsonify(
                status="failed",
                data={username: username},
                message="Failed to login",
                error=error,
            ),
            418,
        )
