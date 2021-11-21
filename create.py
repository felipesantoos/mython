# -*- encoding: utf-8 -*-

# Importação das bibliotecas necessárias.
import mysql.connector
import datetime

# Configuração da conexão.
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="teste"
)

# Variável que executará as operações.
cursor = connection.cursor()

# Comando e dados.
sql = "INSERT INTO users (name, email, created) VALUES (%s, %s, %s)"
data = (
    "Primeiro usuário",
    "primeirousuario@teste.com",
    datetime.datetime.today()
)

# Execução e efetivação do comando.
cursor.execute(sql, data)
connection.commit()

# Obtenção do ID do usuário recém-cadastrado.
userid = cursor.lastrowid

# Fechamento da conexão.
cursor.close()
connection.close()

# Exibição do último ID inserido no banco de dados.
print("Foi cadastrado o nome usuário de ID: ", userid)
