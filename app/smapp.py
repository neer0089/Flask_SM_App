"""Social Media Application."""

import sys
from flask import Flask
from flask_login import LoginManager
from app import smapp
from app.containers import ConfigContainer


config_container = ConfigContainer()
config_container.config.from_ini('./config.ini')

app = Flask(__name__)

# Enable loggin in to the application
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = config_container.config.sm.login_secret()


from app.controller import postscontroller, usercontroller
from app.mapper import postsmapper, usermapper
from app.model import user