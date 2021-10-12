# Hedgehogs (Andrew Juang, David Chong, Eliza Knapp)
# SoftDev
# K13 -- Template for Success
# 2021-10-08

import csv
import random

def readfile(filepath):
    ''' This function takes in a filepath and returns a dictionary with the items from the file'''
    # declaration of dictionary to hold occupations + percentages
    occupations_dict = {}

    # open/read csv file
    with open(filepath) as csvfile:
        # read the occupations.csv into a reader file, which contains a dict of each line
        reader = csv.DictReader(csvfile)
        # add dictionary items
        for line in reader:
            percent_link = []
            percent_link.append(float(line['Percentage']))
            percent_link.append(line['Link'])
            occupations_dict[line['Job Class']] = percent_link

    # remove unnecessary item
    occupations_dict.pop('Total')

    return occupations_dict


def random_occupation(occupations):
    '''Takes in a dictionary with the occupations and percentages and links and returns a random occupation based on percentage'''
    # choose random occupation given weights
    occupation_list = list(occupations.keys())
    values = occupations.values()
    weights = []
    for value in values:
      weights.append(value[0])

    choice = random.choices(occupation_list, weights)

    return(choice[0])
