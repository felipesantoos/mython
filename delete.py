# -*- encoding: utf-8 -*-

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="teste"
)

cursor = connection.cursor()

sql = "DELETE FROM users WHERE id = %s"
data = (1,)

cursor.execute(sql, data)
connection.commit()

records_affected = cursor.rowcount

cursor.close()
connection.close()

print(records_affected, "registros excluídos")
