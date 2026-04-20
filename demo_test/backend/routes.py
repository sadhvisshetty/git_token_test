from flask import Blueprint, render_template, request, redirect, url_for

routes = Blueprint('routes', __name__)

USER = {
    "email": "admin@test.com",
    "password": "1234"
}


def _validate_credentials(email, password):
    return email == USER["email"] and password == USER["password"]


@routes.route("/")
def home():
    return render_template("login.html")


@routes.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if _validate_credentials(email, password):
        return redirect(url_for("routes.dashboard"))
    else:
        return "Invalid Credentials"


@routes.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")