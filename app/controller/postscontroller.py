"""Posts Controller Module."""

import json

from flask import Response, request
from flask_login import current_user, login_required

from app.containers import PostsMapperContainer
from app.smapp import app


@app.route("/api/v1/post/add/", methods=["POST"])
@login_required
def add():
    """Add post endpoint."""
    result = add_post(request.form["post"])
    res = json.dumps({'message': result})
    return Response(res, mimetype='application/json')


def add_post(post_content):
    """Add a post to the database."""
    post = dict()
    post["post_content"] = post_content
    post["likes"] = 0
    post["comments"] = []
    post["user"] = current_user.get_id()

    posts_mapper = PostsMapperContainer.posts_mapper()
    posts_mapper.add_post(post)

    return ("Post added successfully.")


@app.route("/api/v1/post/posts/<username>")
@login_required
def posts(username):
    """Get posts endpoint."""
    result = get_posts(username)
    return Response(json.dumps(result), mimetype="text/json")


def get_posts(username):
    """Get all the post for a particular user."""
    posts_mapper = PostsMapperContainer.posts_mapper()
    return posts_mapper.get_posts(username)


@app.route("/api/v1/post/like/<post_id>", methods=["POST"])
@login_required
def like(post_id):
    """Like post endpoint."""
    result = like_post(post_id)
    res = json.dumps({'message': result})
    return Response(res, mimetype='application/json')


def like_post(post_id):
    """Add a like to a post in database."""
    posts_mapper = PostsMapperContainer.posts_mapper()
    posts_mapper.like_post(post_id)
    return "Post liked."


@app.route("/api/v1/post/comment/<post_id>", methods=["POST"])
@login_required
def comment(post_id):
    """Comment post endpoint."""
    result = comment_post(post_id, request.form["comment"])
    res = json.dumps({'message': result})
    return Response(res, mimetype='application/json')


def comment_post(post_id, comment):
    """Add a comment to a post in database."""
    posts_mapper = PostsMapperContainer.posts_mapper()
    posts_mapper.comment_post(post_id, comment)
    return "Comment added to the post."
