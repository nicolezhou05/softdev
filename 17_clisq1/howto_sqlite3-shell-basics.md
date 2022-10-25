# JANitors: Aden Garbutt, Jing Yi Feng, Nicole Zhou
# SoftDev
# K17 -- Shell Game
# 2022-10-24
# time spent: 0.5 hrs

### Prerequisites:
- Have sqlite3 opened in the terminal by typing ```sqlite3```, or if you are a windows user, you can type ```sqlite3.exe```

### How To Create a Table and View Contents
1. type ```create table <table name>(<column name> <data type, <column name> <data type>);```
    - column names should not be an int
2. Insert values into table: ```insert into <table name> values(<data from each column of the row separated by commas>);```
3. Accessing data from the table:
    - ```select * from <table name>``` access the entire table, returning each row
    - ```select <column name> from <table name>``` access the column we want to look at

### Useful Dot-Commands
* ```.help``` returns a other dot commands and descriptions
* ```.quit``` exists sqlite3 Shell
* ```.databases``` lists name of attached databases
* ```.import FILE TABLE``` imports data from file into table
* ```.recover``` recovers as much info as possible from corrupt databases
* ```.mode``` to change output formats or just ```.mode``` to get the current mode

### Helpful Link: https://www.sqlite.org/cli.html