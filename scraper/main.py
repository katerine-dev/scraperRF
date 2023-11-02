import file
import db.conexao
import db.estabelecimento
import db.endereco
import os
import csv
import tempfile

from scraper.request import webscraping

nome_situacao_cadastral = {  # dicionário para referenciar o nome da situação cadastral no código informado pela tabela
    "01": "NULA",
    "02": "ATIVA",
    "03": "SUSPENSA",
    "04": "INAPTA",
    "08": "BAIXADA"
}
# TODO tornar função genérico (qualquer csv)


def process_csv(csv_path, conexao):
    print("Incluindo informações no Banco de Dados... aguarde!")
    with open(csv_path, 'r', encoding = file.get_encoding(csv_path)) as csv_file:
        reader = csv.reader((row.replace('\0', '') for row in csv_file), delimiter=";") # trocar o byte Nul por '' dentro de um valor do dicionário
        for row in reader:
            dict_estabelecimento = {
                "cnpj": row[0] + row[1] + row[2],
                "tipo_estabelecimento": row[3],
                "nome_fantasia": row[4],
                "codigo_situacao_cadastral": row[5],
                "nome_situacao_cadastral": nome_situacao_cadastral[row[5]],
                "data_situacao_cadastral": row[6],
                "codigo_motivo_situacao_cadastral": row[7],
                "nome_cidade_exterior": row[8],
                "codigo_pais": row[9],
                "data_inicio_atividade": row[10],
                "cnae_fiscal_principal": row[11],
                "cnae_fiscal_secundaria": row[12],
                "endereco": {  # Referência para tabela endereço
                    "tipo_logradouro": row[13],
                    "logradouro": row[14],
                    "numero_logradouro": row[15],
                    "complemento_logradouro": row[16],
                    "bairro": row[17],
                    "cep": row[18],
                    "uf": row[19],
                    "municipio": row[20]
                },
                "ddd_telefone_1": row[21],
                "telefone_1": row[22],
                "ddd_telefone_2": row[23],
                "telefone_2": row[24],
                "ddd_fax": row[25],
                "fax_numero": row[26],
                "email": row[27],
                "situacao_especial": row[28],
                "data_situacao_especial": row[29]
            }
            #file.remove_null_bytes(dict_estabelecimento)  # Corrige line contains NUL
            #file.remove_null_bytes(dict_estabelecimento["endereco"])
            with conexao.transaction():
                dict_estabelecimento["id_endereco"] = db.endereco.create_endereco(dict_estabelecimento["endereco"], cur)
                # raise Exception("Erro forçado!") # Verificando se realmente tem rollback
                db.estabelecimento.create_estabelecimento(dict_estabelecimento, cur)


conexao = db.conexao.conectar_banco()
cur = conexao.cursor()
print("Feito a conexão")
temp_dir = tempfile.TemporaryDirectory()

links_receita_federal = webscraping.baixa_links_receita()
estabelecimentos_urls = list(filter(lambda url: "Estabelecimentos" in url, links_receita_federal))  # Identificar os estabelecimentos
print(estabelecimentos_urls)
for url in estabelecimentos_urls:  # Para cada link de estabelecimento:
    zip_file = file.fetch_file(url)  # criando uma pasta temporária
    file.extract_zipfile(zip_file, temp_dir.name)  # extraindo para um diretório temporátio
    zip_file.close()  # ao fechar um arquivo temporário ele é automaticamente deletado
    print("Extraído os arquivos")
    csv_name = os.listdir(temp_dir.name)[0]  # pegando o nome do csv
    csv_path = os.path.join(temp_dir.name, csv_name)  # invés de concatenar strings, vou usar o path.join

    process_csv(csv_path, conexao)
    conexao.commit()
    temp_dir.cleanup()  # limpa o diretorio temporario e apaga todos os csvs
