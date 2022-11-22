from fastapi import APIRouter, Depends, status, HTTPException
from service.nps_service import NpsService
from pydantic import BaseModel

router = APIRouter()

service = NpsService()

class Nps(BaseModel):
    nps_score: float
    dist_promotor: float
    dist_neutro: float
    dist_detrator: float

@router.get("/nps")
async def info():
    return service.info()