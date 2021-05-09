"""Social Media Application."""

from flask import Flask
from flask_login import LoginManager

from app.containers import config_container


config_container.config.from_ini('./config.ini')

app = Flask(__name__)

# Enable loggin in to the application
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = config_container.config.sm.login_secret()


@app.route('/')
def home():
    """Home page endpoint."""
    return 'Welcome to the flask social media app!'


from app.controller import postscontroller, usercontroller  # noqa
from app.mapper import postsmapper, usermapper  # noqa
from app.model import user  # noqa
