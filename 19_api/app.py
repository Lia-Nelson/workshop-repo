# Yea! -- Andrew Juang, Eliza Knapp, Yuqing Wu
# SoftDev
# K19 -- A RESTful Journey Skyward
# 2021-11-23

from flask import Flask, render_template
import requests, urllib, json

app = Flask(__name__)

f = open("key_nasa.txt")
API_KEY = f.read().strip()

@app.route("/")
def main():
    # Using urllib library
    r = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + API_KEY)

    JSON = r.read()

    URL = json.loads(JSON)['url']
    explanation = json.loads(JSON)['explanation']

    # Using requests library
    # print("API_KEY: " + API_KEY + "\n")
    # r = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + API_KEY)
    #
    # print("JSON:")
    # print(r.json())
    #
    # URL = r.json()['url']
    # print("\nURL: " + URL)

    return render_template('main.html',pic=URL, explanation=explanation)


if __name__ == "__main__":
    app.debug = True
    app.run()
