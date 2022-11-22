from repository.query.sentimento_query import SentimentoQuery
from utils.sql_cmd import ComandosSql


class SentimentoRepository:
    
    def __init__(self):
        self.sql_cmd = ComandosSql()
        self.query = SentimentoQuery()
        
    def contar_positivo(self):
        return self.sql_cmd.consultar(self.query.count_positivo())

    def contar_neutro(self):
        return self.sql_cmd.consultar(self.query.count_neutro())

    def contar_negativo(self):
        return self.sql_cmd.consultar(self.query.count_negativo())

    def contar_misturado(self):
        return self.sql_cmd.consultar(self.query.count_misturado())