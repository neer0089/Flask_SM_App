"""User Controller Module."""

import json

from flask import Response, request
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash

from app.containers import user_mapper_container
from app.smapp import app, login_manager


@app.route("/api/v1/user/register/", methods=["POST"])
def register():
    """User registration end point."""
    result = user_register(
        request.form["username"],
        generate_password_hash(request.form["password"])
        )
    res = json.dumps({'message': result})
    return Response(res, mimetype='application/json')


@app.route("/api/v1/user/login/", methods=["POST"])
def login():
    """Login end point."""
    result = user_login(request.form["username"], request.form["password"])
    res = json.dumps({"message": result})
    return Response(res, mimetype='application/json')


@app.route("/api/v1/user/logout/")
@login_required
def logout():
    """Logout end point."""
    result = user_logout()
    res = json.dumps({"message": result})
    return Response(res, mimetype='application/json')


def user_login(username, password):
    """Login the user identified by a username and password."""
    user_mapper = user_mapper_container.user_mapper()
    user = user_mapper.get_user(username)
    if user and user.check_password(password):
        login_user(user)
        return ("Login successful.")
    else:
        return ("Invalid username or password!")


def user_register(username, password):
    """Register a user."""
    user_mapper = user_mapper_container.user_mapper()
    user = user_mapper.get_user(username)
    if user:
        return ("User already registered. Please login.")
    else:
        user_mapper.add_user(username, password)
        return ("User registered successfully.")


def user_logout():
    """Logout a user."""
    logout_user()
    return ("Logout successfull.")


@login_manager.user_loader
def load_user(user_id):
    """Retrieve users from the DB."""
    user_mapper = user_mapper_container.user_mapper()
    return user_mapper.get_user(user_id)
