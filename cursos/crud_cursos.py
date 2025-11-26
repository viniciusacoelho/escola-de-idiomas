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

def ja_matriculado(id_aluno, id_curso):
    """
        Cadastra o curso no banco de dados.

        Args:
            id_aluno (int): ID do aluno cadastrado no banco de dados.
            id_curso (int): ID do curso cadastrado no banco de dados.

        Raises:
            [ERRO]: Falha ao matricular aluno no curso.
    """
    try:
        coenxao = criar_conexao()
        cursor = coenxao.cursor()
        cursor.execute("SELECT * FROM aluno_curso WHERE id_aluno = %s AND id_curso = %s", (id_aluno, id_curso))
        aluno_curso = cursor.fetchall()
        return aluno_curso
    except Exception as e:
        print(f"[ERRO]: Falha ao matricular aluno no curso: {e}")
    finally:
        cursor.close()
        coenxao.close()

def matricular_aluno_curso(id_aluno: int, id_curso: int):
    """
        Permite o usuário escolher o curso que deseja se matricular.

        Args:
            id_aluno (int): ID do aluno cadastrado no banco de dados.
            id_curso (int): ID do curso cadastrado no banco de dados.
        
        Raises:
            [ERRO]: Falha ao escolher curso.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO aluno_curso (id_aluno, id_curso) VALUES (%s, %s)", (id_aluno, id_curso))
        print("Curso escolhido com sucesso!")
        # TODO: Tentar colocar o nome escolhido pelo aluno
        # print(f"Curso {nome} escolhido com sucesso!")
        conexao.commit()
    except Exception as e:
        print(f"[ERRO]: Falha ao escolher curso: {e}")
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
        cursor.execute("SELECT * FROM cursos_teste ORDER BY id_curso ASC")
        lista_cursos = cursor.fetchall()
        return lista_cursos
        # return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao listar cursos: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_curso(nome_curso: str):
    """
    Busca o curso cadastrado no banco de dados, mostrando todos os dados relacionados ao nome do curso.

    Args:
        nome_curso: Nome do curso cadastrado para busca.

    Raises:
        [ERRO]: Falha ao buscar aluno.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM cursos_teste WHERE nome_curso LIKE %s", (f"%{nome_curso}%",))
        cursos = cursor.fetchall()
        print(f"Curso '{nome_curso}' buscado com sucesso!")
        return cursos
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar curso: {e}")
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