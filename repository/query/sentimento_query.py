class SentimentoQuery:

    def __init__(self):
        pass

    def count_positivo(self):
        return """
        SELECT
	    count(sentimento)
        FROM sentimento
        WHERE sentimento = 'Positivo'
        """
    
    def count_neutro(self):
        return """
        SELECT
	    count(sentimento)
        FROM sentimento
        WHERE sentimento = 'Neutro'
        """
    
    def count_negativo(self):
        return """
        SELECT
	    count(sentimento)
        FROM sentimento
        WHERE sentimento = 'Negativo'
        """

    def count_misturado(self):
        return """
        SELECT
	    count(sentimento)
        FROM sentimento
        WHERE sentimento = 'Misturado'
        """