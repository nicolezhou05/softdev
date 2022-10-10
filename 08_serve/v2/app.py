# Polymer Erasers
# SoftDev
# K08 -- Putting it Together -- flask, debug, new line
# 2022-10-06
# time spent: 0.8hrs

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...") # will print this in the shell
    print(__name__)   #where will this go? A: We think it will print in the shell
    return "No hablo queso!"

app.run()

# the print statements ran after we clicked the website