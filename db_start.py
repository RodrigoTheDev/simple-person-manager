import sqlite3

def criar_db():
    conn = sqlite3.connect('db/sistema.db')

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CLIENTES (
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   NOME TEXT,
                   TELEFONE INTEGER,
                   EMAIL TEXT
        );  
    ''')

    conn.commit()
    conn.close()
