# JANitors: Aden Garbutt, Jing Yi Feng, Nicole Zhou
# SoftDev
# K18 -- (Python+SQLite)3: A Mare Widge Made in Hebben
# 2022-10-25
# time spent: 0.5 hrs

'''
DISCO:
0) To access the database we created in the python file, we enter .open <.db file> inside the sqlite3 shell
1) In your python file, if you created a table and ran that python script, the second time you ran the script, it will say that this specific table already exists. (Possibly have something to do with the information already being stored in the db file)
2) We couldn't add any text to the database because in other for the shell to recognize it as text, we need quotation marks around the text.

QCC:
0) Instead of deleting the db file, is there some other action we can take so that when we run the python script, it won't say that the db file already exists?
1) Why is the default db file called discobandit.db?
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

command = 'create table courses (code text, mark int, id int);'
c.execute(command)

with open('courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        str = row['code'] + "'," + row['mark'] + "," + row['id']
        command = "insert into courses values('" + str + ");"
        c.execute(command)


command = 'create table students (code text, mark int, id int);'
c.execute(command)

with open('students.csv', newline='') as csvfile1:
    reader1 = csv.DictReader(csvfile1)
    for row in reader1:
        str = row['name'] + "'," + row['age'] + "," + row['id']
        command = "insert into students values('" + str + ");"
        c.execute(command)
        

#command = ""          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database