import sqlite3

# PESQUISA DE CLIENTES
#region


# Pesquisa geral de clientes, a função retorna todas as linhas da tabela de clientes
def ver_clientes():
    conn = sqlite3.connect("db/sistema.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM CLIENTES")
    result = cursor.fetchall()

    print(result)

    return result

# Pesquisa por telefone, a função retorna as linhas que possuirem o telefone do argumento
def buscar_telefone(telefone):
    conn = sqlite3.connect("db/sistema.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM CLIENTES WHERE TELEFONE={telefone}")
    result = cursor.fetchall()

    print(result)
    return result

# Função que bosca pelo nome , a função retorna as linhas que possuírem o nome parecido com o do argumento
def busca_nome(nome):
    conn = sqlite3.connect("db/sistema.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM CLIENTES
        WHERE NOME LIKE ?
    ''', (f'%{nome}%',))
    result = cursor.fetchall()

    print(result)
    return result

#endregion

# PESQUISA DE ARQUIVOS