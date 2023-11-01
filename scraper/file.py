import chardet
import zipfile
import requests
import tempfile

# Função para pegar um arquivo


def fetch_file(url):
    response = requests.get(url)  # faz um request http do método get
    temp_file = tempfile.NamedTemporaryFile()  # criar um arquivo temporário
    temp_file.write(response.content)
    return temp_file


def extract_zipfile(file, destination_path):
    zip_file = zipfile.ZipFile(file)  # instanciando um objeto da classe ZipFile
    zip_file.extractall(destination_path)  # caminho para pasta temporária


def get_encoding(file_path):
    with open(file_path, 'rb') as f:  # Abre o arquivos especificado em modo binária
        lines = f.readlines()[:250]  # Lê as primeras 100 linhas do arquivo, (por que?)
        encoding = chardet.detect(b''.join(lines))['encoding']  # Detecta o encoding do arquivo
        print("encoding detectado:", encoding)
        return encoding  # precisa chamar ela ainda


# Função responsável por trocar o byte Nul por '' dentro de um valor do dicionário dict_endereco
# Não precisou pq eu inclui a solução diretamente no reader
#def remove_null_bytes(tabela_dict):
#    for key, value in tabela_dict.items():
#        if isinstance(value, str):
#            tabela_dict[key] = value.replace('\x00', '')
#    return tabela_dict
