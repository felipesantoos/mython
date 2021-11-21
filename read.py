# -*- encoding: utf-8 -*-

# Importação do driver do MySQL.
import mysql.connector

# Configuração da conexão.
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="teste"
)

# Variável que vai executar o comando SQL.
cursor = connection.cursor()

# Comando SQL.
sql = "SELECT * FROM users"

# Execução do comando e armazenamento de todos os registros retornados.
cursor.execute(sql)
results = cursor.fetchall()

# Fechamento da conexão.
cursor.close()
connection.close()

# Listagem de todos os registros retornados.
for result in results:
    print(result)
