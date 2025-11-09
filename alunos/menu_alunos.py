from limpar_tela.limpar_tela import limpar_tela
from alunos.cadastramento_aluno import cadastramento_aluno
from alunos.crud_alunos import cadastrar_aluno, listar_alunos, atualizar_aluno, deletar_aluno

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
                case 2:
                    # TODO: Colocar uma validação se há alunos cadastrados anteriormente
                    # TODO: Melhorar isso:
                    print(f"{listar_alunos()}")
                    # for aluno in alunos:
                    # print(f"{aluno}")
                case 3:
                    
                    while True:
                        try:
                            # TODO: Colocar uma validação se há alunos cadastrados anteriormente
                            # TODO: Colocar uma validação se o ID é válido
                            id_aluno = input("Digite o ID do aluno que deseja atualizar:\n")
                            atualizar_aluno(id_aluno[0])
                            break
                        except ValueError:
                            print("[ERRO]: Digite um número!")
                    # TODO: Perguntar o que quer atualizar do aluno
                    novo_nome_completo = input("Digite o novo nome do aluno:")
                
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
