from limpar_tela.limpar_tela import limpar_tela
from professores.menu_atualizar_professor import menu_atualizar_professor
from professores.crud_professor import buscar_professor
from turmas.crud_turmas import inserir_turma
from turmas.portal_turma import curso_turma, aluno_turma
from cursos.crud_cursos import listar_cursos

from banco_de_dados.criar_conexao import criar_conexao

def professor_turma(id_professor: int):
    """
    Relacionamento de professores e turmas cadastrados no banco de dados.

    Args:
        id_professor (int): ID do professor cadastrado no banco de dados.

    Returns:
        professor_turmas: Relacionamento de professores e turmas cadastrados no banco de dados.

    Raises:
        [ERRO]: Falha ao visualizar professor.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT t.id_turma, t.dia_semana, t.horario FROM professor_turma pt INNER JOIN turmas t ON t.id_turma = pt.id_turma WHERE id_professor = %s", (id_professor,))
        professor_turmas = cursor.fetchall()
        return professor_turmas
    except Exception as e:
        print(f"[ERRO]: Falha ao relacionar professor com turma: {e}")
    finally:
        cursor.close()
        conexao.close()

def professor_curso(id_professor: int, id_curso: int):
    """
    Relacionamento de professores e cursos cadastrados no banco de dados.

    Args:
        id_professor (int): ID do professor cadastrado no banco de dados.
        id_curso (int): ID do curso cadastrado no banco de dados.

    Returns:
        professor_curso: Relacionamento de professores e cursos cadastrados no banco de dados.

    Raises:
        [ERRO]: Falha ao relacionar professor com curso.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO professor_curso VALUES (%s, %s)", (id_professor, id_curso))
        conexao.commit()
        print("Professor inserido no curso com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao relacionar professor com curso: {e}")
    finally:
        cursor.close()
        conexao.close()

def relacionar_professor_curso(id_professor: int):
    """
    Relacionamento de professores e cursos cadastrados no banco de dados.

    Args:
        id_professor (int): ID do professor cadastrado no banco de dados.

    Returns:
        professor_curso: Relacionamento de professores e cursos cadastrados no banco de dados.

    Raises:
        [ERRO]: Falha ao relacionar professor com curso.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT c.nome_curso FROM professor_curso pc INNER JOIN professor_curso p ON c.id_curso = pc.id_curso WHERE id_professor = %s", (id_professor,))
        professor_turmas = cursor.fetchall()
        return professor_turmas
    except Exception as e:
        print(f"[ERRO]: Falha ao relacionar professor com curso: {e}")
    finally:
        cursor.close()
        conexao.close()

def portal_professor(professor_autenticado: str):
    """
    Página do portal do professor.

    Args:
        professor_autenticado (db): Todos os dados cadastrados do professor autenticado.
    """
    menu = ["Visualizar Turma", "Selecionar Curso", "Atualizar Cadastro", "Mostrar Cadastro", "Voltar"]

    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("              Escola de Idiomas")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    turmas = professor_turma(professor_autenticado[0])

                    if len(turmas) > 0:
                        print(f"Professor: {professor_autenticado[1]}")

                        for turma in turmas:
                            print("--------------------------------------------")
                            print(f"Turma {turma[0]}:")
                            cursos = curso_turma(turma[0])

                            if len(cursos) > 0:
                                for curso in cursos:
                                    print(f"Curso: {curso[0]}")

                            else:
                                print("Nenhum curso cadastrado anteriormente na turma.")

                            alunos = aluno_turma(turma[0])
                            print("Alunos: ")

                            if len(alunos) > 0:
                                for aluno in alunos:
                                    print(aluno[0])

                            else:
                                print("Nenhum aluno cadastrado anteriormente na turma.")

                            # TODO: Ajeitar isso, está funcionando, mas se não tiver curso, ele não mostra o horário, mesmo se 
                            # estiver cadastrado
                            if len(cursos) > 0:
                                for curso in cursos:
                                    print(f"Horário: {curso[1]} ({curso[2]})")

                            else:
                                print("Nenhum dia/horário cadastrado anteriormente na turma.")

                    else:
                        print("Nenhuma turma cadastrada anteriormente.")

                case 2:
                    while True:
                        cursos = listar_cursos()

                        if len(cursos) > 0:
                            print("--------------------------------------------")
                            for curso in cursos:
                                print(f"{curso[0]} - {curso[1]}")
                            print("0 - Nenhuma das opções acima.")

                            try:
                                print("--------------------------------------------")
                                id_idioma_lecionado = int(input("Digite o ID do idioma que deseja lecionar:\n"))

                                if id_idioma_lecionado == 0:
                                    break                                

                                for curso in cursos:
                                    if id_idioma_lecionado == curso[0]:
                                        # TODO: Verificação se o professor escolher o idioma já lecionado anterimente
                                        professor_curso(professor_autenticado[0], id_idioma_lecionado)
                                        break
                                else:
                                    print("ID do curso não cadastrado anteriormente.")
                                break

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break

                        print("Nenhum curso cadastrado anteriormente.")
                        break

                case 3:
                    menu_atualizar_professor(professor_autenticado[0])
                case 4:
                    professores = buscar_professor(professor_autenticado[2])

                    for professor in professores:
                        print("--------------------------------------------")
                        print(f"Professor {professor[0]}:\nNome completo: {professor[1]}\nE-mail: {professor[2]}\nGênero: {professor[3]}\nCPF: {professor[4]}\nNúmero de telefone: {professor[5]}\nEndereço: {professor[6]}\\nSenha: *****")

                        # cursos = relacionar_professor_curso(professor_autenticado[0])
                        # if len(cursos) > 0:
                        #     print("Curso:")

                        #     for curso in cursos:
                        #         print(curso[0])

                        # else:
                        #     print("Curso: Nenhum curso escolhido anteriormente.")

                case 5:
                    print("Voltando...")
                    break

        except ValueError:
            print("[ERRO]: Digite um número!")