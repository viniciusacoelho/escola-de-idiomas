from limpar_tela.limpar_tela import limpar_tela
from professores.cadastramento_professor import cadastramento_professor
from professores.login_professor import login_professor

def identificacao_professor():
    """Página de identificação do professor."""
    menu = ["Criar Conta", "Login", "Voltar"]
    
    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("              Escola de Idiomas")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    cadastramento_professor()
                case 2:
                    login_professor()
                case 3:
                    print("Voltando...")
                    break
                case _:
                    print("Digite uma opção válida!")

        except ValueError:
            print("[ERRO]: Digite um número!")