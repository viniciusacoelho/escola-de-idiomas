from cursos.crud_cursos import cadastrar_curso, listar_cursos, buscar_curso, atualizar_curso, deletar_curso
from limpar_tela.limpar_tela import limpar_tela

def menu_curso():
    """Menu principal dos cursos, permitindo o usuário fazer uma série de ações."""
    menu = ["Cadastrar Curso", "Listar Cursos", "Atualizar Curso", "Deletar Curso", "Voltar"]
    
    # TODO: Buscar Curso
    # menu = ["Cadastrar Curso", "Listar Cursos", "Buscar Curso", "Atualizar Curso", "Deletar Curso", "Voltar"]

    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("                   Cursos")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
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
                                
                                lista_cursos_cadastrados = []
                                
                                for curso in cursos:
                                    lista_cursos_cadastrados.append(curso[1])

                                for curso in cursos:
                                    if id_curso == curso[0]:
                                        novo_nome_curso = input("Digite o novo nome do curso:\n")    

                                        if novo_nome_curso not in lista_cursos_cadastrados:
                                            atualizar_curso(id_curso, novo_nome_curso)
                                        else:
                                            print(f"Curso '{novo_nome_curso}' já cadastrado anteriormente.")
                                        break

                                else:
                                    print("ID do curso não cadastrado anteriormente.")
                                break

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break

                        else:
                            print("Nenhum curso cadastrado anteriormente.")
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
                                else:
                                    print("ID do curso não cadastrado anteriormente.")
                                break

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break

                        else:
                            print("Nenhum curso cadastrado anteriormente.")
                            break

                case 5:
                    print("--------------------------------------------")
                    print("Voltando...")
                    break
                
                # TODO: Melhorar Buscar Curso
                case 6:
                    busca_nome = input("Digite nome para buscar: ")
                    nome_bucado = buscar_curso(busca_nome)
                    # TODO: Pode aparecer a quantidade de alunos, professores e turmas no curso
                    for nome in nome_bucado:
                        print(f"{nome[0]} - {nome[1]}")

                case _:
                    print("--------------------------------------------")
                    print("Opção inválida!")

        except ValueError:
            print("--------------------------------------------")
            print("[ERRO]: Digite um número!")

# TODO: Colocar ORDER BY ASC no DBeaver ou no 'crud_curso' para o 'id_curso' ficar em ordem