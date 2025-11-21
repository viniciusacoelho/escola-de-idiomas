from limpar_tela.limpar_tela import limpar_tela
from professores.menu_atualizar_professor import menu_atualizar_professor

def portal_professor(professor_autenticado):
    menu = ["Visualizar Turma", "Atualizar Cadastro", "Voltar"]
    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("              Escola de Idiomas             ")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    print("Em breve...")
                case 2:
                    menu_atualizar_professor(professor_autenticado[0])
                case 3:
                    print("Voltando...")
                    break

        except ValueError:
            print("[ERRO]: Digite um número!")