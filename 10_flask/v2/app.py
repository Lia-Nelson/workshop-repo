# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go? # this will go to the terminal
    return "No hablo queso!"

app.run()

# this will print an extra line above __main__ that tells you it's about to print

# print seems to be like Systems.out.println() not print()