import requests
import tempfile
import zipfile
import os
import csv


# Função para pegar um arquivo


def fetch_file(url):
    response = requests.get(url)  # faz um request http do método get
    temp_file = tempfile.NamedTemporaryFile()  # criar um arquivo temporário
    temp_file.write(response.content)
    return temp_file


def extract_zipfile(file, destination_path):
    zip_file = zipfile.ZipFile(file)  # instanciando um objeto da classe ZipFile
    zip_file.extractall(destination_path)  # caminho para pasta temporária

# TODO tornar função genérico (qualquer csv)
def process_csv(csv_path):
    with open(csv_path, 'r', encoding='ISO-8859-1') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)  # TODO: inserir na base de dados ao invés de imprimir


zip_file = fetch_file("https://dadosabertos.rfb.gov.br/CNPJ/Estabelecimentos8.zip")
temp_dir = tempfile.TemporaryDirectory()  # criando uma pasta temporária
extract_zipfile(zip_file, temp_dir.name)  # extraindo para um diretório temporátio
zip_file.close()  # ao fechar um arquivo temporário ele é automaticamente deletado

csv_name = os.listdir(temp_dir.name)[0]  # pegando o nome do csv
csv_path = os.path.join(temp_dir.name, csv_name)  # invés de concatenar strings, vou usar o path.join

temp_dir.cleanup()  # limpa o diretorio temporario

process_csv(csv_path)
