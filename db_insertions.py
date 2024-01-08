import sqlite3

def inserir_cliente(nome,telefone,email):
    conn = sqlite3.connect('db/sistema.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO CLIENTES (NOME,TELEFONE,EMAIL) VALUES (?,?,?)", (nome,telefone,email))

    conn.commit()
    conn.close()

# inserir_cliente('Marcelitos',999999,'mama@email.com')