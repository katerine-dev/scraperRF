# ETL dos dados abertos da Receita Federal 
- [Receita Federal Index](https://dadosabertos.rfb.gov.br/CNPJ/)

Este projeto é uma extensão do trabalho realizado conjunto com a [ScoreEase](https://github.com/scoreease).
O objetivo é extração de dados do [Cadastro Nacional de Pessoas Jurídicas (CNPJ)](lucoes.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp).
Mais especificamente, extrairemos as seguintes tabelas:

- CNAES
- Empresas
- Estabelecimentos
- Motivos ? 
- Municipios
- Naturezas
- Paises
- QualificaçÕes
- Simples
- Socios

### Venv

Primeiro passo ativando o virtual env
```sh
source venv/bin/activate
```
Instalando as dependências do projeto:
```sh
pip3 install -r requirements.txt
```
### Banco de dados

Comando para iniciar o serviço do postgres via docker:
```sh
docker run -d \
    --rm \
	--name scraperDb \
	-e POSTGRES_PASSWORD=scraper \
    -e POSTGRES_USER=scraper \
    -e POSTGRES_DB=scraperDB \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v pgdata:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres
```
Parar o serviço do docker
```sh
docker stop <container-id>
```

### Migrations

Para criar uma nova migração:
```sh
yoyo new --sql
```
Para ver lista de migrations:
```sh
yoyo list 
```
Para executar as migrations:
```sh
yoyo apply
```

Todas tabelas estão descritas no documento em pdf na pasta .docs



