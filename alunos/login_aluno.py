import getpass

from limpar_tela.limpar_tela import limpar_tela
from alunos.crud_alunos import autenticar_aluno
from alunos.home_alunos import home_alunos

def login_aluno():
    while True:
        limpar_tela()

        print("--------------------------------------------")
        print("              Escola de Idiomas")
        print("--------------------------------------------")
        print("Começe a aprender agora!\n")
        
        usuario = input("Digite seu usuário: ")
        senha = getpass.getpass("Digite sua senha: ")

        aluno_autenticado = autenticar_aluno(usuario, senha)
        
        if aluno_autenticado:
            home_alunos(aluno_autenticado)
            break
        else:
            print(f"Usuário e/ou senha incorretos!")