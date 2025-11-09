from banco_de_dados.bd import criar_conexao

def cadastrar_curso(nome_curso: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO cursos_teste (nome_curso) VALUES (%s)", (nome_curso,))
        conexao.commit()
        print(f"Curso '{nome_curso}' cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar curso: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_cursos():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM cursos_teste")
        lista_cursos = cursor.fetchall()
        print("Cursos listados com sucesso!")
        print("--------------------------------------------")
        return lista_cursos
    except Exception as e:
        print(f"[ERRO]: Falha ao listar cursos: {e}")
    finally:
        cursor.close()
        conexao.close()
"""
def autenticar_curso(nome_curso: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("", (nome_curso,))
        print(f"Curso '{nome_curso}' autenticado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao autenticar curso: {e}")
    finally:
        cursor.close()
        conexao.close()
"""
def atualizar_curso(id_curso: int, nome_curso: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("UPDATE cursos_teste SET nome_curso = %s WHERE id_curso = %s", (nome_curso, id_curso))
        conexao.commit()
        print(f"Curso '{nome_curso}' atualizado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar curso: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_curso(id_curso: int):
# def deletar_curso(id_curso: int, nome_curso: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM cursos_teste WHERE id_curso = %s", (id_curso,))
        # TODO: Verificar se vai funcionar, porque o usuário não digita o nome do curso aqui
        # cursor.execute("DELETE FROM cursos_teste WHERE id_curso = %s AND nome_curso = %s", (id_curso, nome_curso))
        conexao.commit()
        print(f"Curso deletado com sucesso!")
        # print(f"Curso '{nome_curso}' deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar curso: {e}")
    finally:
        cursor.close()
        conexao.close()