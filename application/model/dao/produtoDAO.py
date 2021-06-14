from application.model.entity.produto import Produto

lista_produtos = ["tv", "coisa", "calculadora"]

lista_carrinho = ["coisas", "ricas"]

class ProdutoDAO():
    def __init__(self):
        self.__lista_produtos = lista_produtos
        self.__lista_carrinho = lista_carrinho

    def lista_produtos(self):
        return self.__lista_produtos

    def lista_carrinho(self):
        return self.__lista_carrinho
