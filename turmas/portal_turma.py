from limpar_tela.limpar_tela import limpar_tela
from professores.crud_professor import listar_professores
from professores.crud_professor import inserir_professor
from alunos.crud_aluno import listar_alunos 
from turmas.crud_turmas import inserir_turma, listar_turmas
from cursos.crud_cursos import listar_cursos 

from banco_de_dados.criar_conexao import criar_conexao

def professor_turma(id_turma: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT p.nome_completo FROM professor_turma pt INNER JOIN professores_teste p ON p.id_professor = pt.id_professor WHERE id_turma = %s", (id_turma,))
        # cursor.execute(f"SELECT {tabela[0]}.{atributo} FROM {tabela} att INNER JOIN alunos_teste a ON a.id_aluno = att.id_aluno WHERE id_turma = %s ORDER BY a.nome_completo ASC", (id_turma,))
        professor_turmas = cursor.fetchall()
        return professor_turmas
    except Exception as e:
        print(f"[ERRO]: Falha ao vizualizar professor da turma: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_professor_turma(id_professor: int):
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
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT a.nome_completo FROM aluno_turma att INNER JOIN alunos_teste a ON a.id_aluno = att.id_aluno WHERE id_turma = %s ORDER BY a.nome_completo ASC", (id_turma,))
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
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        # cursor.execute(f"SELECT {tabela[0]}.{atributo} FROM {tabela} att INNER JOIN alunos_teste a ON a.id_aluno = att.id_aluno WHERE id_turma = %s ORDER BY a.nome_completo ASC", (id_turma,))
        cursor.execute("SELECT c.nome_curso, t.dia_semana, t.horario FROM curso_turma ct INNER JOIN cursos_teste c ON c.id_curso = ct.id_curso INNER JOIN turmas_teste t ON t.id_turma = ct.id_turma WHERE t.id_turma = %s", (id_turma,))
        conexao.commit()
        alunos_turma = cursor.fetchall()
        return alunos_turma
    except Exception as e:
        print(f"[ERRO]: Falha ao vizualizar curso da turma: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_curso_turma(id_curso: int):
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
    menu = ["Vizualizar Turma", "Inserir Professor", "Deletar Professor", "Inserir Aluno", "Deletar Aluno", "Inserir Curso", "Deletar Curso", "Voltar"]

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
                            print(f"Curso: {curso[0]}")
                    else:
                        print("Nenhum curso cadastrado anteriormente na turma.")

                    professores = professor_turma(turma_autenticada[0])
                    
                    if len(professores) > 0:
                        for professor in professores:
                            print(f"Professor: {professor[0]}")
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
                            print(aluno[0])
                    else:
                        print("Nenhum aluno cadastrado anteriormente na turma.")
                    
                    if len(cursos) > 0:
                        for curso in cursos:
                            print(f"Dia/Horário: {curso[1]} ({curso[2]})")
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
                                        professores_turma = professor_turma(turma_autenticada[0])

                                        for professor_turmas in professores_turma:
                                            if id_professor == professor_turmas[0]:
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
                        professores = listar_professores()

                        if len(professores) > 0:
                            try:
                                id_professor = int(input("Digite o ID do professor que deseja deletar da turma:\n"))
                                for professor in professores:
                                    if id_professor == professor[0]:
                                        professores_turma = professor_turma(turma_autenticada[0])

                                        for professor_turmas in professores_turma:
                                            if id_professor == professor_turmas[0]:
                                                print("Professor já inserido na turma anteriormente.")
                                                break
                                        else:
                                            deletar_professor_turma(id_professor)
                                break

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                        
                        else:
                            print("Nenhum professor cadastrado anteriormente.")
                            break
                case 4:
                    while True:
                        alunos = listar_alunos()

                        for aluno in alunos:
                            print(f"{aluno[0]} - {aluno[1]}")

                        try:
                            id_aluno = int(input("Digite o id do aluno que deseja inserir na turma: \n"))
                            
                            # TODO: Verificar se o ID já foi cadastrado anteriormente
                            # TODO: Verificar se o ID já foi cadastrado anteriormente na turma
                            inserir_turma(turma_autenticada[0], id_aluno, "Aluno")
                            break

                        except ValueError:
                            print("[ERRO]: Digite apenas números!")
                            break
                    
                case 5:
                    while True:
                        alunos = listar_alunos()

                        if len(alunos) > 0:
                            try:

                                id_aluno = int(input("Digite o ID do aluno que deseja deletar da turma:\n"))
                                # TODO: Verificar se o ID já foi cadastrado anteriormente
                                # TODO: Verificar se o ID já foi cadastrado anteriormente na turma
                                deletar_aluno_turma(id_aluno)
                                break
                            except ValueError:
                                print("[ERRO]: Digite um número!")

                        else:
                            print("Nenhum aluno cadastrado anteriormente.")

                case 6:
                    while True:
                        cursos = listar_cursos()

                        if len(cursos) > 0:
                            for curso in cursos:
                                print(f"{curso[0]} - {curso[1]}")

                            try:
                                id_curso = int(input("Digite o id do curso que deseja inserir na turma: \n"))
                                # TODO: Verificar se o ID já foi cadastrado anteriormente
                                # TODO: Verificar se o ID já foi cadastrado anteriormente na turma
                                inserir_turma(turma_autenticada[0], id_curso, "Curso")
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
                                id_curso = int(input("Digite o ID do curso que deseja deletar da turma:\n"))
                                # TODO: Verificar se o ID já foi cadastrado anteriormente
                                # TODO: Verificar se o ID já foi cadastrado anteriormente na turma
                                deletar_curso_turma(id_curso)
                                break
                            except ValueError:
                                print("[ERRO]: Digite um número!")

                case 8:    
                    print("Voltando...")
                    break
                case _:
                    print("Digite uma opção válida!")

        except ValueError:
            print("[ERRO]: Digite um número!")