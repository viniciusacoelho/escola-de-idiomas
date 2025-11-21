from limpar_tela.limpar_tela import limpar_tela
from alunos.menu_atualizar_alunos import menu_atualizar_alunos
from cursos.crud_cursos import listar_cursos, matricular_aluno_curso, ja_matriculado
# from unique.verificar_unique import verificar_unique

def portal_aluno(aluno_autenticado):
    """
    Portal do aluno referente ao aluno logado.

    Args:
        aluno_autenticado (list): Todos os dados cadastrados do aluno autenticado.
    """
    menu = ["Vizualizar Turma", "Atualizar Cadastro", "Escolher Curso", "Sair"]
    # menu = ["Vizualizar Turma", "Atualizar Cadastro", "Mudar Curso", "Sair"]
    # menu = ["Vizualizar Turma", "Atualizar Cadastro", "Mostrar Caadastro", "Mudar Curso", "Sair"]

    while True:
        limpar_tela()

        print("--------------------------------------------")
        print("             Escola de Idiomas              ")
        print("--------------------------------------------")

        print(f"Bem-vindo de volta, {aluno_autenticado[1]}!\n")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        print("--------------------------------------------")
        try:
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    # TODO: Quando o aluno entra ele vê em qual curso ele tá matriculado, ve seus colegas de turma e seu professor
                    # Curso: Inglês
                    # Turma:
                    # 1 - Fulano
                    # 2 - Sicrano
                    # 3 - Beltrano
                    # Professor: José
                    # Horário: 12:34
                    print("Em breve")
                case 2:
                    menu_atualizar_alunos(aluno_autenticado[0])
                case 3:
                    while True:
                        print("--------------------------------------------\n")
                        cursos = listar_cursos()

                        if len(cursos) > 0:
                            try:
                                for curso in cursos:
                                    print(f"{curso[0]} - {curso[1]}")

                                print("--------------------------------------------")
                                id_curso = int(input("Digite o ID do curso que você deseja se matricular:\n"))
                                for curso in cursos:
                                    if id_curso == curso[0]:
                                        curso_escolhido = ja_matriculado(aluno_autenticado[0], id_curso)
                                        if not curso_escolhido:
                                            matricular_aluno_curso(aluno_autenticado[0], id_curso)
                                        else:
                                            print(f"Aluno '{aluno_autenticado[1]}' já matriculado no curso.")
                                            # TODO: Verificar se tem como fazer isso
                                            # print(f"Aluno {aluno_autenticado[1]} já matriculado no curso {curso[1]}.")
                                        break

                                else:
                                    print("ID do curso não cadastrado anteriormente.")
                                break

                            except ValueError:
                                print("[ERRO]: Digite um número!")

                        else:
                            print("Nenhum curso cadastrado anteriormente.")
                            break
                case 4:
                    break
                case _:
                    print("Opção inválida!")

        except ValueError:
            print("[ERRO]: Digite um número!")