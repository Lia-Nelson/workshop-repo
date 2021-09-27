# Eliza Knapp, Rachel Xiao, Thomas Yu
# SoftDev
# Print A SoftDev Student's Name, Amalgamated Version
# 2021-09-26

'''
Summary: 

FIRST ATTEMPT
After looking at all three of our files, we decided that it would be easiest
to read the names off of two separate text files, one for period 1 and the 
other for period 2. Our generate_name function takes in each of those files
and tries to open it (try, except courtesy of Thomas' group). It adds the 
contents to a list and then shuffles it and prints the first index. If opening 
the files or looking at their content is not possible, it prints the according
error message.

GIVEN NEW DIRECTIONS
We have a dictionary with a list for each period. Based on the length of the 
lists, we choose a random index and print the corresponding name in the list.

Discoveries:
- we learned how to use try: except: in python (because none of us took year 
long introCS)
- we learned what a dictionary was and how to access keys and its items.

Questions:
- we discussed whether to print the outputs inside the function or whether to
return them and then print them outside of the function.
- how might we change the code to make it run for infinite periods of students?

Comments:
- although it is faster to generate a random integer and take that index of the 
array instead of shuffling, we ended up going with random.shuffle(array) because
it looks prettier in the code and the lists aren't too long.
- UPDATE: we are now generating a random integer

'''

import random

def generate_name():
  NAMES = {
    "pd1": ["Emma Buller", "Julia Nelson", "Owen Yaggy", "Haotian Gao", "Reng Zheng", "Kevin Cao", "Michelle Lo", "Ivan Lam",
    "Christopher Liu", "Lucas Lee"],
    "pd2": ["Jesse Xie", "Rachel Xiao", "Yuqing Wu", "Liesel Wong", "Josephine Lee",
    "Yaying Liang", "Justin Zou", "Patrick Ging", "Raymont Yueng", "Michael Borczuk",
    "Eliza Knapp", "Thomas Yu", "Jonathan Wu", "Andy Lin", "Andrew Juang", "Annabel Zhang",
    "David Chong"]
  }

  # here we pick a random index based on the size of the lists
  index1 = random.randint(0, len(NAMES["pd1"])-1)
  index2 = random.randint(0, len(NAMES["pd2"])-1)

  # print the names and period clarification
  print("pd1: " + (NAMES["pd1"])[index1])
  print("pd2: " + (NAMES["pd2"])[index2])


generate_name()