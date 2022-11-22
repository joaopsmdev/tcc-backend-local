from datetime import date
from typing import List
from fastapi import APIRouter
from service.sentimento_service import SertimentoService

router = APIRouter()

service = SertimentoService()

@router.get("/sentimentoScore")
def sentimento_score():
    return service.sentimento_score()