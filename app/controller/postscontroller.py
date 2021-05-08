from app.smapp import app
from app.mapper.postsmapper import PostsMapper
from app.containers import PostsMapperContainer

from flask import request, Response

from flask_login import current_user, login_required

import json


@app.route("/api/v1/post/add-post/", methods=["POST"])
@login_required
def add_post():
    result = add_post(request.form["post"])
    res = json.dumps({'message': result})
    return Response(res, mimetype='application/json')

def add_post(post_content):
    post = dict()
    post["post_content"] = post_content
    post["likes"] = 0
    post["comments"] = []
    post["user"] = current_user.get_id()

    posts_mapper = PostsMapperContainer.posts_mapper()
    posts_mapper.add_post(post)

    return ("Post added successfully.")

@app.route("/api/v1/post/get-posts/<username>")
@login_required
def get_posts(username):
    result = get_post(username)
    return Response(json.dumps(result), mimetype="text/json")

def get_post(username):
    posts_mapper = PostsMapperContainer.posts_mapper()
    return posts_mapper.get_posts(username)

@app.route("/api/v1/post/like-post/<post_id>", methods=["POST"])
@login_required
def like_post(post_id):
    result = like_post(post_id)
    res = json.dumps({'message': result})
    return Response(res, mimetype='application/json')

def like_post(post_id):
    posts_mapper = PostsMapperContainer.posts_mapper()
    posts_mapper.like_post(post_id)
    return "Post liked."

@app.route("/api/v1/post/comment/<post_id>", methods=["POST"])
@login_required
def comment_post(post_id):
    result = comment_post(post_id, request.form["comment"])
    res = json.dumps({'message': result})
    return Response(res, mimetype='application/json')

def comment_post(post_id, comment):
    posts_mapper = PostsMapperContainer.posts_mapper()
    posts_mapper.comment_post(post_id, comment)
    return "Comment added to the post."
