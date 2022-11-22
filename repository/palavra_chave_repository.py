from utils.sql_cmd import ComandosSql
from repository.query.palavra_chave_query import PalavraChaveQuery

from model.palavra_chave import PalavraChave

class PalavraChaveRepository:

    def __init__(self):
        self.sql_cmd = ComandosSql()
        self.query = PalavraChaveQuery()

    def listar_palavra_chave(self, size, offset, filtro):
        query = self.query.listar(size, offset)
        if filtro:
            query = self.query.listar_where_texto(size, offset, filtro)
        return self.sql_cmd.listar(query, PalavraChave)
