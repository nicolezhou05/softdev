# Polymer Erasers
# SoftDev
# 2022-10-06

'''
DISCO:
0) 
'''

import csv
import random


heading = "abc "
from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def random_occupation():
    # declare an empty dictionary
    occupations = {}

    # read csv file
    with open("occupations.csv", "r") as f:
        f_read = csv.reader(f)
        # to skip the header of the csv file
        next(f_read)

        for line in f_read:
          # made the value associated with each key a float so that it can be used in weights
          occupations[line[0]] = float(line[1])
        total = occupations["Total"]

        for key in occupations.keys():
            # divide by total to get a percentage
            occupations[key] = occupations[key]/total
        #print(occupations)
        occupations["Total"] = 0
        return heading + str(random.choices(list(occupations.keys()), weights = occupations.values()))
    

#print(random_occupation("occupations.csv"))

# if __name__ == "__main__":  # true if this file NOT imported
#     app.debug = True        # enable auto-reload upon code change
#     app.run()
app.run()
    
# Our prediction is that after we change the code, save, then reload, the website will reflect the changes