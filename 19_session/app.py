from flask import Flask, render_template, request, session


app = Flask(__name__)    #create Flask object

app.secret_key = 'JANitors_@1'



@app.route("/", methods=['GET', 'POST'])
def login_page():
    return render_template('login.html')


@app.route("/login", methods=['GET', 'POST'])
def response_page():
    session['username'] = request.form.get('username')
    if 'username' in session:
        print(request.cookies.get('JANitors_@1'))
        return render_template('response.html', user=request.form.get('username'))
    return 'You are not logged in'

# def disp_loginpage():
#     print("\n\n\n")
#     print("***DIAG: this Flask obj ***")
#     print(app)
#     print("***DIAG: request obj ***")
#     print(request)
#     print("***DIAG: request.args ***")
#     print(request.args)
#     #print("***DIAG: request.args['username']  ***")
#     #print(request.args['username'])
#     print("***DIAG: request.headers ***")
#     print(request.headers)
#     return render_template( 'login.html' )
# 
# 
# @app.route("/auth", methods=['GET', 'POST'])
# def authenticate():
#     print("\n\n\n")
#     print("***DIAG: this Flask obj ***")
#     print(app)
#     print("***DIAG: request obj ***")
#     print(request)
#     print("***DIAG: request.args ***")
#     print(request.args)
#     #print("***DIAG: request.args['username']  ***")
#     #print(request.args['username'])
#     print("***DIAG: request.headers ***")
#     print(request.headers)
#     return render_template('response.html', user=request.args.get('username'), request_method=request.method)  #response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()