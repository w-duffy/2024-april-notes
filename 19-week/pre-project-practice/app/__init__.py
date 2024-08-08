from flask import Flask, render_template, redirect, jsonify, request
from flask_migrate import Migrate

from app.aws import ImageForm, get_unique_filename, upload_file_to_s3
from .config import Configuration

# from .routes import simple
# from .forms import SimpleForm
from .models import Image, db, Movie, Actor
from .seeds import seed_commands

app = Flask(__name__)


app.cli.add_command(seed_commands)


app.config.from_object(Configuration)
# app.register_blueprint(simple.bp) # don't need this if you decalre your routes here
db.init_app(app)
Migrate(app, db)





@app.route("/api")
def main_page():
    tom = Actor.query.filter(Actor.name == ("Tom")).first()

    if tom is None:
        return {"message": "no actor"}, 400


    return {"actor": tom.to_dict(), "movies": [movie.to_dict() for movie in tom.movies]}

# @app.route("/api/aws", methods=["POST"])
# def aws_handler():
#     print(request.files)

#     return {"hello": "world"}

@app.route("/api/aws", methods=["POST"])
def upload_image():
    print("here")
    print(request.files)
    form = ImageForm()
    print("FORM", form.data)


    print("in validate")
    image = form.data["image"]
    print("image", image)

    image.filename = get_unique_filename(image.filename)
    upload = upload_file_to_s3(image)
    print(upload)

    if "url" not in upload:
    # if the dictionary doesn't have a url key
    # it means that there was an error when you tried to upload
    # so you send back that error message (and you printed it above)
        return {"message": "oopsie"}
    url = upload["url"]
    new_image = Image(image= url)
    db.session.add(new_image)
    db.session.commit()
    return {"image": new_image.to_dict()}, 201


@app.route("/api/error")
def error():
    print("api error out")

    # error =
    return {"message": "you goofed"}, 400




# @app.route("/simple-form-data")
# def simple_form_data():
#     result = SimplePerson.query.filter(SimplePerson.name.like("M%")).all()
#     return render_template("simple_form_data.html", result=result)
