# Polymer Erasers
# SoftDev
# K08 -- Putting it Together -- flask, debug, new line
# 2022-10-06
# time spent: 0.8hrs

'''
DISCO:
 - It appears like only one function is run in the entire app and when you call other functions, their return values don't show up on the screen
 - To create line breaks, we need to use "<br>", in quotations. It does not literally print out <br> which we thought it would
 - app.debug was extremely helpful so that we would not need to start and stop our app every time we made an edit

QCC:
 - Is there a more efficient way to put information on the page rather than using string concatenation?
 - What is flask?
 - How can we incorporate other apps with different names? This one is named __main__ by default. Can we name other apps different names and interweave them?
 - How can we incorporate different functions?
'''

import csv
import random

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def random_occupation():
    heading = """
    Polymer Erasers: Nicole Zhou, Samantha Hua, and Russell Goychayev
    """

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
        occupations.pop("Total")

    # to get all of the occupations
    list_of_occs = "<br>"
    for occupation in occupations:
        list_of_occs += occupation + "<br>"

    return heading + "<br>" + "<br>" + "List of occupations: " + list_of_occs + "<br>" + "Random occupation: "+ str(random.choices(list(occupations.keys()), weights = occupations.values())[0])

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()