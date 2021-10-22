# Absent Duo (Annabel Zhang, Eliza Knapp)
# SoftDev
# K16 -- All About Database
# 2021-10-18

# a Python script for interacting with an SQLite db:
import sqlite3 #enable SQLite operations
from csv import DictReader

# open db if exists, otherwise create
# separate file; made connection
db = sqlite3.connect("foo")

c = db.cursor() #facilitate db ops

students = {}
with open('students.csv') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
      # print(row)
      students[row['name']] = [int(row['age']), row['id']]

courses = {}
with open('courses.csv') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
        courses[row['code']] = [int(row['mark']), row['id']]

# create a table with the name student with columns name, age, and id
# TEXT/INTEGER - data type
# the table info is put into foo
c.execute("CREATE TABLE student(name TEXT, age INTEGER, id INTEGER)")
c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)")

# iterates through students dictionary
# item[0] being keys
# item[1][0] and item[1][1] being both values
for item in students.items():
    # print(item)
    c.execute("INSERT INTO student VALUES (?, ?, ?)", (item[0], item[1][0], item[1][1]))

for item in courses.items():
    # print(item)
    c.execute("INSERT INTO courses VALUES (?, ?, ?)", (item[0], item[1][0], item[1][1]))


# c.execute("SELECT * FROM student")

db.commit() # save changes

db.close()