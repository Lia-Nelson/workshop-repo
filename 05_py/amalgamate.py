# Eliza Knapp, Rachel Xiao, Thomas Yu
# SoftDev
# Print A SoftDev Student's Name, Amalgamated Version
# 2021-09-26

import random

def generate_name(pd1_file, pd2_file):
  pd1 = []
  pd2 = []

  try:
    pd1_names = open(pd1_file)
    for line in pd1_names:
      pd1.append(line.strip())
    pd1_names.close()

    try: 
      random.shuffle(pd1)
      print("pd1: " + pd1[0])
      
    except:
      print("Pd1 text file is empty")
  except:
    print("The pd1 file doesn't exist")
  
  try:
    pd2_names = open(pd2_file)
    for line in pd2_names:
      pd2.append(line.strip())
    pd2_names.close()

    try: 
      random.shuffle(pd2)
      print("pd2: " + pd2[0])

    except:
      print("Pd2 text file is empty")
  except:
    print("The pd2 file doesn't exist")

generate_name("pd1.txt", "pd2.txt")