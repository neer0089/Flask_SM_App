from dependency_injector import containers, providers
from app.mapper.mapper import Mapper


def data_helper(data) -> dict:
    """Helper function to convert mongodb query into a dict."""
    return {
        "id": str(data["_id"]),
        "post_content": data["post_content"],
        "likes": data["likes"],
        "comments": data["comments"],
        "user": data["user"]
    }


class PostsMapper(Mapper):
    """Store information about logged in users."""

    def add_post(self, post):
        """Adds a new post to the database."""
        posts_collection = self.posts_collection
        posts_collection.insert_one(post)

    def get_posts(self, username):
        """Gets all post from the database for a `user`."""
        posts_collection = self.posts_collection
        posts = posts_collection.find({"user": username})
        result = []
        for post in posts:
            result.append(data_helper(post))
        return result

    @property
    def posts_collection(self):
        """Creates/gets posts collection from the social media DB."""
        return self.database.posts