"""Dependency Injection Containers Module."""

from dependency_injector import containers, providers
from pymongo import MongoClient


class ConfigContainer(containers.DeclarativeContainer):
    """Container for Config object."""

    config = providers.Configuration('config')


class MongoClientContainer(containers.DeclarativeContainer):
    """Container for MongoClient object."""

    mongo_client = providers.Singleton(MongoClient)


from app.mapper.usermapper import UserMapper # noqa


class UserMapperContainer(containers.DeclarativeContainer):
    """Container for UserMapper object."""

    user_mapper = providers.Singleton(UserMapper)


from app.mapper.postsmapper import PostsMapper # noqa


class PostsMapperContainer(containers.DeclarativeContainer):
    """Container for PostsMapper object."""

    posts_mapper = providers.Singleton(PostsMapper)
