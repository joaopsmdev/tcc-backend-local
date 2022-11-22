from repository.sentimento_repository import SentimentoRepository

class SertimentoService:

    def __init__(self):
        self.repository = SentimentoRepository()

    def sentimento_score(self):
        qntd_positivo = self.repository.contar_positivo()[0]
        qntd_neutro = self.repository.contar_neutro()[0]
        qntd_negativo = self.repository.contar_negativo()[0]
        qntd_misturado = self.repository.contar_misturado()[0]

        total = qntd_positivo + qntd_neutro + qntd_negativo + qntd_misturado

        dist_positivo = (qntd_positivo / total) * 100
        dist_neutro = (qntd_neutro / total) * 100
        dist_negativo = (qntd_negativo / total) * 100
        dist_misturado = (qntd_misturado / total) * 100

        score = dist_positivo - dist_negativo

        return {
            "score": score,
            "dist_positivo": dist_positivo,
            "dist_neutro": dist_neutro,
            "dist_negativo": dist_negativo,
            "dist_misturado": dist_misturado
            }