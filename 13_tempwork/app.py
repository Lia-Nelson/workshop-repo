# Hedgehogs (Andrew Juang, David Chong, Eliza Knapp)
# SoftDev
# K13 -- Template for Success
# 2021-10-08

from flask import Flask, render_template
import csv
import random

app = Flask(__name__)

with open("./data/occupations.csv") as csvfile:
    # read the occupations.csv into a reader file, which contains a dict of each line
    reader = csv.DictReader(csvfile)

    # these will store the job classes and percentages
    job_class = []
    percentage = []

    # iterates through each line, and fills job_class and percentage with the correct values
    for line in reader:
        job_class.append(line["Job Class"])
        percentage.append(float(line["Percentage"]))

    # removing last item (because it's Total : 99.8)
    job_class.pop(len(job_class) - 1)
    percentage.pop(len(percentage) - 1)
  
def occupations(): #edited to return instead of print
    # job_class is what we want to pick weights are the percentages and we only want to pick once (k=1) then we print whatever job class it was
    randomList = random.choices(job_class, weights=percentage, k=1)
    return(randomList[0])

@app.route("/")
def hello_world():
    return "Hi!"

@app.route("/occupyflaskst")
def test_tmplt():
    return render_template( 'tablified.html', chosenJob=occupations(), jobClass=job_class, percentage=percentage)

if __name__ == "__main__":
    app.debug = True
    app.run()