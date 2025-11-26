import getpass

from limpar_tela.limpar_tela import limpar_tela
from alunos.crud_aluno import autenticar_aluno
from alunos.portal_aluno import portal_aluno

def login_aluno():
    """Página de login do aluno que pede seus dados já cadastrados anteriormente."""
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
            print(f"Aluno '{aluno_autenticado[1]}' logado com sucesso!")
            portal_aluno(aluno_autenticado)
            break
        else:
            print(f"Usuário e/ou senha incorretos!")