import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    users = mongo.db.users.find()
    return render_template("home.html", users=users)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # check if email already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        password = request.form.get("password")
        passwordconfirm = request.form.get("passwordconfirm")
        # check for existing users / mail and password confirm
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        if existing_email:
            flash("Email is already registered")
            return redirect(url_for("register"))

        if password != passwordconfirm:
            flash("The passwords should match")
            return redirect(url_for("register"))

        # build a new user
        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get(
                "passwordconfirm")),
            "email": request.form.get("email")
        }
        mongo.db.users.insert_one(new_user)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # does password match user input
            if check_password_hash(
                                existing_user["password"],
                                request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/stopwatch")
def stopwatch():
    return render_template("stopwatch.html")


@app.route("/team")
def team():
    if request.method == "POST":
        # gets all the info from the form and creates a team
        newteam = {
            "teamName": request.form.get("player1"),
            "player1": request.form.get("player1"),
            "player2": request.form.get("player2"),
            "player3": request.form.get("player3"),
            "player4": request.form.get("player4"),
            "player5": request.form.get("player5"),
            "player6": request.form.get("player6"),
            "player7": request.form.get("player7"),
            "player8": request.form.get("player8"),
            "player9": request.form.get("player9"),
            "player10": request.form.get("player10"),
            "player11": request.form.get("player11"),
            "player12": request.form.get("player12"),
            "player13": request.form.get("player13"),
            "player14": request.form.get("player14"),
            "player15": request.form.get("player15"),
            "player16": request.form.get("player16"),
            "created_by": session["user"]
        }

        # inserts the recipe
        mongo.db.teams.insert_one(newteam)
        flash("team Successfully Added")
        return redirect(url_for("team"))

    return render_template("team.html")


@app.route("/results")
def results():
    return render_template("results.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
