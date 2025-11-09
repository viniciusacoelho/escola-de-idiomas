from limpar_tela import limpar_tela
from cadastro_alunos import cadastro_alunos
def menu_alunos():
    menu = ["Criar conta", "Login", "Sair"]
    while True:
        print("--------------------------------------------")
        print("              Escola de Idiomas")
        print("--------------------------------------------")
        
        for i in range(len(menu)):
            print(f"{i - 1} - {menu[i]}")

        try:
            opcao = input("Digite uma opção: ")
            break
        except ValueError:
            print("[ERRO]: Digite um número!")

    limpar_tela
    cadastro_alunos()