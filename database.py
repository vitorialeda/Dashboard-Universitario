import sqlite3
from datetime import datetime

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


def mostra_disciplinas():
    # Contecta à base de dados
    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()

    # Puxa da base de dados o nome e o objetivo de uma disciplina
    cursor.execute("SELECT id_disciplina AS id, nome, objetivo FROM disciplina")
    
    # Guarda resultado da Query na variavel
    disciplinas = cursor.fetchall()

    # Fecha conexão com o banco de dados 
    connect.close()
    return disciplinas


def mostra_conteudos(id_disciplina):
    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()

    # Puxa da base de dados o titulo, o status e a disciplina dos conteudos de uma disciplina
    cursor.execute(
        '''
        SELECT id, nome, concluido FROM todo 
        WHERE categoria = 'CON' AND id_disciplina = ?
        ''', (id_disciplina,))
    
    conteudos = cursor.fetchall()

    connect.close()
    return conteudos


def mostra_atividades(id_disciplina):
    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()

    # Puxa da base de dados o titulo, o status e a disciplina das atividades de uma disciplina
    cursor.execute(
        '''
        SELECT id, nome, concluido, prazo, id_disciplina as disciplina FROM todo 
        WHERE categoria = 'ATV' AND disciplina = ?
        ''', (id_disciplina,))
    
    atividades = cursor.fetchall()

    connect.close()
    return atividades


def proximos_conteudos():
    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()

    # Puxa o proximo conteudo a fazer de cada disciplina
    cursor.execute(
        '''
        SELECT nome, concluido, id_disciplina AS disciplina FROM todo 
        WHERE categoria = 'CON' AND concluido = 'False' 
        GROUP BY id_disciplina
        ''')
    
    prox_conteudos = cursor.fetchall()

    connect.close()
    return prox_conteudos


def proximas_atividades():
    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()
    
    # Guarda na variavel o dia de hoje na ordem ano mes e dia
    hoje = datetime.today().strftime('%Y-%m-%d')

    # Puxa as atividades com o prazo de entrega para os proximos 7 dias
    cursor.execute(
        '''
        SELECT nome, prazo, id_disciplina AS disciplina FROM todo 
        WHERE julianday(prazo) - julianday(?) <= 7
        ''', (hoje,))
    
    prox_atividades = cursor.fetchall()

    connect.close()
    return prox_atividades


def atualizaStatus(id, status):
    connect = sqlite3.connect("dashboard.db")
    cursor = connect.cursor()

    # Modifica o status da atividade/conteudo
    cursor.execute("UPDATE todo SET concluido = ? WHERE id = ?", (status, id) )
    
    # Commit do update no banco de dados
    connect.commit()

    connect.close()
    return


def mostra_eventos():
    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()

    cursor.execute(
        '''
        SELECT id, nome, prazo, id_disciplina AS disciplina, concluido FROM todo 
        WHERE prazo NOT NULL
        ''')
    
    eventos = cursor.fetchall()

    connect.close()
    return eventos

def progresso():
    # Guarda numero do mes atual na variavel
    mesAtual = datetime.today().strftime("%m")

    connect = sqlite3.connect("dashboard.db")
    connect.row_factory = dict_factory
    cursor = connect.cursor()


    # Verifica a quantidade de tarefas a serem entregues no mes atual
    cursor.execute(
        '''
        SELECT COUNT(*) AS total FROM todo 
        WHERE strftime('%m', prazo) = ?
        ''', (mesAtual,))

    totalAtividadesMes = cursor.fetchall()


    # Verifica quantas tarefas foram feitas 
    cursor.execute(
        '''
        SELECT COUNT(*) AS concluidas FROM todo
        WHERE strftime('%m', prazo) = ?
        AND concluido = 'True'
        ''', (mesAtual,))
    
    atvConcluidasMes = cursor.fetchall()
    
    return {"total": totalAtividadesMes[0]["total"], "concluidas": atvConcluidasMes[0]["concluidas"]}