from datetime import datetime
codigo_tipo_estabelecimento = {  # dicionário para referenciar o nome da situação cadastral no código informado pela tabela
    "1": "matriz",
    "2": "filial"
}


def normalize_date(data_situacao_cadastral):
    data_situacao_cadastral_convertida = datetime.strptime(data_situacao_cadastral, '%Y%m%d').date()
    return data_situacao_cadastral_convertida


def create_estabelecimento(dict_estabelecimento, cur):
    dict_estabelecimento['tipo_estabelecimento'] = codigo_tipo_estabelecimento[dict_estabelecimento['tipo_estabelecimento']]

    if dict_estabelecimento['data_situacao_cadastral'] != "":
        dict_estabelecimento['data_situacao_cadastral'] = normalize_date(dict_estabelecimento['data_situacao_cadastral'])
    cur.execute(
        """
        INSERT INTO estabelecimento (
            id_endereco,
            cnpj, 
            tipo_estabelecimento, 
            nome_fantasia, 
            codigo_situacao_cadastral, 
            nome_situacao_cadastral, 
            data_situacao_cadastral, 
            codigo_motivo_situacao_cadastral, 
            nome_cidade_exterior,
            codigo_pais,
            data_inicio_atividade,
            cnae_fiscal_principal,
            cnae_fiscal_secundaria,
            ddd_telefone_1,
            telefone_1,
            ddd_telefone_2,
            telefone_2,
            ddd_fax,
            fax_numero,
            email,
            situacao_especial,
            data_situacao_especial
            
        )
        VALUES (
            %(id_endereco)s, 
            %(cnpj)s, 
            %(tipo_estabelecimento)s, 
            %(nome_fantasia)s,
            %(codigo_situacao_cadastral)s,
            %(nome_situacao_cadastral)s,
            %(data_situacao_cadastral)s,
            %(codigo_motivo_situacao_cadastral)s,
            %(nome_cidade_exterior)s,
            %(codigo_pais)s,
            %(data_inicio_atividade)s,
            %(cnae_fiscal_principal)s,
            %(cnae_fiscal_secundaria)s,
            %(ddd_telefone_1)s,
            %(telefone_1)s,
            %(ddd_telefone_2)s,
            %(telefone_2)s,
            %(ddd_fax)s,
            %(fax_numero)s,
            %(email)s,
            %(situacao_especial)s,
            %(data_situacao_especial)s
        )
        """,
        dict_estabelecimento
    )
