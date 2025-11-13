from cursos.crud_cursos import cadastrar_curso, listar_cursos, atualizar_curso, deletar_curso
from limpar_tela.limpar_tela import limpar_tela

# def menu_curso(usuario):
def menu_curso():
    menu = ["Cadastrar Curso", "Listar Cursos", "Atualizar Curso", "Deletar Curso", "Voltar"]
    
    
    while True:
        limpar_tela()
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
                    # TODO: Verificar se 'if nome_curso' funciona, se não funcionar
                case 2:
                    cursos = listar_cursos()

                    if len(cursos) > 0:
                        print("--------------------------------------------")

                        for curso in cursos:
                            print(f"{curso[0]} - {curso[1]}")

                    else:
                        print("Nenhum curso cadastrado anteriormente.")

                case 3:
                    while True:
                        try:
                            print("--------------------------------------------")
                            id_curso = int(input("Digite o ID do curso que deseja atualizar:\n"))
                            existe_curso = atualizar_curso(id_curso)
                            
                            if existe_curso:
                                print("ID do curso não existe!")
                                # limpar_tela()
                            else:    
                                print("--------------------------------------------")
                                novo_nome_curso = input("Digite o novo nome do curso:\n")
                                existe_nome_curso = atualizar_curso(id_curso, novo_nome_curso)

                                if not existe_nome_curso:
                                    print("Nenhum curso cadastrado anteriormente.")
                                else:
                                    break
                                
                        except ValueError:
                            print("[ERRO]: Digite um número!")
                case 4:
                    while True:
                        try:
                            print("--------------------------------------------")
                            id_curso = int(input("Digite o ID do curso que deseja deletar:\n"))
                            existe_id_curso = deletar_curso(id_curso)
                            if existe_id_curso:
                                break
                            else:
                                print("ID não existe!")

                        except ValueError:
                            print("[ERRO]: Digite um número!")

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