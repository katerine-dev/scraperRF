def create_estabelecimento(dict_estabelecimento, cur):
    cur.execute(
        """
        INSERT INTO endereco (
            tipo_logradouro, 
            logradouro, 
            numero_logradouro, 
            complemento_logradouro, 
            bairro, 
            cep, 
            uf, 
            municipio
        )
        VALUES (
            %(tipo_logradouro)s, 
            %(logradouro)s, 
            %(numero_logradouro)s, 
            %(complemento_logradouro)s,
            %(bairro)s,
            %(cep)s,
            %(uf)s,
            %(municipio)s
        )
        """,
        dict_estabelecimento
    )