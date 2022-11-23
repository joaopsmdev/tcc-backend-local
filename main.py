import imp
from logging import getLogger

from fastapi import FastAPI
from starlette_exporter import handle_metrics
from fastapi.middleware.cors import CORSMiddleware

from routers import root
from routers import health_check
from routers import pesquisa_router
from routers import nps_router
from routers import analisar_router
from routers import palavra_chave_router
from routers import sentimento_router

application_name = "artificialis-analisys-backend"
application_description = "Aplicacao para analise textual"

logger = getLogger()

app = FastAPI(
    title=application_name,
    description=application_description,
    version="v1.0.0",
)

origins = ["*"]

app.add_middleware(
     CORSMiddleware,
     allow_origins=origins,
     allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/metrics", handle_metrics)
app.include_router(root.router, tags=["App"])
app.include_router(health_check.router, tags=["App"])
app.include_router(pesquisa_router.router, tags=["Pesquisa"])
app.include_router(nps_router.router, tags=["Nps"])
app.include_router(analisar_router.router, tags=["Analisar"])
app.include_router(palavra_chave_router.router, tags=["Palavra Chave"])
app.include_router(sentimento_router.router, tags=["Sentimento"])