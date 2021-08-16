from flask import Flask
from flask import render_template, request, make_response
from werkzeug.utils import redirect


app = Flask(__name__)

auth_token = '3h1e4l1l5o9p2r6i5v3e5t'

def set_token(user, password):
    return '3h1e4l1l5o9p2r6i5v3e5t'

def auth(request):
    global auth_token
    token = request.cookies.get('login_info')
    return (token == auth_token)

@app.route("/")
def apps():
        return render_template("login.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == 'GET':
        return redirect('/')
    else :
        user = request.form.get('userName')
        password = request.form.get('password')
        if (user == 'admin' and password == 'admin'):
            token = set_token(user, password)
            respond = make_response(redirect('/index'))
            respond.set_cookie('login_info', token)
            return respond
        else:
            return redirect('/')

@app.route('/index', methods = ["POST", "GET"])
def index():
    if auth(request):
        return render_template("main.html")
    else:
        return redirect('/')


@app.route("/log_out", methods=["POST","GET"])
def log_out():
    respond = make_response(redirect('/index'))
    respond.set_cookie('login_info', '', expires=0)
    return respond

if __name__ == "__main__":
    app.run(host="localhost", port='5000')
