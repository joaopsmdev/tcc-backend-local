class PalavraChaveQuery:

    def __init__(self):
        pass

    def listar(self, size, offset):
        return f"""
        SELECT 
        pc.id_palavra_chave,
        pc.score,
        pc.texto,
        pc.inicio,
        pc.fim,
        pc.id_pesquisa,
        p.classificacao_nps
        FROM palavra_chave pc
        INNER JOIN pesquisa p
        ON pc.id_pesquisa = p.id_pesquisa
        ORDER BY pc.texto ASC LIMIT {size} OFFSET {offset};
        """

    def listar_where_texto(self, size, offset, filtro):
        return f"""
        SELECT 
        pc.id_palavra_chave,
        pc.score,
        pc.texto,
        pc.inicio,
        pc.fim,
        pc.id_pesquisa,
        p.classificacao_nps
        FROM palavra_chave pc
        INNER JOIN pesquisa p
        WHERE pc.texto like '%{filtro}%'
        ORDER BY pc.texto ASC LIMIT {size} OFFSET {offset};
        """