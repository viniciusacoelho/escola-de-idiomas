from limpar_tela.limpar_tela import limpar_tela
from professores.menu_atualizar_professor import menu_atualizar_professor
from turmas.crud_turmas import inserir_turma

from banco_de_dados.bd import criar_conexao

def professor_aluno(id_professor: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT a.nome_completo FROM professor_aluno pa INNER JOIN alunos_teste a ON a.id_aluno = pa.id_aluno WHERE id_professor = %s", (id_professor,))
        professor_alunos = cursor.fetchall()
        return professor_alunos
    except Exception as e:
        print(f"[ERRO]: Falha ao vizualizar alunos: {e}")
    finally:
        cursor.close()
        conexao.close()

def professor_turma(id_professor: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT t.id_turma, t.dia_semana, t.horario FROM professor_turma pt INNER JOIN turmas_teste t ON t.id_turma = pt.id_turma WHERE id_professor = %s", (id_professor,))
        professor_turmas = cursor.fetchall()
        return professor_turmas
    except Exception as e:
        print(f"[ERRO]: Falha ao vizualizar turmas: {e}")
    finally:
        cursor.close()
        conexao.close()

def professor_curso(id_professor: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT c.nome_curso FROM professor_curso pc INNER JOIN cursos_teste c ON c.id_curso = pc.id_curso WHERE id_professor = %s", (id_professor,))
        professor_cursos = cursor.fetchall()
        return professor_cursos
    except Exception as e:
        print(f"[ERRO]: Falha ao vizualizar cueso: {e}")
    finally:
        cursor.close()
        conexao.close()

def portal_professor(professor_autenticado):
    menu = ["Visualizar Turma", "Atualizar Cadastro", "Voltar"]
    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("              Escola de Idiomas             ")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    print(f"Turma {professor_turma(professor_autenticado[0])}:")
                    cursos = professor_curso(professor_autenticado[0])
                    
                    # if len(cursos) > 0:
                    for curso in cursos:
                        print(f"Curso: {curso[0]}")
                    # else:
                    #     print("Nenhum curso cadastrado anteriormente na turma.")

                    alunos = professor_aluno(professor_autenticado[0])

                    print("Alunos: ")

                    if len(alunos) > 0:
                        for aluno in alunos:
                            print(aluno[1])
                    print(f"Professor: {professor_autenticado[1]}")
                        # print("Você não foi cadastrado em nenhuma turma anteriormente.")
                    
                    for curso in cursos:
                        print(f"Horário: {curso[1]} ({curso[2]})")

                case 2:
                    menu_atualizar_professor(professor_autenticado[0])
                case 3:
                    print("Voltando...")
                    break

        except ValueError:
            print("[ERRO]: Digite um número!")