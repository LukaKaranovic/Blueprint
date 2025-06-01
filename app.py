from backend import *
from frontend.forms import *
from flask import Flask, render_template, request

app = Flask(__name__)

app.config["SECRET_KEY"] = "secretkeyoooooo"




@app.route('/', methods=["GET", "POST"])
def index():
    loginForm = LoginForm()
    return render_template("index.html", loginForm = loginForm)


@app.route('/register', methods=["GET", "POST"])
def register():
    registerForm = RegistrationForm()

    if registerForm.validate_on_submit():
        username = registerForm.username.data
        password = registerForm.password.data
        userType = registerForm.userType.data


    return render_template("register.html", registerForm = registerForm)
