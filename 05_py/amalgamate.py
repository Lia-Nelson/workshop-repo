# Eliza Knapp, Rachel Xiao, Thomas Yu
# SoftDev
# Print A SoftDev Student's Name, Amalgamated Version
# 2021-09-26

'''
Summary: 
After looking at all three of our files, we decided that it would be easiest
to read the names off of two separate text files, one for period 1 and the 
other for period 2. Our generate_name function takes in each of those files
and tries to open it (try, except courtesy of Thomas' group). It adds the 
contents to a list and then shuffles it and prints the first index. If opening 
the files or looking at their content is not possible, it prints the according
error message.

Discoveries:
- we learned how to use try: except: in python (because none of us took year 
long introCS)

Questions:
- we discussed whether to print the outputs inside the function or whether to
return them and then print them outside of the function.
- how might we change the code to make it run for infinite periods of students?

Comments:
- although it is faster to generate a random integer and take that index of the 
array instead of shuffling, we ended up going with random.shuffle(array) because
it looks prettier in the code and the lists aren't too long.

'''

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