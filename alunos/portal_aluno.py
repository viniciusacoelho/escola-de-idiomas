from limpar_tela.limpar_tela import limpar_tela
from alunos.menu_atualizar_alunos import menu_atualizar_alunos
from cursos.crud_cursos import listar_cursos, matricular_aluno_curso, ja_matriculado
from turmas.portal_turma import aluno_turma, curso_turma, professor_turma
from alunos.crud_aluno import buscar_aluno, aluno_curso

from banco_de_dados.criar_conexao import criar_conexao

def curso_aluno(id_aluno: int):
    """
        Lista os cursos cadastrados no banco de dados.

        Returns:
            lista_cursos: Lista dos cursos castrados.

        Raises:
            [ERRO]: Falha ao listar curso.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT c.id_curso, c.nome_curso FROM aluno_curso ac INNER JOIN cursos c ON c.id_curso = ac.id_curso WHERE id_aluno = %s", (id_aluno,))
        lista_cursos = cursor.fetchall()
        return lista_cursos
        # return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao relacionar curso aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def sair_curso(id_aluno: int, id_curso: int):
    """
        Lista os cursos cadastrados no banco de dados.

        Returns:
            id_aluno: ID do aluno cadastrado no banco de dados.
            id_curso: ID do curso cadastrado no banco de dados.

        Raises:
            [ERRO]: Falha ao listar curso.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM aluno_curso WHERE id_aluno = %s AND id_curso = %s", (id_aluno, id_curso))
        print("Aluno deletado do curso com sucesso!")
        conexao.commit()
    except Exception as e:
        print(f"[ERRO]: Falha ao relacionar aluno curso: {e}")
    finally:
        cursor.close()
        conexao.close()

def portal_aluno(aluno_autenticado):
    """
    Portal do aluno referente ao aluno logado.

    Args:
        aluno_autenticado (db): Todos os dados cadastrados do aluno autenticado.
    """
    menu = ["Vizualizar Turma", "Atualizar Cadastro", "Mostrar Cadastro", "Escolher Curso", "Sair Curso", "Sair"]
    # menu = ["Vizualizar Turma", "Atualizar Cadastro", "Mostrar Cadastro", "Mudar Curso", "Sair"]

    while True:
        limpar_tela()

        print("--------------------------------------------")
        print("             Escola de Idiomas              ")
        print("--------------------------------------------")

        print(f"Bem-vindo de volta, {aluno_autenticado[1]}!\n")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    turmas = aluno_turma(aluno_autenticado[0])
                    
                    if len(turmas) > 0:
                        cursos = curso_turma(aluno_autenticado[0])

                        if len(cursos) > 0:
                            for curso in cursos:
                                print(f"Curso: {curso[0]}")

                                turmas = aluno_turma(aluno_autenticado[0])
                                if len(turmas) > 0:
                                    for turma in turmas:
                                        print(f"Turma: {turma[0]}")
                                else:
                                    print("Turma\nNenhuma turma cadastrada anteriormente.")

                                professores = professor_turma(aluno_autenticado[0])
                                if len(professores) > 0:
                                    for professor in professores:
                                        print(f"Professor: {professor[1]}")
                                else:
                                    print("Professor:\nNenhum professor cadastrado anteriormente.")

                                # TODO: Colocar os colegas de classe do aluno
                                alunos = aluno_turma(turma[0])
                                if len(alunos) > 0:
                                    for aluno in alunos:
                                        print(aluno[1])
                                else:
                                    print("Nenhum aluno cadastrado anteriormente na turma.")

                                if len(cursos) > 0:
                                    print(f"Dia/Horário: {curso[2]} ({curso[3]})")
                                else:
                                    print("Dia/Horário\nNenhum dia/horário cadastrado anteriormente.")

                        else:
                            print("Nenhum curso cadastrado anteriormente.")

                    else:
                        print("Nenhuma turma cadastrada anteriormente.")

                case 2:
                    menu_atualizar_alunos(aluno_autenticado[0])
                case 3:
                    alunos = buscar_aluno(aluno_autenticado[2])

                    for aluno in alunos:
                        print(f"Aluno {aluno[0]}\nNome completo: {aluno[1]}\nUsuário: {aluno[2]}\nE-mail: {aluno[3]}\nCPF: {aluno[4]}\nData de nascimento: {aluno[5]}\nNúmero de telefone: {aluno[6]}\nSenha: *****")

                        cursos = aluno_curso(aluno[0])
                        if len(cursos) > 0:
                            print("Curso:")

                            for curso in cursos:
                                print(curso[0])

                        else:
                            print("Curso: Nenhum curso escolhido anteriormente.")

                case 4:
                    while True:
                        print("--------------------------------------------")
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
                case 5:
                    while True:
                        print("--------------------------------------------")
                        cursos = curso_aluno(aluno_autenticado[0])
                        
                        if cursos:
                            for curso in cursos:
                                print(f"{curso[0]} - {curso[1]}")
                            
                            try:
                                print("--------------------------------------------")
                                id_curso = int(input("Digite o ID do curso que você deseja sair:\n"))
                                for curso in cursos:
                                    if id_curso == curso[0]:
                                        curso_escolhido = ja_matriculado(aluno_autenticado[0], id_curso)

                                        if curso_escolhido:
                                            sair_curso(aluno_autenticado[0], id_curso)
                                        else:
                                            print(f"Aluno '{aluno_autenticado[1]}' não matriculado no curso.")
                                        break

                                else:
                                    print("Nenhum do curso não escolhido anteriormente.")
                                break

                            except ValueError:
                                print("[ERRO]: Digite um número!")

                        else:
                            print("Nenhum curso cadastrado anteriormente.")
                            break
                case 6:
                    print("Saindo...") # ou Voltando...
                    # exit()
                    break
                case _:
                    print("Opção inválida!")

        except ValueError:
            print("[ERRO]: Digite um número!")