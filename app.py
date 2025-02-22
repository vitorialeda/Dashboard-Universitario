from flask import Flask, render_template, request # type: ignore
import database

app = Flask(__name__)
app.run(debug=True)




@app.route("/")
def dashboard():
    disciplinas = database.mostra_disciplinas()
    conteudos = database.mostra_conteudos()
    return render_template("dashboard.html", disciplinas = disciplinas, conteudos = conteudos, tamanho = len(disciplinas))
