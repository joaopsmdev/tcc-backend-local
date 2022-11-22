class Pesquisa:

    def __init__(self):
        pass

    def __init__(self, id, texto, data, classificacao_nps, valor_nps, foi_analisado, sentimento):
        self.id = id
        self.texto = texto
        self.data = data
        self.classificacao_nps = classificacao_nps
        self.valor_nps = valor_nps
        self.foi_analisado = foi_analisado
        self.sentimento = sentimento

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def texto(self):
        return self.__texto
    
    @texto.setter
    def texto(self, texto):
        self.__texto = texto
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def classificacao_nps(self):
        return self.__classificacao_nps
    
    @classificacao_nps.setter
    def classificacao_nps(self, classificacao_nps):
        self.__classificacao_nps = classificacao_nps

    @property
    def valor_nps(self):
        return self.__valor_nps
    
    @valor_nps.setter
    def valor_nps(self, valor_nps):
        self.__valor_nps = valor_nps

    @property
    def foi_analisado(self):
        return self.__foi_analisado
    
    @foi_analisado.setter
    def foi_analisado(self, foi_analisado):
        self.__foi_analisado = foi_analisado

    @property
    def sentimento(self):
        return self.__sentimento
    
    @sentimento.setter
    def sentimento(self, sentimento):
        self.__sentimento = sentimento

    def builder(row):
        return Pesquisa(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    def json(self):
        return  {
                "id": self.id,
                "texto": self.texto,
                "data": self.data,
                "classificacao_nps": self.classificacao_nps,
                "valor_nps": self.valor_nps,
                "foi_analisado": self.foi_analisado,
                "sentimento": self.sentimento
            }
