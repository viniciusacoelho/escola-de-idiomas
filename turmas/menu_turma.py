from limpar_tela.limpar_tela import limpar_tela
from turmas.cadastramento_turma import cadastramento_turma
from turmas.crud_turmas import listar_turmas, buscar_turma, atualizar_turma, deletar_turma
from turmas.atualizar_turma import atualizar_turma
from turmas.login_turma import login_turma

def menu_turma():
    """Página do menu da turma."""
    menu = ["Cadastrar Turma", "Logar Turma", "Listar Turma", "Buscar Turma", "Atualizar Turma", "Deletar Turma", "Voltar"]

    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("               Atualizar Turma")
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
                    turmas = listar_turmas()                    
                    
                    if len(turmas) > 0:
                        login_turma()
                    else:
                        print("Nenhuma turma cadastrada anteriormente.")

                case 3:
                    turmas = listar_turmas()                    

                    if len(turmas) > 0:
                        print("Turmas listadas com sucesso!")
                        print("--------------------------------------------\n")
                        
                        for turma in turmas:
                            print(f"Turma {turma[0]}:\n{turma[1]} ({turma[2]})")
                            print("--------------------------------------------")
                    
                    else:
                        print("Nenhuma turma cadastrada anteriormente.")

                case 4:
                    while True:    
                        turmas = listar_turmas()                    

                        if len(turmas) > 0:
                            try:
                                id_turma = int(input("Digite o ID da turma que você deseja buscar:\n"))
                                turmas = buscar_turma(id_turma)

                                for turma in turmas:
                                    print("--------------------------------------------")
                                    print(f"Turma {turma[0]}:\n{turma[1]} ({turma[2]})")
                                break

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break

                        else:
                            print("Nenhuma turma cadastrada anteriormente.")
                            break

                case 5:
                    while True:    
                        turmas = listar_turmas()                    

                        if len(turmas) > 0:
                            try:
                                id_turma = int(input("Digite o ID da turma que você deseja atualizar:\n"))
                                atualizar_turma(id_turma)

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break

                        else:
                            print("Nenhuma turma cadastrada anteriormente.")
                            break

                case 6:
                    while True:    
                        turmas = listar_turmas()                    

                        if len(turmas) > 0:
                            try:
                                id_turma = int(input("Digite o ID da turma que você deseja deletar:\n"))
                                deletar_turma(id_turma)
                                break

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break

                        else:
                            print("Nenhuma turma cadastrada anteriormente.")
                            break

                case 7:  
                    print("Voltando...")
                    break
                case _:
                    print("Digite uma opção válida!")

        except ValueError:
            print("[ERRO]: Digite um número!")