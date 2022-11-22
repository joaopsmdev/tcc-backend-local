from repository.query.analisar_query import AnalisarQuery
from utils.sql_cmd import ComandosSql
from model.pesquisa import Pesquisa

class AnalisarRepository:

    def __init__(self):
        self.sql_cmd = ComandosSql()
        self.query = AnalisarQuery()

    def listar_pesquisa_nao_analisado(self, query):
        return self.sql_cmd.listar(query, Pesquisa, False)

    def salvar_sentimento(self, query, s):
        params = (s.sentimento, s.neutro, s.positivo, s.negativo, s.misturado, s.id_pesquisa)
        self.sql_cmd.salvar(query, params)

    def salvar_palavra_chave(self, query, ls_palavra_chave):
        params = []
        for p in ls_palavra_chave:
            params.append((p.score, p.texto, p.inicio, p.fim, p.id_pesquisa))
        self.sql_cmd.salvar_varios(query, params)

    def atualizar_pesquisa_analisado(self, query, id):
        params = (id,)
        self.sql_cmd.salvar(query, params)