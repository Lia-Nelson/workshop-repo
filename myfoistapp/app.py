from flask import Flask
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?
# In a lot of other languages- particularly python, where a variable
# is set to the output of a function.

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
# It is the separator in paths in the terminal. In this case it means 
# that there is no specific path after the file name past localhost or
# whatever the name of the site is.
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    # This will print to the inspect element console on the website.
    # Only if hello_world is run?
    return "No hablo queso!"  # Q3: Will this appear anywhere? How u know?
    # this will not appear anywhere unless hello_world is run and the output 
    # is set to a value and printed.

app.run()  # Q4: Where have you seen similar construcs in other languages?
# in java when you run methods from specific objects, you call them by
# typing object.method(), just like this. For ex. arraylist.size()
                