from limpar_tela.limpar_tela import limpar_tela
from professores.crud_professor import listar_professores
from alunos.crud_aluno import listar_alunos 
from turmas.crud_turmas import inserir_turma
from cursos.crud_cursos import listar_cursos 

from banco_de_dados.criar_conexao import criar_conexao

def professor_turma(id_turma: int):
    """
    Relaciona o professor com a turma no banco de dados.

    Args:
        id_turma (int): ID da turma cadastrad no banco de dados.
    
    Raises:
        [ERRO]: Falha ao vizualizar professor da turma.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT p.id_professor, p.nome_completo FROM professor_turma pt INNER JOIN professores_teste p ON p.id_professor = pt.id_professor WHERE id_turma = %s", (id_turma,))
        # cursor.execute(f"SELECT {tabela[0]}.{atributo} FROM {tabela} att INNER JOIN alunos_teste a ON a.id_aluno = att.id_aluno WHERE id_turma = %s ORDER BY a.nome_completo ASC", (id_turma,))
        professor_turmas = cursor.fetchall()
        return professor_turmas
    except Exception as e:
        print(f"[ERRO]: Falha ao vizualizar professor da turma: {e}")
    finally:
        cursor.close()
        conexao.close()

def select_existe(id_turma: int, id_professor: int, entidade_atributo: str):
    """
    Relaciona o professor com a turma no banco de dados.

    Args:
        id_turma (int): ID da turma cadastrad no banco de dados.
    
    Raises:
        [ERRO]: Falha ao vizualizar professor da turma.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM {entidade_atributo}_turma WHERE id_turma = %s AND id_{entidade_atributo} = %s", (id_turma, id_professor))
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao vizualizar professor da turma: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_professor_turma(id_professor: int):
    """
    Deleta o professor da turma no banco de dados.

    Args:
        id_professor (int): ID do professor cadastrado no banco de dados.
    
    Raises:
        [ERRO]: Falha ao deletar turma.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE from professor_turma WHERE id_professor = %s", (id_professor,))
        conexao.commit()
        print("Professor deletado da turma com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar professor da turma: {e}")
    finally:
        cursor.close()
        conexao.close()

def aluno_turma(id_turma: int):
    """
    Relaciona o aluno com a turma no banco de dados.

    Args:
        id_turma (int): ID da turma cadastrada no banco de dados.
    
    Raises:
        [ERRO]: Falha ao vizualizar aluno da turma.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT a.id_aluno, a.nome_completo FROM aluno_turma att INNER JOIN alunos_teste a ON a.id_aluno = att.id_aluno WHERE id_turma = %s ORDER BY a.nome_completo ASC", (id_turma,))
        # cursor.execute(f"SELECT {tabela[0]}.{atributo} FROM aluno_turma att INNER JOIN {tabela} a ON {tabela[0]}.{id_entidade} = att.{id_entidade} WHERE id_turma = %s ORDER BY {tabela}.{atributo} ASC", (id_turma,))
        # cursor.execute(f"SELECT {tabela[0]}.{atributo} FROM {tabela} att INNER JOIN alunos_teste a ON a.id_aluno = att.id_aluno WHERE id_turma = %s ORDER BY a.nome_completo ASC", (id_turma,))
        # cursor.execute(f"SELECT {tabela[0]}.{atributo} FROM {tabela} att INNER JOIN alunos_teste a ON a.id_aluno = att.id_aluno WHERE id_turma = %s ORDER BY a.nome_completo ASC", (id_turma,))
        alunos_turma = cursor.fetchall()
        return alunos_turma
    except Exception as e:
        print(f"[ERRO]: Falha ao vizualidar alunos da turma: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_aluno_turma(id_aluno: int):
    """
    Deleta o aluno da turma no banco de dados.

    Args:
        id_aluno (int): ID do aluno cadastrado no banco de dados.
    
    Raises:
        [ERRO]: Falha ao deletar aluno da turma.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE from aluno_turma WHERE id_aluno = %s", (id_aluno,))
        conexao.commit()
        print("Aluno deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar aluno da turma: {e}")
    finally:
        cursor.close()
        conexao.close()

def curso_turma(id_turma: int):
    """
    Relaciona o curso com a turma no banco de dados.

    Args:
        id_turma (int): ID da turma cadastrada no banco de dados.
    
    Raises:
        [ERRO]: Falha ao vizualizar curso da turma.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        # cursor.execute(f"SELECT {tabela[0]}.{atributo} FROM {tabela} att INNER JOIN alunos_teste a ON a.id_aluno = att.id_aluno WHERE id_turma = %s ORDER BY a.nome_completo ASC", (id_turma,))
        cursor.execute("SELECT c.id_curso, c.nome_curso, t.dia_semana, t.horario FROM curso_turma ct INNER JOIN cursos_teste c ON c.id_curso = ct.id_curso INNER JOIN turmas_teste t ON t.id_turma = ct.id_turma WHERE t.id_turma = %s", (id_turma,))
        conexao.commit()
        alunos_turma = cursor.fetchall()
        return alunos_turma
    except Exception as e:
        print(f"[ERRO]: Falha ao vizualizar curso da turma: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_curso_turma(id_curso: int):
    """
    Deleta o curso da turma no banco de dados.

    Args:
        id_curso (int): ID do curso cadastrado no banco de dados.
    
    Raises:
        [ERRO]: Falha ao deletar curso da turma.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE from curso_turma WHERE id_curso = %s", (id_curso,))
        conexao.commit()
        print("Curso deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar curso da turma: {e}")
    finally:
        cursor.close()
        conexao.close()

def portal_turma(turma_autenticada):
    """
    Página do portal da turma.
    
    Args:
        turma_autenticada (db): Todos os dados cadastrados da turma autenticada.
    """
    menu = ["Vizualizar Turma", "Inserir Professor", "Deletar Professor", "Inserir Aluno", 
            "Deletar Aluno", "Inserir Curso", "Deletar Curso", "Voltar"]

    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("                Login Turma                 ")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    print(f"Turma {turma_autenticada[0]}:")
                    cursos = curso_turma(turma_autenticada[0])

                    if len(cursos) > 0:
                        for curso in cursos:
                            print(f"Curso: {curso[1]}")
                    else:
                        print("Nenhum curso cadastrado anteriormente na turma.")

                    professores = professor_turma(turma_autenticada[0])
                    
                    if len(professores) > 0:
                        for professor in professores:
                            print(f"Professor: {professor[1]}")
                    else:
                        print("Professor:\nNenhum professor cadastrado anteriormente na turma.")
                    
                    print("Alunos:")
                    alunos = aluno_turma(turma_autenticada[0])
                    # TODO: Verificar se tem como fazer assim, para não criar várias funções
                    # alunos = aluno_turma(turma_autenticada[0], "id_aluno", "alunos_teste", "nome_completo")

                    if len(alunos) > 0:
                        # TODO: Verificar se isso funciona, ele insere o professor na tabela 'professor_aluno' se e somente se
                        #       os alunos estiverem matriculados/listados na turma
                        # inserir_professor(id_professor, id_aluno, "aluno")
                        for aluno in alunos:
                            print(aluno[1])
                    else:
                        print("Nenhum aluno cadastrado anteriormente na turma.")
                    
                    if len(cursos) > 0:
                        for curso in cursos:
                            print(f"Dia/Horário: {curso[2]} ({curso[3]})")
                    else:
                        print("Nenhum curso cadastrado anteriormente na turma.")

                case 2:
                    while True:
                        professores = listar_professores()

                        if len(professores) > 0:
                            for professor in professores:
                                
                                print(f"{professor[0]} - {professor[1]}")

                            try:
                                id_professor = int(input("Digite o id do professor que deseja inserir na turma:\n"))
                                professor_turma(turma_autenticada[0])

                                for professor in professores:
                                    if id_professor == professor[0]:
                                        professores_turma = select_existe(turma_autenticada[0], id_professor, "professor")

                                        for professor_turmas in professores_turma:
                                            if id_professor == professor_turmas[0] and turma_autenticada[0] == professor_turmas[1]:
                                                print("Professor já inserido na turma anteriormente.")
                                                break
                                        else:
                                            inserir_turma(turma_autenticada[0], id_professor, "Professor")
                                        break

                                else:
                                    print("ID do professor inválido!")
                                break

                            except ValueError:
                                print("[ERRO]: Digite apenas números!")
                                break

                        else:
                            print("Nenhum professor cadastrado anteriormente.")
                            break

                case 3:
                    while True:
                        lista_professores = listar_professores()
                        
                        if len(lista_professores) > 0:
                            try:
                                professores = professor_turma(turma_autenticada[0])
                                
                                for professor in professores:
                                    print(f"{professor[0]} - {professor[1]}")
                                    
                                id_professor = int(input("Digite o ID do professor que deseja deletar da turma:\n"))
                                
                                for professor in professores:
                                    if id_professor == professor[0]:
                                        professores_turma = professor_turma(turma_autenticada[0])

                                        for professor_turmas in professores_turma:
                                            if id_professor == professor_turmas[0]:
                                                deletar_professor_turma(id_professor)
                                                break
                                        else:
                                            print("Professor não inserido na turma anteriormente.")
                                        break

                                else:
                                    print("Professor não cadastrado anteriormente.")
                                break

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break
                        
                        else:
                            print("Nenhum professor cadastrado anteriormente.")
                            break

                case 4:
                    while True:
                        alunos = listar_alunos()
                        if len(alunos) > 0:

                            for aluno in alunos:
                                print(f"{aluno[0]} - {aluno[1]}")

                            try:
                                id_aluno = int(input("Digite o id do aluno que deseja inserir na turma: \n"))
                                
                                for aluno in alunos:
                                    if id_aluno == aluno[0]:
                                        alunos_turma = select_existe(turma_autenticada[0], id_aluno, "aluno")

                                        for aluno_turmas in alunos_turma:
                                            if id_aluno == aluno_turmas[0] and turma_autenticada[0] == aluno_turmas[1]:
                                                print("Aluno já inserido na turma anteriormente.")
                                                break
                                        else:
                                            inserir_turma(turma_autenticada[0], id_aluno, "Aluno")
                                        break

                                else:
                                    print("ID do aluno inválido!")
                                break

                            except ValueError:
                                print("[ERRO]: Digite apenas números!")
                                break
                        else:
                            print("Nenhum aluno cadastrado anteriormente.")
                            break

                case 5:
                    while True:
                        lista_alunos = listar_alunos()

                        if len(lista_alunos) > 0:
                            try:
                                alunos = aluno_turma(turma_autenticada[0])

                                for aluno in alunos:
                                    # TODO: ORDER BY id_aluno
                                    print(f"{aluno[0]} - {aluno[1]}")
                                    
                                id_aluno = int(input("Digite o ID do aluno que deseja deletar da turma:\n"))
                                
                                for aluno in alunos:
                                    if id_aluno == aluno[0]:
                                        alunos_turma = aluno_turma(turma_autenticada[0])

                                        for aluno_turmas in alunos_turma:
                                            if id_aluno == aluno_turmas[0]:
                                                deletar_aluno_turma(id_aluno)
                                                break
                                        else:
                                            print("Aluno não inserido na turma anteriormente.")
                                        break

                                else:
                                    print("Aluno não cadastrado anteriormente.")
                                break

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break

                        else:
                            print("Nenhum aluno cadastrado anteriormente.")
                            break

                case 6:
                    while True:
                        cursos = listar_cursos()

                        if len(cursos) > 0:
                            for curso in cursos:
                                print(f"{curso[0]} - {curso[1]}")

                            try:
                                # TODO: Uma turma não pode ter dois cursos
                                id_curso = int(input("Digite o id do curso que deseja inserir na turma:\n"))
                                for curso in cursos:
                                    if id_curso == curso[0]:
                                        cursos_turma = select_existe(turma_autenticada[0], id_curso, "curso")

                                        for curso_turmas in cursos_turma:
                                            if id_curso == curso_turmas[0] and turma_autenticada[0] == curso_turmas[1]:
                                                print("Curso já inserido na turma anteriormente.")
                                                break
                                        else:
                                            inserir_turma(turma_autenticada[0], id_curso, "Curso")
                                        break

                                else:
                                    print("ID do curso inválido!")
                                break

                            except ValueError:
                                print("[ERRO]: Digite apenas números!")
                                break

                        else:
                            print("Nenhum curso cadastrado anteriormente.")

                case 7:
                    while True:
                        cursos = listar_cursos()

                        if len(cursos) > 0:
                            try:
                                cursos = curso_turma(turma_autenticada[0])

                                for curso in cursos:
                                    print(f"{curso[0]} - {curso[1]}")
                                
                                id_curso = int(input("Digite o ID do curso que deseja deletar da turma:\n"))
                                                                    
                                for curso in cursos:
                                    if id_curso == curso[0]:
                                        cursos_turma = curso_turma(turma_autenticada[0])

                                        for curso_turmas in cursos_turma:
                                            if id_curso == curso_turmas[0]:
                                                deletar_curso_turma(id_curso)
                                                break
                                        else:
                                            print("Curso não inserido na turma anteriormente.")
                                        break

                                else:
                                    print("Curso não cadastrado anteriormente.")
                                break
                                
                            except ValueError:
                                print("[ERRO]: Digite um número!")

                        else:
                            print("Nenhum curso cadastrado anteriormente.")

                case 8:    
                    print("Voltando...")
                    break
                case _:
                    print("Digite uma opção válida!")

        except ValueError:
            print("[ERRO]: Digite um número!")