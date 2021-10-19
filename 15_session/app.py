# Absent Duo (Annabel Zhang, Eliza Knapp)
# SoftDev
# K15 -- Making a Login Page
# 2021-10-18

# configures flask so that each user gets their own version of the session
from flask import Flask, render_template, request, redirect, session
# creates an instance of session
from flask_session import Session

app = Flask(__name__)    #create Flask object

app.secret_key = "secret key yay"

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    # first check if it is already in session
    if not session.get("wombat"):
        return render_template( 'login.html' )
    else:
        return render_template("response.html", username = "wombat")


@app.route("/auth" , methods=['GET', 'POST'])
# the form has now been submitted, so we must record the username in session
def authenticate():
    username = "wombat"
    password = "cute"
    #runs if request method POST is used
    if request.method == "POST":
        # when it posts some data, record the user info in session data if it is correct
        if request.form["username"] == username and request.form["password"] == password:
            session["wombat"] = "cute"
            return render_template("response.html", username = request.form["username"])
        else:
            # otherwise, display the incorrect stuff
            return render_template("login.html", status = "Wrong username and password combination. Try again.")
    else: 
        #it should not be a GET request
        if request.method == "GET":
            return render_template("login.html", status = "Wrong request method; use POST")

@app.route("/logout")
# ends the session
def logout():
    session["wombat"] = None
    return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    app.run()