"""Dependency Injection Containers Module."""

from dependency_injector import containers, providers
from pymongo import MongoClient


class ConfigContainer(containers.DeclarativeContainer):
    """Container for Config object."""

    config = providers.Configuration('config')


config_container = ConfigContainer()


class MongoClientContainer(containers.DeclarativeContainer):
    """Container for MongoClient object."""

    mongo_client = providers.Singleton(MongoClient)


mongo_client_container = MongoClientContainer()

from app.mapper.usermapper import UserMapper  # noqa


class UserMapperContainer(containers.DeclarativeContainer):
    """Container for UserMapper object."""

    user_mapper = providers.Singleton(UserMapper)


user_mapper_container = UserMapperContainer()

from app.mapper.postsmapper import PostsMapper  # noqa


class PostsMapperContainer(containers.DeclarativeContainer):
    """Container for PostsMapper object."""

    posts_mapper = providers.Singleton(PostsMapper)


posts_mapper_container = PostsMapperContainer()
