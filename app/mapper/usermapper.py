from dependency_injector import containers, providers
from app.model.user import User
from app.mapper.mapper import Mapper


class UserMapper(Mapper):
    """Store information about logged in users."""

    def get_user(self, username):
        """Retrieve user data from the database."""
        user_collection = self.user_collection
        result = user_collection.find_one({"username": username})
        if result is not None:
            user = User(result["username"], result["password"])
            return user
        else:
            None

    def add_user(self, username, password):
        """Write user data into the database."""
        user_collection = self.user_collection
        doc = {"username": username, "password": password}
        result = user_collection.replace_one({"username": username}, doc)
        if result.matched_count == 0:
            user_collection.insert_one(doc)

    @property
    def user_collection(self):
        """Creates/gets users collection from the social media DB."""
        return self.database.users
