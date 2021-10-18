# Absent Duo (Annabel Zhang, Eliza Knapp)
# SoftDev
# K15 -- Making a Login Page
# 2021-10-18

from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' )


@app.route("/auth" , methods=['GET', 'POST'])
def authenticate():
    #users should not be using GET
    if request.method == "GET":
        return render_template("login.html", status = "Wrong request method; use POST")
    #runs if request method POST is used
    else:
        #checks against hardcoded username/pw of cookie/jam
        if request.form["username"] == "cookie" and request.form["password"] == "jam":
            return render_template("response.html", username = request.form["username"])
        #if wrong username/pw is inputted
        else:
            return render_template("login.html", status = "Wrong username and password combination. Try again.")

if __name__ == "__main__":
    app.debug = True
    app.run()