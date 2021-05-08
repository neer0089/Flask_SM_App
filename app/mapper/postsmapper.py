"""Post Mapper Module."""

from app.mapper.mapper import Mapper
from bson import ObjectId


def data_helper(data) -> dict:
    """Convert mongodb query into a dict."""
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
        """Add a new post to the database."""
        posts_collection = self.posts_collection
        posts_collection.insert_one(post)

    def get_posts(self, username):
        """Get all post from the database for a `user`."""
        posts_collection = self.posts_collection
        posts = posts_collection.find({"user": username})
        result = []
        for post in posts:
            result.append(data_helper(post))
        return result

    def like_post(self, post_id):
        """Add a like to a post."""
        posts_collection = self.posts_collection
        posts_collection.update_one({"_id": ObjectId(post_id)}, {"$inc": {"likes": 1}})

    def comment_post(self, post_id, comment):
        """Add a comment to a post."""
        posts_collection = self.posts_collection
        posts_collection.update_one(
            {"_id": ObjectId(post_id)},
            {'$push': {'comments': comment}}
            )

    @property
    def posts_collection(self):
        """Creates/gets posts collection from the social media DB."""
        return self.database.posts
