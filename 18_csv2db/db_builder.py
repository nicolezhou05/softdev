# JANitors: Aden Garbutt, Jing Yi Feng, Nicole Zhou
# SoftDev
# K18 -- (Python+SQLite)3: A Mare Widge Made in Hebben
# 2022-10-25
# time spent: 0.5 hrs (so far)

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

# command = 'create table courses (code text, mark int, id int);'
# c.execute(command)

with open('courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        str = row['code'] + "'," + row['mark'] + "," + row['id']
        command = "insert into courses values('" + str + ");"
        c.execute(command)
       #print(row['code'], row['id'])
        
c.execute("select * from courses;")

# csvfile = open('courses.csv', 'r')
# reader = csv.DictReader(csvfile)
# for row in reader:
#     #command = 'insert'
#     command = 'insert into courses values(' + row['code'], row['mark'], row['id'] + ');'
#     #c.execute(command)
#     print(command)

#command = ""          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database