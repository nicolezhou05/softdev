# Polymer Erasers
# SoftDev
# 2022-10-06

from flask import Flask
app = Flask(__name__) # We think that it will be __main__

@app.route("/") # The website created will show what is in this file. We also think that the app created will live in the root directory.
def hello_world():
    print(__name__) # It will print __main__
    return "No hablo queso!"  # What the website will print

app.run()  # running the script, without it the website will not show
                
