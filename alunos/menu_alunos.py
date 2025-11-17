from limpar_tela.limpar_tela import limpar_tela
from alunos.cadastramento_aluno import cadastramento_aluno
from alunos.crud_alunos import listar_alunos, deletar_aluno
from alunos.menu_atualizar_alunos import menu_atualizar_alunos

def menu_aluno():
    """Menu principal dos alunos."""
    # TODO: Buscar Aluno
    menu = ["Cadastrar Aluno", "Listar Alunos", "Atualizar Aluno", "Deletar Aluno", "Voltar"]

    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("                   Alunos")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção:\n"))

            match opcao:
                case 1:
                    cadastramento_aluno()
                case 2:
                    # TODO: Colocar uma validação se há alunos cadastrados anteriormente
                    alunos = listar_alunos()
                    
                    if len(alunos) > 0:
                        print(f"Alunos listados com sucesso!")
                        print("--------------------------------------------")
            
                        # TODO: Melhorar isso:
                        for aluno in alunos:
                            print(f"{aluno[0]} - {aluno[1]}")
                    else:
                        print("Nenhum aluno cadastrado anteriormente")

                case 3:
                    while True:
                        alunos = listar_alunos()

                        if len(alunos) > 0: 
                            try:
                                id_aluno = int(input("Digite o ID do aluno que deseja atualizar:\n"))
                                
                                for aluno in alunos:
                                    if id_aluno == aluno[0]:
                                        menu_atualizar_alunos(id_aluno)
                                        break
                                else:
                                    print("ID do aluno inválido!")
                                    break

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break

                        else:
                            print("Nehum aluno cadastrado anteriormente.")
                            break
                case 4:
                    while True:
                        alunos = listar_alunos()

                        if len(alunos) > 0:
                            try:
                                id_aluno = int(input("Digite o ID do aluno que deseja deletar:\n"))
                                
                                for aluno in alunos:
                                    if id_aluno == aluno[0]:
                                        deletar_aluno(id_aluno, alunos[1])
                                        break
                                else:
                                    print("ID do aluno inválido!")
                                    break

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break
                        
                        else:
                            print("Nenhum aluno cadastrado anteriormente")
                            break
                
                case 5:
                    print("Voltando...")
                    break
                case _:
                    print("Digite uma opção válida!")
                
        except ValueError:
            print("--------------------------------------------")
            print("[ERRO]: Digite um número!")