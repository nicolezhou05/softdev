# TNPG: Circle (Thomas Zhang, Bob, Nicole Zhou, Duck)
# SoftDev
# K07 -- Flask
# 2022-10-03
# time spent: 0.4 hr

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
0. You have to install Flask first.
1. After running it, it will say warning and give this link: http://127.0.0.1:5000/

QCC:
0. It is similar to Java.
1. Going through different paths and files.
2. (Not too sure)
3. (Not too sure)
4. Maybe not appear?
5. Looks a bit like Java
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
