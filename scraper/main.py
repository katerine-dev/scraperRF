import requests
import tempfile
import zipfile
import os
import csv
import psycopg

# Função para pegar um arquivo


def fetch_file(url):
    response = requests.get(url)  # faz um request http do método get
    temp_file = tempfile.NamedTemporaryFile()  # criar um arquivo temporário
    temp_file.write(response.content)
    return temp_file


def extract_zipfile(file, destination_path):
    zip_file = zipfile.ZipFile(file)  # instanciando um objeto da classe ZipFile
    zip_file.extractall(destination_path)  # caminho para pasta temporária


nome_situacao_cadastral = {  # dicionário para referenciar o nome da situação cadastral no código informado pela tabela
    "01": "NULA",
    "02": "ATIVA",
    "03": "SUSPENSA",
    "04": "INAPTA",
    "08": "BAIXADA"
}
# TODO tornar função genérico (qualquer csv)


def process_csv(csv_path, cur):
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
                "fax_numero": row[25],
                "email": row[26],
                "situacao_especial": row[27],
                "data_situacao_especial": row[28],
            }
            create_endereco(dict_estabecimento["endereco"], cur)


def conectar_banco():
    try:
        conn = psycopg.connect(
            "dbname=scraperDB host=localhost user=scraper password=scraper port=5432", autocommit=True
        )
        return conn
    except Exception as e:
        print(f"Erro na conexão com o PostgreSQL: {e}")


def create_endereco(dict_endereco, cur):
    id = cur.execute(
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
        RETURNING id;
        """,
        dict_endereco
    )
    return id


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


conexao = conectar_banco()
cur = conexao.cursor()
# Faça o que precisa com o cursor e a conexão
zip_file = fetch_file("https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos8.zip")
temp_dir = tempfile.TemporaryDirectory()  # criando uma pasta temporária
extract_zipfile(zip_file, temp_dir.name)  # extraindo para um diretório temporátio
zip_file.close()  # ao fechar um arquivo temporário ele é automaticamente deletado

csv_name = os.listdir(temp_dir.name)[0]  # pegando o nome do csv
csv_path = os.path.join(temp_dir.name, csv_name)  # invés de concatenar strings, vou usar o path.join

process_csv(csv_path, cur)
conexao.commit()
temp_dir.cleanup()  # limpa o diretorio temporario e apaga todos os csvs
