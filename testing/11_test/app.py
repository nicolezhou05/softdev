# Notes and tests on 11_flask-forms
# Oct 2022

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not.
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    # returns <Flask 'app'>

    print("***DIAG: request obj ***")
    print(request)
    # returns <Request 'http://127.0.0.1:5000/' [GET]>

    print("***DIAG: request.args ***")
    print(request.args)
    # returns ImmutableMultiDict([])

    # these two lines of code were commented out
    # print("***DIAG: request.args['username']  ***")
    # print(request.args['username'])
    # Get a bunch of errors: BAdRequestKeyError

    print("***DIAG: request.headers ***")
    print(request.headers)
    ''' returns
    Host: 127.0.0.1:5000
    Connection: keep-alive
    Cache-Control: max-age=0
    Sec-Ch-Ua: "Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"
    Sec-Ch-Ua-Mobile: ?0
    Sec-Ch-Ua-Platform: "Windows"
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Sec-Fetch-Site: none
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Accept-Encoding: gzip, deflate, br
    Accept-Language: en-US,en;q=0.9
    '''

    return render_template( 'login.html' ) # displays the contents of login.html on web server

# After submitting the form, we get directed to this route because login.html contains
# <form action="/auth">
#   <input type="text" name="username">
#   <input type="submit" name="sub1">
# </form>
@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    # returns <Flask 'app'>

    print("***DIAG: request obj ***")
    print(request)
    # returns <Request 'http://127.0.0.1:5000/auth?username=something&sub1=Submit' [GET]>

    print("***DIAG: request.args ***")
    print(request.args)
    # returns ImmutableMultiDict([('username', 'something'), ('sub1', 'Submit')])

    # these two lines of code were commented out
    print("***DIAG: request.args['username']  ***")
    print(request.args['username'])
    # returns [whatever that was typed in the form]

    print("***DIAG: request.headers ***")
    print(request.headers)
    ''' returns
    Host: 127.0.0.1:5000
    Connection: keep-alive
    Sec-Ch-Ua: "Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"
    Sec-Ch-Ua-Mobile: ?0
    Sec-Ch-Ua-Platform: "Windows"
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Referer: http://127.0.0.1:5000/
    Accept-Encoding: gzip, deflate, br
    Accept-Language: en-US,en;q=0.9
    '''

    return "Waaaa hooo HAAAH"  # response to a form submission
# AFter getting directed to this route, the URl link was: http://127.0.0.1:5000/auth?username=something&sub1=Submit
# 'something' was what was typed into the form


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()