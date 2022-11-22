from typing_extensions import Self
from repository.palavra_chave_repository import PalavraChaveRepository

class PalavraChaveService:

    def __init__(self):
        self.repository = PalavraChaveRepository()

    def nuvem_palavras(self, size, offset, filtro):
        return self.repository.listar_palavra_chave(size, offset, filtro)