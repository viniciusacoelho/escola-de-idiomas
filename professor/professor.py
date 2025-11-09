from limpar_tela import limpar_tela

def identificacao_professor():
    menu = ["Criar Conta", "Login", "Voltar"]

    print("--------------------------------------------")
    print("              Escola de Idiomas             ")
    print("--------------------------------------------")

    for i in range(len(menu)):
        print(f"{i + 1} - {menu[i]}")
    
    while True:
        try:
            opcao = input("Digite uma opção: ")
            break
        except ValueError:
            print("[ERRO]: Digite um número!")

    match opcao:
        case 1:
        case 2:
        case 3:
        case _:
            print("Digite uma opção válida!")