from dbm.dumb import _Database
from sqlite3 import Cursor
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="RandomBl0quia22092001",
    database = "tcc"
)

Cursor = conexao.cursor()

comando = 'INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)'

Cursor.close()
conexao.close()