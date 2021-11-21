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

# Variável que vai executar a atualização.
cursor = connection.cursor()

# Comando SQL e dados.
sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
data = (
    "Primeiro usuário atualizado",
    "primeirousuarioatualizado@teste.com",
    1
)

# Execução e efetivação do comando.
cursor.execute(sql, data)
connection.commit()

# Amazenamento da quantidade de registros afetados.
records_affected = cursor.rowcount

# Fechamendo da conexão.
cursor.close()
connection.close()

# Exibição da quantidade de registros afetados.
print(records_affected, " registros atualizados")
