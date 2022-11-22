class Sentimento:

    def __init__(self):
        pass

    def __init__(self, id, sentimento, neutro, positivo, negativo, misturado, id_pesquisa):
        self.id = id
        self.sentimento = sentimento
        self.neutro = neutro
        self.positivo = positivo
        self.negativo = negativo
        self.misturado = misturado
        self.id_pesquisa = id_pesquisa

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def sentimento(self):
        return self.__sentimento
    
    @sentimento.setter
    def sentimento(self, sentimento):
        self.__sentimento = sentimento

    @property
    def neutro(self):
        return self.__neutro
    
    @neutro.setter
    def neutro(self, neutro):
        self.__neutro = neutro
    
    @property
    def positivo(self):
        return self.__positivo
    
    @positivo.setter
    def positivo(self, positivo):
        self.__positivo = positivo

    @property
    def negativo(self):
        return self.__negativo
    
    @negativo.setter
    def negativo(self, negativo):
        self.__negativo = negativo

    @property
    def misturado(self):
        return self.__misturado
    
    @misturado.setter
    def misturado(self, misturado):
        self.__misturado = misturado

    @property
    def id_pesquisa(self):
        return self.__id_pesquisa
    
    @id_pesquisa.setter
    def id_pesquisa(self, id_pesquisa):
        self.__id_pesquisa = id_pesquisa

    def converter_in_comprehend(result, id_pesquisa):
        sentimento = ""
        if result["Sentiment"] == "POSITIVE":
            sentimento = "Positivo"
        elif result["Sentiment"] == "NEUTRAL":
            sentimento = "Neutro"
        elif result["Sentiment"] == "NEGATIVE":
            sentimento = "Negativo"
        elif result["Sentiment"] == "MIXED":
            sentimento = "Misturado"

        return Sentimento(None, sentimento, result["SentimentScore"]["Neutral"], result["SentimentScore"]["Positive"], result["SentimentScore"]["Negative"], result["SentimentScore"]["Mixed"], id_pesquisa)

    def __str__(self) -> str:
        return f"({self.id}, {self.sentimento})"