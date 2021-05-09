"""Fixtures for the test functions."""

import pytest
from mongomock import MongoClient
from dependency_injector import providers

from app.smapp import app
from app.containers import mongo_client_container


@pytest.fixture(scope='module')
def client():
    """Create a test client of flask app for testing."""
    with app.test_client() as client:
        # Establish an application context
        with app.app_context():
            yield client


@pytest.fixture(scope='module')
def mock_mongo():
    """Override Mongoclient with mock MongoClient for test."""
    mongo_client_container.mongo_client.override(providers.Singleton(MongoClient))
