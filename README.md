# scraperRF

Estrutura do pacote:

site para scraper
https://dadosabertos.rfb.gov.br/CNPJ/

Bibliotecas 
 psycopg2 = Conexão com o postgress

Para usuário: 

1* passo Ativando o virtual env
```sh
source venv/bin/activate
```
Instalando projeto dependencias:

```sh
pip3 install -r requirements.txt
```

Por que usar o docker: ele vai uniformizar o ambiente de desemvolvimento. (Sem diferença de sistema operacional)


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
docker stop <container-name>
```


TODO
- [] Mover configuração de banco da dados para variavel de ambiente
- [] Quebrar a main em vários arquivos 
- [] Tratar erros (try except)
- [] Fazer função que insere estabelecimento no banco 

PRÓXIMOS PASSOS


Pergunta:
O encoding do cvs de teste é ISO-8859-1, vale pena usar o pandas? ele tem alguma maneira de detectar o encoding? 

