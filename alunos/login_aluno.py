import getpass

from limpar_tela.limpar_tela import limpar_tela
from alunos.crud_alunos import autenticar_aluno
from alunos.portal_aluno import portal_aluno

def login_aluno():
    """Página de login do aluno."""
    while True:
        limpar_tela()

        print("--------------------------------------------")
        print("              Escola de Idiomas")
        print("--------------------------------------------")
        print("Começe a aprender agora!\n")

        usuario = input("Digite seu usuário:\n").lower()
        senha = getpass.getpass("Digite sua senha:\n")

        aluno_autenticado = autenticar_aluno(usuario, senha)

        if aluno_autenticado:
            portal_aluno(aluno_autenticado)
            break
        else:
            print(f"Usuário e/ou senha incorretos!")