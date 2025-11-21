from limpar_tela.limpar_tela import limpar_tela
from turmas.cadastramento_turma import cadastramento_turma
from turmas.crud_turmas import listar_turmas, deletar_turma, atualizar_turma

def menu_turma():
    menu = ["Cadastrar Turma", "Listar Turma", "Buscar Turma", "Atualizar Turma", "Deletar Turma", "Voltar"]

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
                    cadastramento_turma()
                case 2:
                    listar_turmas()                    
                case 3:
                    atualizar_turma()
                case 4:
                    deletar_turma()
                case 5:  
                    print("Voltando...")
                    break
                case _:
                    print("Digite uma opção válida!")

        except ValueError:
            print("[ERRO]: Digite um número!")