# Hedgehogs (Andrew Juang, David Chong, Eliza Knapp)
# SoftDev
# K13 -- Template for Success
# 2021-10-08

from flask import Flask, render_template, redirect
import functions

app = Flask(__name__)

@app.route("/")
def hello_world():
    return redirect("/occupyflaskst")

@app.route("/occupyflaskst")
def test_tmplt():
    # read in csv file to "occupations" dictionary
    occupations = functions.readfile("./data/occupations.csv")
    # choose random occupation
    chosen_occupation = functions.random_occupation(occupations)

    return render_template('tablified.html', chosenJob=chosen_occupation, jobClass=occupations)


if __name__ == "__main__":
    app.debug = True
    app.run()