# Polymer Erasers
# SoftDev
# 2022-10-06

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True # debug mode: on
app.run()

# What is debug mode?

# What we saw in the shell:
#  * Restarting with stat
# /usr/bin/python3: No module named thonny.plugins.cpython.app

# It worked in the terminal but didn't work in the thonny shell
# We saw debugger is active in the terminal and the PIN: 760-007-819
# No visual difference in the website