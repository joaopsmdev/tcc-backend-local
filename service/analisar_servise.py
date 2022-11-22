from repository.analisar_repository import AnalisarRepository
from utils.comprehend import Comprehend
from model.sentimento import Sentimento
from repository.query.analisar_query import AnalisarQuery
from model.palavra_chave import PalavraChave

class AnalisarService:

    def __init__(self):
        self.repository = AnalisarRepository()
        self.comprehend = Comprehend()
        self.query = AnalisarQuery()

    def analisar(self):
        ls_pesquisa = self.repository.listar_pesquisa_nao_analisado(self.query.listar_pesquisa_nao_analisado())
        for p in ls_pesquisa:
            self.analisar_sentimento(p.texto, p.id)
            self.analisar_palavra_chave(p.texto, p.id)
            self.atualizar_pesquisa_analisado(p.id)

    def atualizar_pesquisa_analisado(self, id):
        self.repository.atualizar_pesquisa_analisado(self.query.atualizar_pesquisa_analisado(), id)
    
    def analisar_sentimento(self, texto, id_pesquisa):
        result = self.comprehend.detectar_sentimento(texto)
        s = Sentimento.converter_in_comprehend(result, id_pesquisa)
        self.repository.salvar_sentimento(self.query.inserir_sentimento(), s)

    def analisar_palavra_chave(self, texto, id_pesquisa):
        result = self.comprehend.detectar_palavra_chave(texto)
        ls_palavra_chave = []
        for r in result["KeyPhrases"]:
            ls_palavra_chave.append(PalavraChave.converter_in_comprehend(r, id_pesquisa))
        self.repository.salvar_palavra_chave(self.query.inserir_palavra_chave(), ls_palavra_chave)
