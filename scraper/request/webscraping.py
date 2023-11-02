from bs4 import BeautifulSoup
import requests

from scraper import file

# URL DA PÁGINA
url = 'https://dadosabertos.rfb.gov.br/CNPJ/'

# Realiza o request http
response = requests.get(url)
print('status code: {}'.format(response.status_code))
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar todas as tabelas pelo href
file_urls = soup.findAll('a', href=True)

def baixa_links(file_urls):
    # Lista para armazenar as tabelas .zip
    zip_urls = []  # armazenar em um vetor

    for link in file_urls:
        href = link.get('href')
        if href.endswith('.zip'):
            # Construa a URL completa do arquivo .zip
            zip_url = url + href
            zip_urls.append(zip_url)
            return zip_urls


file.baixar_temporariamente(baixa_links(file_urls))