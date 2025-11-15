from cursos.crud_cursos import cadastrar_curso, listar_cursos, atualizar_curso, deletar_curso
from limpar_tela.limpar_tela import limpar_tela

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
                case 2:
                    cursos = listar_cursos()

                    if len(cursos) > 0:
                        print("Cursos listados com sucesso!")
                        print("--------------------------------------------")

                        for curso in cursos:
                            print(f"{curso[0]} - {curso[1]}")

                    else:
                        print("Nenhum curso cadastrado anteriormente.")

                case 3:
                    while True:
                        cursos = listar_cursos()

                        if len(cursos) > 0:
                            try:
                                print("--------------------------------------------")
                                id_curso = int(input("Digite o ID do curso que deseja atualizar:\n"))
                                
                                for curso in cursos:
                                    if id_curso == curso[0]:
                                        novo_nome_curso = input("Digite o novo nome do curso:\n")
                                        
                                        if novo_nome_curso != curso:
                                            atualizar_curso(id_curso, novo_nome_curso)
                                            break
                                        else:
                                            print(f"Curso '{novo_nome_curso}' já cadastrado anteriormente.")
                                            break
                                            
                                else:
                                    print("ID do curso não cadastrado anteriormente.")
                                break

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break
                                    
                case 4:
                    while True:
                        cursos = listar_cursos()
                        
                        if len(cursos) > 0:    
                            try:
                                print("--------------------------------------------")
                                id_curso = int(input("Digite o ID do curso que deseja deletar:\n"))
                                
                                for curso in cursos:
                                    if id_curso == curso[0]:
                                        deletar_curso(id_curso)
                                        break
                                    else:
                                        print("ID do curso não existe!")
                                
                            except ValueError:
                                print("[ERRO]: Digite um número!")

                        else:
                            print("Nenhum curso cadastrado anteriormente.")
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