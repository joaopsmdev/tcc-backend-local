from this import s
from repository.nps_repository import NpsRepository
from model.custom.nps import Nps

class NpsService:

    def __init__(self):
        self.repository = NpsRepository()

    def info(self):
        qntd_promotor = self.repository.contar_promotor()[0]
        qntd_neutro = self.repository.contar_neutro()[0]
        qntd_detrator = self.repository.contar_detrator()[0]

        total = qntd_detrator + qntd_neutro + qntd_promotor

        dist_promotor = (qntd_promotor / total) * 100
        dist_neutro = (qntd_neutro / total) * 100
        dist_detrator = (qntd_detrator / total) * 100

        score = dist_promotor - dist_detrator

        return Nps(float(score), float(dist_promotor), float(dist_neutro), float(dist_detrator))