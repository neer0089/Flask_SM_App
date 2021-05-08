"""Containers module."""

from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide, Provider
from pymongo import MongoClient
from app.config import Config


class ConfigContainer(containers.DeclarativeContainer):
    config = providers.Configuration('config')


class MongoClientContainer(containers.DeclarativeContainer):
    mongo_client = providers.Singleton(MongoClient)


from app.mapper.usermapper import UserMapper


class UserMapperContainer(containers.DeclarativeContainer):
    user_mapper = providers.Singleton(UserMapper)
