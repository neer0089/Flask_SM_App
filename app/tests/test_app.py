"""Tests for the application."""


def test_home_page(client):
    """
    Given a flask application
    when the '/' route is called
    checks for valid response.
    """
    response = client.get('/')
    assert response.status_code == 200


def test_mongo(client, mock_mongo):
    """a"""
    request = {
        "username": "testuser2",
        "password": "secret"
    }
    response = client.post(
        '/api/v1/user/register/',
        data=request
        )
    assert response.status_code == 200
