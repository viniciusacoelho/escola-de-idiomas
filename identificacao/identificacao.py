from limpar_tela.limpar_tela import limpar_tela
from administrador.administrador import administrador

def identificacao(opcao_escolhida):
    limpar_tela()

    menu = ["Criar Conta", "Login", "Voltar"]

    print("--------------------------------------------")
    print("              Escola de Idiomas             ")
    print("--------------------------------------------")

    for i in range(len(menu)):
        print(f"{i + 1} - {menu[i]}")
    
    while True:
        try:
            opcao = input("Digite uma opção: ")
            if opcao == 1 and opcao_escolhida == 1:
                administrador()
            else:
                print("Opção inválida!")
                limpar_tela()
                continue
            break
        except ValueError:
            print("[ERRO]: Digite um número!")
            limpar_tela()