"""Tests for the application."""
import json


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
    Then check that valid response is returned.
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


def test_user_login(client, mock_mongo):
    """
    Given a flask application
    When the '/api/v1/user/login/' route is called
    Then check that valid response is returned.
    """
    request = {
        "username": "testuser",
        "password": "secret"
    }
    response = client.post(
        '/api/v1/user/login/',
        data=request
        )
    assert response.status_code == 200


def test_add_post(client, mock_mongo):
    """
    Given a flask application
    When the '/api/v1/post/add/' route is called
    Then check that valid response is returned.
    """
    request = {'post': 'This is a new post.'}
    response = client.post(
        '/api/v1/post/add/',
        data=request
        )
    assert response.status_code == 200


def test_get_posts(client, mock_mongo):
    """
    Given a flask application
    When the '/api/v1/post/posts/' route is called
    Then check that valid response is returned.
    """
    response = client.get('/api/v1/post/posts/testuser')
    assert response.status_code == 200
    assert response.data is not None


def test_like_post(client, mock_mongo):
    """
    Given a flask application
    When the '/api/v1/post/like/' route is called
    Then check that valid response is returned.
    """
    response = client.get('/api/v1/post/posts/testuser')
    decoded_res = response.data.decode("utf-8")
    json_res = json.loads(decoded_res)
    post_id = json_res[0]["id"]

    response = client.post('/api/v1/post/like/'+post_id)
    assert response.status_code == 200


def test_comment_post(client, mock_mongo):
    """
    Given a flask application
    When the '/api/v1/post/comment/' route is called
    Then check that valid response is returned.
    """
    response = client.get('/api/v1/post/posts/testuser')
    decoded_res = response.data.decode("utf-8")
    json_res = json.loads(decoded_res)
    post_id = json_res[0]["id"]

    request = {'comment': 'This is a new post.'}
    response = client.post(
        '/api/v1/post/comment/'+post_id,
        data=request
        )
    assert response.status_code == 200


def test_delete_post(client, mock_mongo):
    """
    Given a flask application
    When the '/api/v1/post/delete/' route is called
    Then check that valid response is returned.
    """
    response = client.get('/api/v1/post/posts/testuser')
    decoded_res = response.data.decode("utf-8")
    json_res = json.loads(decoded_res)
    post_id = json_res[0]["id"]

    response = client.post('/api/v1/post/delete/'+post_id)
    assert response.status_code == 200


def test_user_logout(client, mock_mongo):
    """
    Given a flask application
    When the '/api/v1/user/logout/' route is called
    Then check that valid response is returned.
    """
    response = client.get(
        '/api/v1/user/logout/'
        )
    assert response.status_code == 200
