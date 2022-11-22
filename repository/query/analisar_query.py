class AnalisarQuery:

    def __init__(self):
        pass

    def listar_pesquisa_nao_analisado(self):
        return """
            SELECT
            p.id_pesquisa,
            p.texto,
            p.data,
            p.classificacao_nps,
            p.valor_nps,
            p.foi_analisado,
            s.sentimento
            FROM pesquisa p
            LEFT JOIN sentimento s
            ON s.id_pesquisa = p.id_pesquisa
            WHERE p.foi_analisado = 0 LIMIT 10;
        """

    def inserir_sentimento(self):
        return """
            INSERT INTO sentimento
            (
                sentimento,
                neutro,
                positivo,
                negativo,
                misturado,
                id_pesquisa
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
        """
    
    def inserir_palavra_chave(self):
        return """
            INSERT INTO palavra_chave
            (
                score,
                texto,
                inicio,
                fim,
                id_pesquisa
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s
            )
        """
    
    def atualizar_pesquisa_analisado(self):
        return """
            UPDATE pesquisa
            SET foi_analisado = 1
            WHERE id_pesquisa = %s
        """