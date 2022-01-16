import os
from datetime import datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_mail import Mail
from flask_mail import Message
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# all the configs of the mail
# app.config["TESTING"] = os.environ.get("TESTING")
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ["MAIL_USERNAME"],
    "MAIL_PASSWORD": os.environ["MAIL_PASSWORD"]
    }


app.config.update(mail_settings)
mail = Mail(app)
mongo = PyMongo(app)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


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
            flash("Username already exists", 'error')
            return redirect(url_for("register"))

        if existing_email:
            flash("Email is already registered", 'error')
            return redirect(url_for("register"))

        if password != passwordconfirm:
            flash("The passwords should match", 'error')
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
        flash("Registration Successful!", 'success')
        return render_template("home.html")
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
                    request.form.get("username")), 'success')
                return render_template("home.html")

            else:
                # invalid password match
                flash("Incorrect Username and/or Password", 'error')
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password", 'error')
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/stopwatch", methods=["GET", "POST"])
def stopwatch():
    if session.get("user") is not None:
        userTeam = mongo.db.teams.find(
            {"created_by": session["user"]})
        teamResults = mongo.db.results.find(
            {"created_by": session["user"]})
        return render_template("stopwatch.html", userTeam=userTeam, teamResults=teamResults)
    else:
        flash("You need to be logged in to see this content", 'error')
        return render_template("login.html")


@app.route("/stopwatchClock/<team_id>", methods=["GET", "POST"])
def stopwatchClock(team_id):
    if session.get("user") is not None:
        userTeam = mongo.db.teams.find(
            {"created_by": session["user"]})
        date = datetime.now()

        if request.method == "POST":
            result = {
                "created_by": session["user"],
                "overallTime": request.form.get("timer_33"),
                "datum": date.strftime("%d/%m/%y"),
                "teamName": request.form.get("teamName"),
                "fieldTime_1": request.form.get("timer_2"),
                "fieldTime_2": request.form.get("timer_4"),
                "fieldTime_3": request.form.get("timer_6"),
                "fieldTime_4": request.form.get("timer_8"),
                "fieldTime_5": request.form.get("timer_10"),
                "fieldTime_6": request.form.get("timer_12"),
                "fieldTime_7": request.form.get("timer_14"),
                "fieldTime_8": request.form.get("timer_16"),
                "fieldTime_9": request.form.get("timer_18"),
                "fieldTime_10": request.form.get("timer_20"),
                "fieldTime_11": request.form.get("timer_22"),
                "fieldTime_12": request.form.get("timer_24"),
                "fieldTime_13": request.form.get("timer_26"),
                "fieldTime_14": request.form.get("timer_28"),
                "fieldTime_15": request.form.get("timer_30"),
                "fieldTime_16": request.form.get("timer_32"),
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
            }

            mongo.db.results.insert(result)
            flash("The results are stored", 'success')
        team = mongo.db.teams.find_one({"_id": ObjectId(team_id)})
        return render_template(
                                "stopwatchClock.html",
                                userTeam=userTeam,
                                team=team)
    else:
        flash("You need to be logged in to see this content", 'error')
        return render_template("login.html")


@app.route("/team", methods=["GET", "POST"])
def team():
    if session.get("user") is not None:
        if request.method == "POST":
            # gets all the info from the form and creates a team
            newteam = {
                "teamName": request.form.get("teamName"),
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

            # inserts the team
            mongo.db.teams.insert_one(newteam)
            flash("team Successfully Added", 'success')
            return redirect(url_for("team"))

        userTeam = mongo.db.teams.find(
            {"created_by": session["user"]})
        return render_template("team.html", userTeam=userTeam)
    else:
        flash("You need to be logged in to see this content", 'error')
        return render_template("login.html")


@app.route("/editteam/<team_id>", methods=["GET", "POST"])
def editteam(team_id):
    if session.get("user") is not None:
        if request.method == "POST":
            # gets a recipe and takes all info /changes from the form and saves it
            editedteam = {
                "teamName": request.form.get("teamName"),
                "created_by": session["user"],
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
                "player16": request.form.get("player16")

            }
            mongo.db.teams.update({"_id": ObjectId(team_id)}, editedteam)
            flash("Team Successfully edited", 'success')
            return redirect(url_for('team', username=session['user']))

        team = mongo.db.teams.find_one({"_id": ObjectId(team_id)})
        return render_template(
            "editteam.html", team=team)
    else:
        flash("You need to be logged in to see this content", 'error')
        return render_template("login.html")


@app.route("/deleteTeam/<team_id>", methods=["GET", "POST"])
def deleteTeam(team_id):
    if session.get("user") is not None:
        # deletes recipe
        mongo.db.teams.remove({"_id": ObjectId(team_id)})
        flash("team succesfully deleted", 'success')
        return redirect(url_for('team', username=session['user']))
    else:
        flash("You need to be logged in to see this content", 'error')
        return render_template("login.html")


@app.route("/results")
def results():
    if session.get("user") is not None:
        userResults = mongo.db.results.find(
            {"created_by": session["user"]})
        return render_template("results.html", userResults=userResults)
    else:
        flash("You need to be logged in to see this content", 'error')
        return render_template("login.html")


@app.route("/resultsind/<results_id>", methods=["GET", "POST"])
def resultsind(results_id):
    if session.get("user") is not None:
        results = mongo.db.results.find({"_id": ObjectId(results_id)})
        return render_template("resultsind.html", results=results)
    else:
        flash("You need to be logged in to see this content", 'error')
        return render_template("login.html")


@app.route("/deleteResults/<results_id>", methods=["GET", "POST"])
def deleteResults(results_id):
    if session.get("user") is not None:
        # deletes recipe
        mongo.db.results.remove({"_id": ObjectId(results_id)})
        flash("results successfully deleted", 'success')
        return redirect(url_for('results', username=session['user']))
    else:
        flash("You need to be logged in to see this content", 'error')
        return render_template("login.html")


@app.route("/settings")
def settings():
    if session.get("user") is not None:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        user = mongo.db.users.find_one({"username": username})
        return render_template("settings.html", user=user)
    else:
        flash("You need to be logged in to see this content", 'error')
        return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have been logged out", 'success')
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/passwordsettings", methods=["GET", "POST"])
def passwordsettings():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    user = mongo.db.users.find_one({"username": username})

    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # does password match user input
            if existing_user["password"] == request.form.get("oldpassword"):

                newpass = {
                    "username": request.form.get("username").lower(),
                    "password": generate_password_hash(
                                                    request.form.get(
                                                        "passwordconfirm")),
                    "email": request.form.get("email")
                    }

                mongo.db.users.replace_one(user, newpass)
                flash("Password successfully updated", 'success')
                return render_template("settings.html", username=username)

    return render_template(
        "passwordsettings.html", user=user)


@app.route("/pass_reset_request")
def pass_reset_request():

    return render_template(
        "pass_reset_request.html")


@app.route("/recoverymail", methods=["GET", "POST"])
def recoverymail():

    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        print(existing_user)
        if existing_user:

            msg = Message()
            msg.subject = "reset pass"
            msg.sender = 'infobenchtimer@gmail.com'
            msg.recipients = ['pjdijxhoorn@hotmail.com']
            msg.html = "<h2>We are sorry to hear you lost your password </h2>"

            print(msg)
            mail.send(msg)

            flash("An email with a link has been send", 'success')
            return render_template("login.html")

        else:
            flash("the mail/ username isnt correct", 'error')
            return render_template("passwordrecovery.html")
    return render_template("passwordrecovery.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
