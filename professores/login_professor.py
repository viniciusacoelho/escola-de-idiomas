import getpass
from limpar_tela.limpar_tela import limpar_tela
from professores.crud_professor import autenticar_professor
from professores.portal_professor import portal_professor

def login_professor():
    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("             Login - Professor")
        print("--------------------------------------------")

        email = input("Digite seu e-mail:\n").lower()
        senha = getpass.getpass("Digite sua senha:\n")

        professor_autenticado = autenticar_professor(email, senha)

        if professor_autenticado:
            portal_professor(professor_autenticado)
            break
        else:
            print(f"Usuário e/ou senha incorretos!")