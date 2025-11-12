import getpass

from limpar_tela.limpar_tela import limpar_tela
from alunos.crud_alunos import login
from alunos.home_alunos import home_alunos

def login_aluno():
    limpar_tela()

    print("--------------------------------------------")
    print("              Escola de Idiomas")
    print("--------------------------------------------")
    print("Começe a aprender agora!\n")
    
    usuario = input("Digite seu usuário: ").lower()
    senha = getpass.getpass("Digite sua senha: ")

    login(usuario, senha)

    home_alunos(usuario)