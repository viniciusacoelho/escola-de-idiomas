import getpass

from limpar_tela.limpar_tela import limpar_tela
from administrador.menu_administrador import menu_administrador

def identificacao_administrador():
    "Página de identificação do administrador que pede uma senha de acesso."
    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("               Identifique-se")
        print("--------------------------------------------")

        senha = getpass.getpass("Digite a senha de acesso:\n")

        if senha == "adm1234":
            menu_administrador()
            break
        else:
            print("Senha inválida!")