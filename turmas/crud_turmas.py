from banco_de_dados.bd import criar_conexao

def cadastrar_turma(dia_semana: str, horario: str):
    """
    Cadastra a turma no banco de dados.

    Args:
        dia_semana (str): Dia da semana da turma.
        horario (str): Horário da turma.

    Raises:
        [ERRO]: Falha ao cadastrar turma.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO turmas_teste (dia_semana, horario) VALUES (%s, %s)", (dia_semana, horario)) 
        conexao.commit()
        print("Turma cadastrada com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar turma: {e}")
    finally:
        cursor.close()
        conexao.close()

def autenticar_turma(id_turma: int):
    """
    Autentica o turma no banco de dados.

    Args:
        id_turma (int): ID da turma cadastrada no banco de dados.

    Returns:
        turma: Turma logada com sucesso!
        None: Turma não autenticada no banco de dados anteriormente.

    Raises:
        [ERRO]: Falha ao autenticar turma.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM turmas_teste WHERE id_turma = %s", (id_turma,))
        turma = cursor.fetchone()
        print(f"Turma '{id_turma}' logada com sucesso!")
        return turma
    except Exception as e:
        return f"[ERRO]: Falha ao autenticar turma: {e}"
    finally:
        cursor.close()
        conexao.close()

def inserir_turma(id_turma: int, parametro_atributo: str, entidade: str):
    """
    Insere a turma no banco de dados.

    Args:
        id_turma (int): ID da turma cadastrado no banco de dados.
        parametro_atributo (str): Parâmetro.

    Raises:
        [ERRO]: Falha ao inserir turma.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO {entidade.lower()}_turma VALUES (%s, %s)", (parametro_atributo, id_turma))
        conexao.commit()
        print(f"{entidade} inserido com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao inserir turma: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_turmas():
    """
    Lista as turmas cadastradas no banco de dados.

    Returns:
        turmas: Lista das turmas cadastrados no banco de dados.

    Raises:
        [ERRO]: Falha ao listar turmas.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM turmas_teste ORDER BY id_turma ASC")
        turmas = cursor.fetchall()
        return turmas
    except Exception as e:
        print(f"[ERRO]: Falha ao listar turmas: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_turma(id_turma: int):
    """ 
    Busca a turma cadastrada no banco de dados, mostrando todos os dados relacionados ao e-mail.

    Args:
        email (str): E-mail da turma cadastrada para busca.

    Raises:
        [ERRO]: Falha ao buscar turma.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM turmas_teste WHERE id_turma = %s", (id_turma,))
        turma = cursor.fetchall()
        print(f"Turma '{id_turma}' buscada com sucesso!")
        return turma
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar turma: {e}")
    finally:
        cursor.close()
        conexao.close()
    
def atualizar_turma(id_turma: int, parametro_atributo: str, atributo: str, nome_atributo: str):
    """
    Atualiza os dados da turma no banco de dados.

    Args:
        id_turma (int): ID da turma cadastrada no banco de dados.
        parametro_atributo (str): Parâmetro cadastrado que o turma deseja atualizar.
        atributo (str): O nome dos dados que o turma deseja atualizar.
        nome_atributo (str): O nome dos dados que o turma deseja atualizar para mensagem.

    Raises:
        [ERRO]: Falha ao atualizar turma.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE turmas_teste SET {atributo} = %s WHERE id_turma = %s", (parametro_atributo, id_turma))
        conexao.commit()
        print(f"{nome_atributo} atualizado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar turma: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_turma(id_turma: int):
    """
    Deleta a turma no banco de dados.

    Args:
        id_usuario (int): ID da turma cadastrada no banco de dados.
    
    Raises:
        [ERRO]: Falha ao deletar turma.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM turmas_teste WHERE id_turma = %s", (id_turma,))
        conexao.commit()
        print("Turma deletada com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar turma: {e}")
    finally:
        cursor.close()
        conexao.close()