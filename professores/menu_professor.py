from limpar_tela import limpar_tela

def professor():
    pass
# def cadastrar_professor():
    menu = ["Criar Conta", "Login", "Voltar"]
    print("--------------------------------------------")
    print("              Escola de Idiomas             ")
    print("--------------------------------------------")
    for i in range(len(menu)):
        print(f"{i + 1} - {menu[i]}")
    while True:
        try:
            opcao = input("Digite uma opção: ")
            match opcao:
                case 1:
                    cadastramento_professor()
                case 2:
                    login_professores()
                case 3:
                    break
                case _:
                    print("Digite uma opção válida!")
        except ValueError:
            print("[ERRO]: Digite um número!")
