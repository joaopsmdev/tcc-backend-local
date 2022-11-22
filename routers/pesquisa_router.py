from datetime import date
from typing import List
from fastapi import APIRouter
from service.pesquisa_service import PesquisaService
from pydantic import BaseModel

router = APIRouter()

service = PesquisaService()

class Pesquisa(BaseModel):
    id: int
    texto: str
    data: date
    classificacao_nps: str
    valor_nps: float
    foi_analisado: bool
    sentimento: str

class PesquisaForm(BaseModel):
    texto: str
    data: date
    classificacao_nps: str
    valor_nps: float


@router.get("/pesquisa", response_model=List[Pesquisa])
async def listar(size: int = 20, offset: int = 0, sentimento: str = None, nps: str = None, palavraChave: str = None):
    return service.listar(size, offset, palavraChave, sentimento, nps)

@router.post("/pesquisa")
async def criar(pesquisa: PesquisaForm):
    return service.criar(pesquisa)

