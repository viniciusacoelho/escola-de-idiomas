import getpass

from limpar_tela.limpar_tela import limpar_tela
from professores.crud_professor import autenticar_professor
from professores.portal_professor import portal_professor

from banco_de_dados.criar_conexao import criar_conexao

def professor(entidade: str, id_turma: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM {entidade}_turma WHERE id_turma = %s", (id_turma,))
        professores_teste = cursor.fetchone()
        return professores_teste
    except Exception as e:
        return f"[ERRO]: Falha ao autenticar e-mail e/ou senha: {e}"
    finally:
        cursor.close()
        conexao.close()

def login_professor():
    """Página de login do professor."""
    while True:
        limpar_tela()

        print("--------------------------------------------")
        print("             Login - Professor")
        print("--------------------------------------------")

        email = input("Digite seu e-mail:\n").lower()
        senha = getpass.getpass("Digite sua senha:\n")

        professor_autenticado = autenticar_professor(email, senha)

        if professor_autenticado:
            print(f"Professor '{professor_autenticado[1]}' logado com sucesso!")
            portal_professor(professor_autenticado)
            break
        else:
            print(f"Usuário e/ou senha incorretos!")