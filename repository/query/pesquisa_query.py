class PesquisaQuery:

    def __init__(self):
        pass

    def listar(self, size, offset):
        return f"""
           SELECT
            p.id_pesquisa,
            p.texto,
            p.data,
            p.classificacao_nps,
            p.valor_nps,
            p.foi_analisado,
            s.sentimento
            FROM pesquisa p
            INNER JOIN sentimento s
            ON s.id_pesquisa = p.id_pesquisa
            ORDER BY data DESC LIMIT {size} OFFSET {offset};
            """

    def listar_where_palavra_chave(self, size, offset, palavraChave):
        return f"""
            SELECT
            p.id_pesquisa,
            p.texto,
            p.data,
            p.classificacao_nps,
            p.valor_nps,
            p.foi_analisado,
            s.sentimento
            FROM pesquisa p
            INNER JOIN sentimento s
            ON s.id_pesquisa = p.id_pesquisa
            INNER JOIN palavra_chave pc
            ON pc.id_pesquisa = p.id_pesquisa
            WHERE pc.texto LIKE '%{palavraChave}%'
            ORDER BY data DESC LIMIT {size} OFFSET {offset};
            """

    def listar_where_sentimento(self, size, offset, sentimento):
        return f"""
            SELECT
            p.id_pesquisa,
            p.texto,
            p.data,
            p.classificacao_nps,
            p.valor_nps,
            p.foi_analisado,
            s.sentimento
            FROM pesquisa p
            INNER JOIN sentimento s
            ON s.id_pesquisa = p.id_pesquisa
            WHERE s.sentimento = '{sentimento}'
            ORDER BY data DESC LIMIT {size} OFFSET {offset};
            """

    def listar_where_nps(self, size, offset, nps):
        return f"""
            SELECT
            p.id_pesquisa,
            p.texto,
            p.data,
            p.classificacao_nps,
            p.valor_nps,
            p.foi_analisado,
            s.sentimento
            FROM pesquisa p
            INNER JOIN sentimento s
            ON s.id_pesquisa = p.id_pesquisa
            WHERE p.classificacao_nps = '{nps}'
            ORDER BY data DESC LIMIT {size} OFFSET {offset};
            """

    def criar(self):
        return f"""
        INSERT INTO        
        pesquisa     
        (texto,
        data,
        classificacao_nps,
        valor_nps)
        values
        (
            %s,
            %s,
            %s,
            %s
        )
        """        