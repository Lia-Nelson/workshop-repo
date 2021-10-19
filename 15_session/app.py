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
# ^^ note he said that later we use urandom(32)

# hardcoded username and password
username = "wombat"
password = "cute"

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    # first check if it is already in session
    if not session.get(username):
        return render_template( 'login.html' )
    else:
        return render_template("response.html", username = username)


@app.route("/auth" , methods=['GET', 'POST'])
# the form has now been submitted, so we must record the username in session
def authenticate():
    #runs if request method POST is used
    if request.method == "POST":
        # when it posts some data, record the user info in session data if it is correct
        if request.form["username"] == username and request.form["password"] == password:
            session[username] = password
            # below prints the password in the console just to check
            # print(session.get("wombat")) 
            return render_template("response.html", username = request.form["username"])
        else:
            if not request.form["username"] == username:
                # if the username is wrong, there should be no further information on the accuracy of the password
                return render_template("login.html", status = "Wrong username. Try again.")
            if request.form["username"] == username and not request.form["password"] == password:
                return render_template("login.html", status = "Wrong password. Try again.")
            # otherwise, display the incorrect stuff
    elif request.method == "GET":
        #it should not be a GET request
        return render_template("login.html", status = "Wrong request method; use POST")
    else:
        #if nothing predictable is wrong, just say there is an error
        return render_template("login.html", status = "Error!")

@app.route("/logout")
# ends the session
def logout():
    if username in session:
        # print(session.items())
        session.pop(username)
        # print(session.items())
        # the above print statement was meant to check if it was actually popped off
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run()