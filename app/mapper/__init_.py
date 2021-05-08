from app.smapp import create_mongo_client
from pymongo import MongoClient


class Mapper:
    """
    Base class for mappers.

    Mappers are classes which handle persistence of objects into a database.
    This class provides a base class for other more specific mappers in the
    application.
    """

    def __init__(self):
        """Construct a Mapper."""
        super().__init__()

    @property
    def mongoclient(self):
        """Get the MongoClient that the mapper uses to talk to the DB."""
        return create_mongo_client()

    @property
    def database(self):
        """Get the MongoDB database on which mappers work."""
        return self.mongoclient.social_media_db