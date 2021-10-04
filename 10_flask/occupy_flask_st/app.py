# Wombats (Eliza Knapp [ducky: Douglas], Noakai Aronesty [ducky: Wombat], Ryan Wang [ducky: TBD])
# SoftDev


from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def roster():
  return "ROSTER"

def hello_world():
    print("the __name__ of this module is... ") # here, the print above is clearer
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change (COOL!) 
    app.run()

# in this case, the app only runs if the file is not imported