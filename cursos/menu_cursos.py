from cursos.crud_cursos import cadastrar_curso, listar_cursos, buscar_curso, atualizar_curso, deletar_curso
from limpar_tela.limpar_tela import limpar_tela
from unique.verificar_unique import verificar_unique

def menu_curso():
    """Menu principal dos cursos, permite o usuário fazer uma série de ações."""
    menu = ["Cadastrar Curso", "Listar Cursos", "Buscar Curso", "Atualizar Curso", "Deletar Curso", "Voltar"]

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
                    while True:
                        print("--------------------------------------------")
                        nome_curso = input("Digite o nome do curso que deseja cadastrar:\n")
                        erro_nome_curso_unique = verificar_unique("Cursos", nome_curso, 1, "Curso")

                        if erro_nome_curso_unique:
                            print(erro_nome_curso_unique)
                        else:
                            cadastrar_curso(nome_curso)
                        break

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
                            print("--------------------------------------------")
                            nome_busca = input("Digite nome do curso que deseja buscar:\n")
                            erro_buscar_curso_unique = verificar_unique("Cursos", nome_busca, 1, "Curso")

                            if not erro_buscar_curso_unique:
                                print(f"Curso '{nome_busca}' não cadastrado anteriormente.")
                                break
                            else:
                                nome_buscado = buscar_curso(nome_busca)
                                
                                # TODO: Aparecer a quantidade de alunos, professores e turmas no curso
                                for nome in nome_buscado:
                                    print(f"{nome[0]} - {nome[1]}")
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
                                id_curso = int(input("Digite o ID do curso que deseja atualizar:\n"))

                                for curso in cursos:
                                    if id_curso == curso[0]:
                                        novo_nome_curso = input("Digite o novo nome do curso:\n")
                                        erro_novo_nome_curso_unique = verificar_unique("Cursos", novo_nome_curso, 1, "Curso")

                                        if erro_novo_nome_curso_unique:
                                            print(erro_novo_nome_curso_unique)
                                        else:
                                            atualizar_curso(id_curso, novo_nome_curso)
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

                case 5:
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
                                    print("ID do curso não cadastrado anteriormente.")
                                break

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break

                        else:
                            print("Nenhum curso cadastrado anteriormente.")
                            break

                case 6:
                    print("--------------------------------------------")
                    print("Voltando...")
                    break

                case _:
                    print("--------------------------------------------")
                    print("Opção inválida!")

        except ValueError:
            print("--------------------------------------------")
            print("[ERRO]: Digite um número!")