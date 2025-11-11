from limpar_tela.limpar_tela import limpar_tela
from alunos.cadastramento_aluno import cadastramento_aluno
from alunos.crud_alunos import listar_alunos, atualizar_aluno, deletar_aluno
from alunos.atualizar_alunos import atualizar_alunos
def menu_aluno():
    menu = ["Cadastrar Aluno", "Listar Alunos", "Atualizar Aluno", "Deletar Aluno", "Voltar"]

    limpar_tela()

    while True:
        print("--------------------------------------------")
        print("                   Alunos")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        print("--------------------------------------------")
        try:
            opcao = int(input("Digite uma opção:\n"))

            match opcao:
                case 1:
                    cadastramento_aluno()
                    limpar_tela()
                case 2:
                    # TODO: Colocar uma validação se há alunos cadastrados anteriormente
                    # TODO: Melhorar isso:
                    alunos = listar_alunos()
                    
                    for aluno in alunos:
                        print(f"{aluno[0]} - {aluno[1]}")
                    limpar_tela()
                case 3:

                    while True:
                        try:
                            # TODO: Colocar uma validação se há alunos cadastrados anteriormente
                            # TODO: Colocar uma validação se o ID é válido
                            id_aluno = input("Digite o ID do aluno que deseja atualizar:\n")
                            atualizar_alunos(id_aluno)
                            break
                        except ValueError:
                            print("[ERRO]: Digite um número!")


                case 4:

                    while True:
                        try:
                            # TODO: Colocar uma validação se há alunos cadastrados anteriormente
                            # TODO: Colocar uma validação se o ID é válido
                            id_aluno = input("Digite o ID do aluno que deseja deletar:\n")
                            deletar_aluno(id_aluno[0])
                            break
                        except ValueError:
                            print("[ERRO]: Digite um número!")
                case 5:
                    print("Voltando...")
                    limpar_tela()
                    break
                case _:
                    print("Digite uma opção válida!")
                
        except ValueError:
            print("--------------------------------------------")
            print("[ERRO]: Digite um número!")
            limpar_tela()