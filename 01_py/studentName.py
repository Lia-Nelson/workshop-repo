# Knapp Eliza
# SoftDev
# Print A SoftDev Student's Name
# 2021-09-21

import random

def generateName(filename):
  names = []
  file = open(filename)
  for line in file:
    names.append(line.strip())
  # print(names)
  file.close()

  random.shuffle(names)
  return names[0]

print(generateName("names.txt"))