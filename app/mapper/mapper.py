"""Object Persistence."""

from app.containers import ConfigContainer
from app.containers import mongo_client_container


class Mapper:
    """
    Base class for mappers.

    Mappers are classes which handle persistence of objects into a database.
    This class provides a base class for other more specific mappers in the
    application.
    """

    def __init__(self):
        """
        Construct a Mapper.

        The Mappers constructor takes exactly one argument: The
        `DIContainer` which a mapper shall use to retrieve further
        dependencies.
        """
        super().__init__()
        self._config_container = ConfigContainer()

    @property
    def mongoclient(self):
        """Get the MongoClient that the mapper uses to talk to the DB."""
        client = mongo_client_container.mongo_client(
            self._config_container.config.sm.mongodb_host(),
            self._config_container.config.sm.mongodb_port()
        )
        return client

    @property
    def database(self):
        """Get the MongoDB database on which mappers work."""
        return self.mongoclient.social_media_db
