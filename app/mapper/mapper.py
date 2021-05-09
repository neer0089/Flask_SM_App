"""Object Persistence."""

from app.containers import config_container
from app.containers import mongo_client_container


class Mapper:
    """
    Base class for mappers.

    Mappers are classes which handle reading and writing into a database.
    This class provides a base class for other more specific mappers in the
    application.
    """

    @property
    def mongoclient(self):
        """Get the MongoClient that the mapper uses to talk to the DB."""
        client = mongo_client_container.mongo_client(
            config_container.config.sm.mongodb_host(),
            config_container.config.sm.mongodb_port()
        )
        return client

    @property
    def database(self):
        """Get the MongoDB database on which mappers work."""
        return self.mongoclient.social_media_db
