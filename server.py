import sys

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

# Importando scripts de bancos de dados
import db_insertions as dbi, db_search as dbs, db_start as dbstart

app = Flask(__name__)

CORS(app)


# Rotas de páginas
@app.route('/')
def index():
    result = dbs.ver_clientes()
    return render_template('index.html', teste=result)


# Rotas de páginas
@app.route('/cliente/gerenciar')
def gerenciar_clientes():
    result = dbs.ver_clientes()
    return render_template('gerenciar_clientes.html', clientes=result)


if __name__ == '__main__':
    dbstart.criar_db()
    app.run()