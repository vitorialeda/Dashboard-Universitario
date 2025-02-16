from flask import Flask, render_template, request # type: ignore
import sqlite3

app = Flask(__name__)
app.run(debug=True)

con = sqlite3.connect("dashboard.db")
cur = con.cursor()


@app.route("/")
def hello_world():
    return "<p>Helloooo</p>"


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")