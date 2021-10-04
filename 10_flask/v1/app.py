# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!" # no print(__name__)

app.run()

# not printing the name into the terminal doesn't change the actual website but __main__ is no longer printed in the terminal
# not a necessary step