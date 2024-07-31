from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from .models import db, User

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)



# READ all
@app.route("/")
def index():
    users = User.query.all()
    print("GET ALL", users)
    return [user.to_dict() for user in users]



# READ one
@app.route("/<int:id>")
def get_user(id):
    user = User.query.get(id)
    return_dict = {}
    return_dict["name"] = user.name
    return user.to_dict()




# CREATE new
@app.route("/new")
def create_user():
    # Object takes in kwargs
    new_user = User(name="will")
    print(new_user)
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()




@app.route("/update/<int:id>")
def update_user(id):
    user = User.query.get(id)
    user.name = "new name"
    db.session.commit()
    return user.to_dict()


@app.route("/delete/<int:id>")
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return "Success!"


@app.route("/test")
def testing():
    users = User.query.all()
    print(users)
    return [user.to_dict() for user in users]
