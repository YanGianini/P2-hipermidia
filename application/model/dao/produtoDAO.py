from application.model.entity.produto import Produto
import json


lista_carrinho = []

class ProdutoDAO():
    def __init__(self):
        self.__lista_carrinho = lista_carrinho

    def lista_produtos(self):
        return self.__lista_produtos

    def lista_carrinho(self):
        return self.__lista_carrinho

    def dict_to_list(self, lista_prod):
        lista = []
        for produto_item in lista_prod:
            produto = Produto()
            produto.set_id(produto_item['id'])
            produto.set_nome(produto_item['name'])
            produto.set_imagens(produto_item['images'])
            preco = produto_item['price']
            produto.set_preco(preco['value'])
            produto.set_parcela(preco['installments'])
            produto.set_valParcela(preco['installmentValue'])
            lista.append(produto)
        return lista

    def listar_produtos(self):
        lista = []
        with open('buscape.json', 'r') as file:
            produto_json = json.load(file)
            lista = self.dict_to_list(produto_json)
        return lista

