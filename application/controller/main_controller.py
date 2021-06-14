from application import app 
from flask import render_template, request, url_for, redirect
from application.model.dao.produtoDAO import ProdutoDAO


produtoDAO = ProdutoDAO()
lista_produtos = produtoDAO.lista_produtos()
lista_carrinho = produtoDAO.lista_carrinho()


@app.route("/")
def index():
    return render_template("index.html", lista_produtos=lista_produtos, lista_carrinho=lista_carrinho)