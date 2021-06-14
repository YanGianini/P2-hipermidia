import re
from application import app 
from flask import render_template, request, url_for, redirect
from application.model.dao.produtoDAO import ProdutoDAO


produtoDAO = ProdutoDAO()
lista_produtos = produtoDAO.listar_produtos()
lista_carrinho = produtoDAO.lista_carrinho()


@app.route("/")
def index():
    return render_template("index.html", lista_produtos=lista_produtos, lista_carrinho=lista_carrinho)


@app.route("/adicionar/<id>")
def adicionar(id):
    for produto in lista_produtos:
        if int(id)==produto.get_id():
            lista_carrinho.append(produto)
            return redirect(url_for('index'))
            
@app.route("/remover/<id>")
def remover(id):
    for produto in lista_carrinho:
        if int(id)==produto.get_id():
            lista_carrinho.remove(produto)
            return redirect(url_for('index'))