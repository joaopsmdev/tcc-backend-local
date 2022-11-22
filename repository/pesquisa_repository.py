from repository.query.pesquisa_query import PesquisaQuery
from utils.sql_cmd import ComandosSql
from model.pesquisa import Pesquisa

class PesquisaRepository:

    def __init__(self):
        self.sql_cmd = ComandosSql()
        self.query = PesquisaQuery()

    def listar(self, size, offset, palavraChave, sentimento, nps):

        query = self.query.listar(size, offset)
        if palavraChave and not sentimento and not nps:
            query = self.query.listar_where_palavra_chave(size, offset, palavraChave)
        elif sentimento and not nps and not palavraChave:
            query = self.query.listar_where_sentimento(size, offset, sentimento)
        elif nps and not sentimento and not palavraChave:
            query = self.query.listar_where_nps(size, offset, nps)
        
        return self.sql_cmd.listar(query, Pesquisa)

    def salvar(self,pesquisa):
        query = self.query.criar()
        params = (pesquisa.texto, pesquisa.data, pesquisa.classificacao_nps, pesquisa.valor_nps)
        self.sql_cmd.salvar(query, params)

