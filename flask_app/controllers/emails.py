from flask_app import app
from flask import get_flashed_messages, render_template, redirect, request, session, flash
from flask_app.models.email import Email

@app.route("/")
def index():
    return render_template("index.html", messages=get_flashed_messages())

@app.route("/submit", methods=["POST"])
def create():
    if not Email.validate_email(request.form):
        return redirect ("/")
    data = {
        "email": request.form["email"]
    }
    Email.create_email(data)
    return redirect ("/success")

@app.route("/success")
def display_all():
    emails = Email.display_all()
    return render_template("success.html", emails=emails)