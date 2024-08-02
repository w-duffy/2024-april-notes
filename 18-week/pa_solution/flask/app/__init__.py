
from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from .config import Configuration
from .routes import simple
from .models import db
# from .forms import SimpleForm # uncomment if you declare routes here

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(simple.bp) # don't need this if you decalre your routes here
db.init_app(app)
Migrate(app, db)


# Don't need a blueprint if you put everything in the same file 🧠
# That said, on the projectin Mod 6, we will have a blueprint for each route

# @app.route("/")
# def main_page():
#     return render_template("main_page.html")


# @app.route("/simple-form")
# def simple_form():
#     form = SimpleForm()
#     return render_template("simple_form.html", form=form)


# @app.route("/simple-form", methods=["POST"])
# def simple_data():
#     form = SimpleForm()
#     if form.validate_on_submit():
#         data = SimplePerson()
#         form.populate_obj(data)
#         db.session.add(data)
#         db.session.commit()
#         return redirect("/")
#     print(form.errors)
#     return "Bad Data"


# @app.route("/simple-form-data")
# def simple_form_data():
#     result = SimplePerson.query.filter(SimplePerson.name.like("M%")).all()
#     return render_template("simple_form_data.html", result=result)
