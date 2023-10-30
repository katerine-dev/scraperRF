import file
import db.conexao
import db.estabelecimento
import db.endereco
import os
import csv
import tempfile


nome_situacao_cadastral = {  # dicionário para referenciar o nome da situação cadastral no código informado pela tabela
    "01": "NULA",
    "02": "ATIVA",
    "03": "SUSPENSA",
    "04": "INAPTA",
    "08": "BAIXADA"
}
# TODO tornar função genérico (qualquer csv)


def process_csv(csv_path, cur):
    print("Incluindo informações no Banco de Dados... aguarde!")
    with open(csv_path, 'r', encoding='ISO-8859-1') as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        for row in reader:
            dict_estabecimento = {
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
            dict_estabecimento["id_endereco"] = db.endereco.create_endereco(dict_estabecimento["endereco"], cur)
            db.estabelecimento.create_estabelecimento(dict_estabecimento, cur)


conexao = db.conexao.conectar_banco()
cur = conexao.cursor()
# Faça o que precisa com o cursor e a conexão
zip_file = file.fetch_file("https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos8.zip")
temp_dir = tempfile.TemporaryDirectory()  # criando uma pasta temporária
file.extract_zipfile(zip_file, temp_dir.name)  # extraindo para um diretório temporátio
zip_file.close()  # ao fechar um arquivo temporário ele é automaticamente deletado

csv_name = os.listdir(temp_dir.name)[0]  # pegando o nome do csv
csv_path = os.path.join(temp_dir.name, csv_name)  # invés de concatenar strings, vou usar o path.join

process_csv(csv_path, cur)
conexao.commit()
temp_dir.cleanup()  # limpa o diretorio temporario e apaga todos os csvs
