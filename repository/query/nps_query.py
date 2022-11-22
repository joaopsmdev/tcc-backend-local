class NpsQuery:

    def __init__(self):
        pass

    def count_promotor(self):
        return """
        SELECT
	    count(classificacao_nps)
        FROM pesquisa
        WHERE classificacao_nps = 'Promotor'
        """
    
    def count_neutro(self):
        return """
        SELECT
	    count(classificacao_nps)
        FROM pesquisa
        WHERE classificacao_nps = 'Neutro'
        """
    
    def count_detrator(self):
        return """
        SELECT
	    count(classificacao_nps)
        FROM pesquisa
        WHERE classificacao_nps = 'Detrator'
        """