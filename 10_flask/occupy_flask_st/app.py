# Wombats (Eliza Knapp [ducky: Douglas], Noakai Aronesty [ducky: Wombat], Ryan Wang [ducky: TBD])
# SoftDev
# K10 -- Putting Little Pieces Together
# 2021-10-04

from flask import Flask
import csv
import random

app = Flask(__name__) #create instance of class Flask

with open("occupations.csv") as csvfile:
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

job_ret = "<br>".join(job_class) # create a string version of job_class so it can be returned with other html

def occupations(): #edited to return instead of print
        # job_class is what we want to pick weights are the percentages and we only want to pick once (k=1) then we print whatever job class it was
        randomList = random.choices(job_class, weights=percentage, k=1)
        return(randomList[0])

@app.route("/")       #assign fxn to route
def roster():
    print("the __name__ of this module is... ")
    print(__name__)
    return "<h2>Wombats (Eliza Knapp [ducky: Douglas], Noakai Aronesty [ducky: Wombat], Ryan Wang [ducky: TBD])</h2>" \
           + "<b>Chosen Job:</b><br>" + occupations() + "<br><br>"\
           + "<b>Possible Jobs:</b><br>" + job_ret

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change (COOL!) 
    app.run()

# in this case, the app only runs if the file is not imported