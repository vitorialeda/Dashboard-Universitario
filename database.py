import sqlite3

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

# Puxa da base de dados o nome e o objetivo de todas as disciplinas
def mostra_disciplinas():
    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()

    cursor.execute("SELECT nome, objetivo FROM disciplina")
    disciplinas = cursor.fetchall()

    connect.close()
    return disciplinas

# Puxa da base de dados o titulo dos conteudos de uma disciplina especifica
def mostra_conteudos():
    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()

    cursor.execute("SELECT disciplina_id_disciplina, titulo FROM conteudo ORDER BY disciplina_id_disciplina")
    conteudos = cursor.fetchall()

    connect.close()
    return conteudos