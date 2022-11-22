from repository.query.nps_query import NpsQuery
from utils.sql_cmd import ComandosSql

class NpsRepository:

    def __init__(self):
        self.sql_cmd = ComandosSql()
        self.query = NpsQuery()

    def contar_promotor(self):
        return self.sql_cmd.consultar(self.query.count_promotor())

    def contar_neutro(self):
        return self.sql_cmd.consultar(self.query.count_neutro())

    def contar_detrator(self):
        return self.sql_cmd.consultar(self.query.count_detrator())