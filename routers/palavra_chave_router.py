from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from service.palavra_chave_service import PalavraChaveService
from pydantic import BaseModel

router = APIRouter()

service = PalavraChaveService()

class PalavraChave(BaseModel):
    id: int
    score: float
    texto: str
    inicio: int
    fim: int
    id_pesquisa: int
    classificacao_nps: str

@router.get("/nuvemPalavras", response_model=List[PalavraChave])
async def nuvem_palavras(size: int = 10, offset: int = 0, filtro: str = None):
    return service.nuvem_palavras(size, offset, filtro)