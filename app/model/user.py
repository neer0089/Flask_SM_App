from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin):
    """
    User management.

    This class is used to represent users that can log in to the application
    to use restricted APIs.
    """

    def __init__(self, username, password):
        """Create a User object."""
        self._username = username
        self._password_hash = password

    def is_authenticated():
        return True

    def is_active():
        return True

    def is_anonymous():
        return False

    def get_id(self):
        return self._username

    def check_password(self, password):
        return check_password_hash(self._password_hash, password)