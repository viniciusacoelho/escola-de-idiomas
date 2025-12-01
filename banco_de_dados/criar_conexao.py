import psycopg2

def criar_conexao() -> str | None:
    "Cria a conexão com o banco de dados PostgreSQL."
    try:
        conexao = psycopg2.connect(
            dbname = 'escola-de-idiomas',
            user = 'postgres',
            password = '1234',
            host = 'localhost',
            port = '5432'
        )
        return conexao
    except Exception as e:
        print(f"[ERRO]: Falha ao criar conexão: {e}")
        return None