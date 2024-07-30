from flask import Flask, render_template, redirect, url_for
from app.config import Config
from .posts import posts, users

app = Flask(__name__)

app.config.from_object(Config)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts")
def all_posts():
    return render_template("posts.html", posts=posts, page_type="posts")


@app.route("/users/<int:id>/posts")
def get_single_users_posts(id):
    user = users[id - 1]
    user_posts = [post for post in posts if post["author"] == user["name"]]
    return render_template("posts.html", posts=user_posts, page_type="user")


@app.route("/posts/<int:id>/delete", methods=["GET"])
def delete_post(id):
    post_to_delete = [post for post in posts if post["id"] == id][0]
    posts.remove(post_to_delete)
    return redirect(url_for("all_posts"))


@app.route("/posts/<int:id>")
def get_single_post(id):
    post = [post for post in posts if post["id"] == id]
    return render_template("posts.html", posts=post, post_type="post")
