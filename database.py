import sqlite3
from datetime import datetime

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


# Puxa da base de dados o nome e o objetivo de uma disciplina
def mostra_disciplinas():
    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()

    cursor.execute("SELECT id_disciplina AS id, nome, objetivo FROM disciplina")
    disciplinas = cursor.fetchall()

    connect.close()
    return disciplinas


# Puxa da base de dados o titulo, o status e a disciplina dos conteudos de uma disciplina
def mostra_conteudos(id_disciplina):
    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()

    cursor.execute("SELECT id, nome, concluido FROM todo WHERE categoria = 'CON' AND id_disciplina = ?", (id_disciplina,))
    conteudos = cursor.fetchall()

    connect.close()
    return conteudos


# Puxa da base de dados o titulo, o status e a disciplina das atividades de uma disciplina
def mostra_atividades(id_disciplina):
    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()

    cursor.execute("SELECT id, nome, concluido, prazo, id_disciplina as disciplina FROM todo WHERE categoria = 'ATV' AND disciplina = ?", (id_disciplina,))
    atividades = cursor.fetchall()

    connect.close()
    return atividades


# Puxa o proximo conteudo a fazer de cada disciplina
def proximos_conteudos():
    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()

    cursor.execute("SELECT nome, concluido, id_disciplina AS disciplina FROM todo WHERE categoria = 'CON' AND concluido = 'False' GROUP BY id_disciplina")
    prox_conteudos = cursor.fetchall()

    connect.close()
    return prox_conteudos


# Puxa as atividades com o prazo de entrega para os proximos 7 dias
def proximas_atividades():
    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()

    hoje = datetime.today().strftime('%Y-%m-%d')
    cursor.execute("SELECT nome, prazo, id_disciplina AS disciplina FROM todo WHERE julianday(prazo) - julianday(?) <= 7", (hoje,))
    prox_atividades = cursor.fetchall()

    connect.close()
    return prox_atividades


def atualizaStatus(id, status):
    connect = sqlite3.connect("dashboard.db")
    cursor = connect.cursor()

    cursor.execute("UPDATE todo SET concluido = ? WHERE id = ?", (status, id) )
    
    connect.commit()
    connect.close()
    return

def mostra_eventos():
    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()

    cursor.execute("SELECT id, nome, prazo, id_disciplina AS disciplina, concluido FROM todo WHERE prazo NOT NULL")
    eventos = cursor.fetchall()

    connect.close()
    return eventos