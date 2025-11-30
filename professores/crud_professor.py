from banco_de_dados.criar_conexao import criar_conexao
from criptografar.criptografar import criptografar, checar_senha

def cadastrar_professor(nome_completo, email, cpf, numero_telefone, endereco, idioma_lecionado, senha):
    """
    Cadastra o professor no banco de dados.

    Args:
        nome_completo (str): Nome completo do professor.
        usuario (str): Usuário professor.
        email (str): E-mail professor.
        cpf (str): CPF do professor.
        numero_telefone (str): Número de telefone do professor.
        endereco (str): Endereço do professor.
        idioma_lecionado (str): Idioma lecionado do professor.
        senha (str): Senha do professor.

    Raises:
        [ERRO]: Falha ao cadastrar professor.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        senha = criptografar(senha)

        cursor.execute("INSERT INTO professores_teste (nome_completo, email, cpf, numero_telefone, endereco, idioma_lecionado, senha) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nome_completo, email, cpf, numero_telefone, endereco, idioma_lecionado, senha))
        conexao.commit()
        print(f"Professor '{nome_completo}' cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar professor: {e}")
    finally:
        cursor.close()
        conexao.close()

def autenticar_professor(email: str, senha: str):
    """
    Autentica o professor no banco de dados.

    Args:
        email (str): E-mail do professor.
        senha (str): Senha do professor.

    Returns:
        professor: professor autenticado no banco de dados.
        None: professor não autenticado no banco de dados anteriormente.

    Raises:
        [ERRO]: Falha ao autenticar professor.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM professores_teste WHERE email = %s", (email,))
        professores = cursor.fetchone()

        if professores and checar_senha(senha, bytes(professores[7])):
            return professores
        return None

    except Exception as e:
        return f"[ERRO]: Falha ao autenticar professor: {e}"
    finally:
        cursor.close()
        conexao.close()

def inserir_professor(id_professor: int, parametro_atributo: str, entidade: str):
    """
    Insere o professor no banco de dados.

    Args:
        id_professor (int): ID do professor cadastrado no banco de dados.
        parametro_atributo (str): Senha do professor.

    Raises:
        [ERRO]: Falha ao inserir professor.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO professor_{entidade.lower()} VALUES (%s, %s)", (parametro_atributo, id_professor))
        conexao.commit()
        print(f"{entidade} inserido com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar professor: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_professores():
    """
    Lista os professores cadastrados no banco de dados.

    Returns:
        professores: Lista dos professores cadastrados no banco de dados.

    Raises:
        [ERRO]: Falha ao listar professor.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM professores_teste ORDER BY id_professor ASC")
        professores = cursor.fetchall()
        return professores
    except Exception as e:
        print(f"[ERRO]: Falha ao listar professor: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_professor(email: str):
    """ 
    Busca o professor cadastrado no banco de dados, mostrando todos os dados relacionados ao e-mail.

    Args:
        email (str): E-mail do professor cadastrado para busca.

    Raises:
        [ERRO]: Falha ao buscar professor.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM professores_teste WHERE email LIKE %s", (f"%{email}%",))
        turma = cursor.fetchall()
        print(f"Professor buscado com sucesso!")
        return turma
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar professor: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_professor(id_professor: int, parametro_atributo: str, atributo: str, nome_atributo: str):
    """
    Atualiza os dados do professor no banco de dados.

    Args:
        id_professor (int): ID do professor cadastrado no banco de dados.
        parametro_atributo (str): Parâmetro cadastrado que o professor deseja atualizar.
        atributo (str): O nome dos dados que o professor deseja atualizar.
        nome_atributo (str): O nome dos dados que o professor deseja atualizar para mensagem.

    Raises:
        [ERRO]: Falha ao atualizar professor.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        if atributo == "senha":
            parametro = criptografar(parametro)
        
        cursor.execute(f"UPDATE professores_teste SET {atributo} = %s WHERE id_professor = %s", (parametro_atributo, id_professor))
        print(f"{nome_atributo} atualizado com sucesso!")
        conexao.commit()
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar professor: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_professor(id_professor):
    """
    Deleta o professor no banco de dados.

    Args:
        id_usuario (int): ID do professor cadastrado no banco de dados.
    
    Raises:
        [ERRO]: Falha ao deletar professor.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM professor WHERE id_professor = %s", (id_professor,))
        conexao.commit()
        print("Professor deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar professor: {e}")
    finally:
        cursor.close()
        conexao.close()

def cadastrar_curso_professor(nome_curso: str):
    pass