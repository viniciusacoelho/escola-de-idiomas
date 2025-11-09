from cursos.crud_cursos import cadastrar_curso, listar_cursos, atualizar_curso, deletar_curso
from limpar_tela.limpar_tela import limpar_tela

# def menu_curso(usuario):
def menu_curso():
    menu = ["Cadastrar Curso", "Listar Cursos", "Atualizar Curso", "Deletar Curso", "Voltar"]
    
    limpar_tela()
    
    while True:
        print("--------------------------------------------")
        print("                   Cursos")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        print("--------------------------------------------")
        try:
            opcao = int(input("Digite uma opção:\n"))

            match opcao:
                case 1:
                    print("--------------------------------------------")
                    nome_curso = input("Digite o nome do curso que deseja cadastrar:\n")
                    cadastrar_curso(nome_curso)
                    limpar_tela()
                    # TODO: Verificar se 'if nome_curso' funciona, se não funcionar, usar isso:
                    # curso = 1
                case 2:
                    # if nome_curso:
                    print("--------------------------------------------")
                    cursos = listar_cursos()

                    for curso in cursos:
                        print(f"{curso[0]} - {curso[1]}")
                    limpar_tela()
                    # else:
                    #     print("Nenhum curso cadastrado anteriormente.")

                case 3:
                    # if nome_curso:
                        
                    while True:
                        try:
                            # if nome_curso:
                            print("--------------------------------------------")
                            id_curso = int(input("Digite o ID do curso que deseja atualizar:\n"))
                            
                            # else:
                            #     print("ID do curso inválido!")
                            break
                        except ValueError:
                            print("[ERRO]: Digite um número!")
                            # limpar_tela()
                    print("--------------------------------------------")
                    novo_nome_curso = input("Digite o novo nome do curso:\n")
                    atualizar_curso(id_curso, novo_nome_curso)
                    limpar_tela()
                    # else:
                    #     print("Nenhum curso cadastrado anteriormente.")
                case 4:
                    # if nome_curso:
                    while True:
                        try:
                            print("--------------------------------------------")
                            id_curso = int(input("Digite o ID do curso que deseja deletar:\n"))
                            break
                        except ValueError:
                            print("[ERRO]: Digite um número!")
                            # TODO: Verificar se dá para colocar:
                            # limpar_tela()

                    # if id_curso:
                    deletar_curso(id_curso)
                    limpar_tela()
                    # else:
                    #     print("ID inválido.")
                    # else:
                    #     print("Nenhum curso cadastrado anteriormente.")
                case 5:
                    print("--------------------------------------------")
                    print("Voltando...")
                    break
                case _:
                    print("--------------------------------------------")
                    print("Opção inválida!")
        except ValueError:
            print("--------------------------------------------")
            print("[ERRO]: Digite um número!")

# TODO: Colocar ORDER BY ASC no DBeaver ou aqui