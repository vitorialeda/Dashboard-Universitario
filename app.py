from flask import Flask, jsonify, render_template, request, redirect # type: ignore
import database

app = Flask(__name__)


@app.route("/")
def dashboard():
    prox_conteudos = database.proximos_conteudos()
    prox_atividades = database.proximas_atividades()
    disciplinas = database.mostra_disciplinas()
    progresso = database.progresso()

    for i in range(len(disciplinas)):
        disciplinas[i]["ementa"] = database.mostra_conteudos(disciplinas[i]["id"])
        disciplinas[i]["atividades"] = database.mostra_atividades(disciplinas[i]["id"])
 

    return render_template("index.html", disciplinas= disciplinas, prox_conteudos=prox_conteudos, prox_atividades=prox_atividades, progresso = progresso)


@app.route("/atualizaStatus", methods=['POST'])
def atualizaStatus():
    data = request.json
    id = data["id"]
    status = str(data["status"])

    database.atualizaStatus(id, status)

    return redirect("/")

@app.route("/eventos")
def eventos():
    eventos = database.mostra_eventos()
    return jsonify(eventos)