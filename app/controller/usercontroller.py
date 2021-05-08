from app.smapp import app
from app.mapper.usermapper import UserMapper
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, redirect, Response
from flask_login import current_user, login_user, logout_user, login_required
from flask_login import LoginManager
from app.smapp import login_manager
import json
from app.containers import UserMapperContainer


@app.route("/api/v1/user/register/", methods=["POST"])
def register():
    """Login end point."""
    form_data = request.form
    missing_fields = []

    for k, v in form_data.items():
        if v == "":
            missing_fields.append(k)

    if missing_fields:
        message = f"Missing fields for {', '.join(missing_fields)}"
        res = json.dumps({'message': message})
        return Response(res, status=422, mimetype='application/json')

    result = register(
        request.form["username"],
        generate_password_hash(request.form["password"])
        )
    res = json.dumps({'message': result})
    return Response(res, mimetype='application/json')
         

@app.route("/api/v1/user/login/", methods=["POST"])
def login():
    """Login end point."""
    result = login(request.form["username"], request.form["password"])
    res = json.dumps({"message": result})
    return Response(res, mimetype='application/json')

@app.route("/api/v1/user/logout/")
@login_required
def logout():
    """Logout end point."""
    result = logout()
    res = json.dumps({"message": result})
    return Response(res, mimetype='application/json')


def login(username, password):
    """Login the user identified by a username and password."""

    user_mapper = UserMapperContainer.user_mapper()
    user = user_mapper.get_user(username)
    if user and user.check_password(password):
        login_user(user)
        return ("Login successful.")
    else:
        return ("Invalid username or password!")

def register(username, password):
    """Registers a user."""
    user_mapper = UserMapperContainer.user_mapper()
    user = user_mapper.get_user(username)
    if user:
        return ("User already registered. Please login.")
    else:
        user_mapper.add_user(username, password)
        return ("User registered successfully.")

def logout():
    """Logouts a user."""
    logout_user()
    return ("Logout successfull.")

@login_manager.user_loader
def load_user(user_id):
    """Retrieve users from the DB."""
    user_mapper = UserMapperContainer.user_mapper()
    return user_mapper.get_user(user_id)
