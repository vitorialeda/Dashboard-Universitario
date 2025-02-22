from flask import Flask, render_template, request # type: ignore
import database

app = Flask(__name__)


@app.route("/")
def dashboard():
    disciplinas = database.mostra_disciplinas()
    conteudos = database.mostra_conteudos()
    atividades = database.mostra_atividades()
    proximos_conteudos = database.proximos_conteudos()
    proximas_atividades = database.proximas_atividades()
    
    return render_template("dashboard.html", disciplinas = disciplinas, conteudos = conteudos, tamanho = len(disciplinas), atividades = atividades, proximos_conteudos=proximos_conteudos, proximas_atividades=proximas_atividades)
