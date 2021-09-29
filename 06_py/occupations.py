# Nice Mice: Ryan Wang, Noakai Aronesty, Eliza Knapp 
# SoftDev
# K06 -- StI/O: Divine your Destiny!
# 2021-09-28

import csv
import random

# preps the file opening, reading and closing
def occupations():
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

        # job_class is what we want to pick
        # weights are the percentages
        # and we only want to pick once (k=1)
        # then we print whatever job class it was
        randomList = random.choices(job_class, weights=percentage, k=1)
        print(randomList[0])

occupations()