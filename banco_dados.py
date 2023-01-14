import sqlite3
from sqlite3 import Error
import os

caminho = os.path.dirname(__file__)
nome_bd = caminho + "\\biblioteca.db"


### cria conexão com banco de dados
def conexao_banco():
    try:
        con=None
        conexao = sqlite3.connect(nome_bd)
    except Error as ex:
        print(ex)
    finally:
        return conexao


### função específica para o comando select
def dql(query):
    vcon = conexao_banco()
    c = vcon.cursor()
    c.execute(query)
    resultado = c.fetchall()
    vcon.close()
    return resultado


### função específica para os comandos insert, delete ou update
def dml(query):
    try:
        vcon = conexao_banco()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
        return "Sucesso"
    except Error as ex:
        return "Erro SQL: " + str(ex)