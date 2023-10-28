import psycopg


def conectar_banco():
    try:
        conn = psycopg.connect(
            "dbname=scraperDB host=localhost user=scraper password=scraper port=5432", autocommit=True
        )
        return conn
    except Exception as e:
        print(f"Erro na conexão com o PostgreSQL: {e}")
