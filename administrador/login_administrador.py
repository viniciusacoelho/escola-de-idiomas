import getpass

from limpar_tela.limpar_tela import limpar_tela
from administrador.menu_administrador import menu_administrador

def login_administrador():
    "Página de login do administrador que pede uma senha de acesso para logar no sistema."
    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("                    Login")
        print("--------------------------------------------")

        senha = getpass.getpass("Digite a senha de acesso:\n")

        if senha == "adm1234":
            print("Administrador logado com sucesso!")
            menu_administrador()
            break
        else:
            print("Senha inválida!")