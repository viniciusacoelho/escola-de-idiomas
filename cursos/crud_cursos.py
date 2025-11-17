from banco_de_dados.bd import criar_conexao

def cadastrar_curso(nome_curso: str):
    """
        Cadastra o curso no banco de dados.

        Args:
            nome_curso (str): Nome do curso digitado pelo usuário.
        
        Raises:
            [ERRO]: Falha ao cadastrar curso.
    """
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
        cursor.execute("SELECT * FROM cursos_teste")
        lista_cursos = cursor.fetchall()
        return lista_cursos
        # return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar cursos: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_curso(busca_nome: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM cursos_teste WHERE nome_curso LIKE %s", (f"%{busca_nome}%",))
        cursos = cursor.fetchall()
        print(f"Curso '{busca_nome}' buscado com sucesso!")
        return cursos
    except Exception as e:
        print(f"[ERRO]: Falha ao bucar curso: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_curso(id_curso: int, novo_nome_curso: str):
    """
        Atualiza o curso cadastrado no banco de dados.

        Args:
            id_curso (int): ID do curso cadastrado no banco de dados.
            nome_curso (str): Nome do curso digitado pelo usuário.
        
        Raises:
            [ERRO]: Falha ao atualizar curso.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("UPDATE cursos_teste SET nome_curso = %s WHERE id_curso = %s", (novo_nome_curso, id_curso))
        conexao.commit()
        print(f"Curso '{novo_nome_curso}' atualizado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar curso: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_curso(id_curso: int):
# def deletar_curso(id_curso: int, nome_curso: str):
    """
        Deleta o curso cadastrado no banco de dados.

        Args:
            id_curso (int): ID do curso cadastrado no banco de dados.
        
        Raises:
            [ERRO]: Falha ao deletar curso.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        # cursor.execute("INSERT INTO lixeira-teste (nome) VALUES (%s)", (id_curso,))
        cursos = listar_cursos()
        # for curso in cursos:
        #     if id_curso == curso[0]:
        #         print(f"Curso '{curso[1]}' deletado com sucesso!")
        #     break
        cursor.execute("DELETE FROM cursos_teste WHERE id_curso = %s", (id_curso,))
        # TODO: Verificar se vai funcionar, porque o usuário não digita o nome do curso aqui
        # cursor.execute("DELETE FROM cursos_teste WHERE id_curso = %s AND nome_curso = %s", (id_curso, nome_curso))
        conexao.commit()
        print("Curso deletado com sucesso!")

        # print(f"Curso '{nome_curso}' deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar curso: {e}")
    finally:
        cursor.close()
        conexao.close()