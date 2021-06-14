class Produto():
    def __init__(self, id=None, nome=None, imagens=None, preco=None, parcela=None, valParcela=None):
        self.__id = id
        self.__nome = nome
        self.__imagens = imagens
        self.__preco = preco
        self.__parcela = parcela
        self.__valParcela = valParcela

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id


    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome


    def get_imagens(self):
        return self.__imagens

    def set_imagens(self, img):
        self.__imagens = img


    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco


    def get_parcela(self):
        return self.__parcela

    def set_parcela(self, parcela):
        self.__parcela = parcela


    def get_valParcela(self):
        return self.__valParcela

    def set_valParcela(self, valParcela):
        self.__valParcela = valParcela


