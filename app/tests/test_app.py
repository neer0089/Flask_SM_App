"""Tests for the application."""


def test_home_page(client):
    """
    Given a flask application
    when the '/' route is called
    checks for valid response.
    """
    response = client.get('/')
    assert response.status_code == 200


def test_user_registration(client, mock_mongo):
    """
    Given a flask application
    When the '/api/v1/user/register/' route is called
    Then check that a '200' status code is returned.
    """
    request = {
        "username": "testuser",
        "password": "secret"
    }
    response = client.post(
        '/api/v1/user/register/',
        data=request
        )
    assert response.status_code == 200
