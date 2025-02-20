from flask import Flask, render_template, request # type: ignore
import sqlite3

app = Flask(__name__)
app.run(debug=True)

con = sqlite3.connect("dashboard.db", check_same_thread=False)
def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}
con.row_factory = dict_factory
cur = con.cursor()


@app.route("/")
def dashboard():
    # resposta = cur.execute('SELECT * FROM disciplina')
    # disciplina = resposta.fetchone()
    # print(disciplina[0])
    cur.execute("SELECT * FROM disciplina")
    disciplina = cur.fetchall()
    print(disciplina)
    return render_template("dashboard.html", disciplina = disciplina)
