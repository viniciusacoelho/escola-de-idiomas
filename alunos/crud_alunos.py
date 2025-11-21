from banco_de_dados.bd import criar_conexao
from criptografar.criptografar import criptografar, checar_senha

def cadastrar_aluno(nome_completo: str, usuario: str, email: str, cpf: str, data_nascimento: str, numero_telefone: str, senha: str):
    """
    Cadastra o aluno no banco de dados.

    Args:
        nome_completo (str): Nome completo do aluno.
        usuario (str): Usuário aluno.
        email (str): E-mail aluno.
        cpf (str): CPF do aluno.
        data_nascimento (str): Data de nascimento do aluno.
        numero_telefone (str): Número de telefone do aluno.
        senha (str): Senha do aluno.

    Raises:
        [ERRO]: Falha ao cadastrar aluno.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        senha = criptografar(senha)
        
        cursor.execute("INSERT INTO alunos_teste (nome_completo, usuario, email, cpf, data_nascimento, numero_telefone, senha) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nome_completo, usuario, email, cpf, data_nascimento, numero_telefone, senha))
        conexao.commit()
        print(f"Aluno '{nome_completo}' cadastrado com sucesso!")
        # TODO: Colocar somente o primeiro e último nome
        # nome = []
        # nome = nome_completo.split(" ")
        # print(f"Aluno '{nome[0]} {nome[-1]}' cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def autenticar_aluno(usuario: str, senha: str):
    """
    Autentica o aluno no banco de dados.

    Args:
        usuario (str): Usuário do aluno.
        senha (str): Senha do aluno.

    Returns:
        aluno: Aluno autenticado no banco de dados.
        None: Aluno não autenticado no banco de dados anteriormente.

    Raises:
        [ERRO]: Falha autenticar aluno.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos_teste WHERE usuario = %s", (usuario,))
        alunos_teste = cursor.fetchone()
        
        if alunos_teste and checar_senha(senha, bytes(alunos_teste[7])):
            # print(f"Usuário '{usuario}' logado com sucesso!")
            return alunos_teste
        return None
        
    except Exception as e:
        return f"[ERRO]: Falha ao logar usuário e/ou senha: {e}"
    finally:
        cursor.close()
        conexao.close()

def listar_alunos():
    """
    Lista os alunos cadastrados no banco de dados.

    Returns:
        lista_alunos: Lista dos alunos cadastrados no banco de dados.

    Raises:
        [ERRO]: Falha ao listar aluno.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos_teste ORDER BY id_aluno ASC")
        lista_alunos = cursor.fetchall()
        return lista_alunos
    except Exception as e:
        return f"[ERRO] ao listar alunos: {e}"
    finally:
        cursor.close()
        conexao.close()

def buscar_aluno(usuario: str):
    """ 
    Busca o aluno cadastrado no banco de dados, mostrando todos os dados relacionados ao usuário.

    Args:
        usuario: Usuário do aluno cadastrado para busca.

    Raises:
        [ERRO]: Falha ao buscar aluno.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos_teste WHERE usuario LIKE %s", (f"%{usuario}%",))
        aluno = cursor.fetchall()
        print(f"Usuário '{usuario}' buscado com sucesso!")
        return aluno
    except Exception as e:
        return f"[ERRO] ao buscar alunos: {e}"
    finally:
        cursor.close()
        conexao.close()

def atualizar_aluno(id_aluno: int, parametro: str, atualizar: str, tipo: str):
    """
    Atualiza os dados do aluno no banco de dados.

    Args:
        id_aluno (int): ID do aluno cadastrado no banco de dados.
        parametro (str): Parâmetro cadastrado que o aluno deseja atualizar.
        atualizar (str): O nome dos dados que o aluno deseja atualizar.
        tipo (str): O nome dos dados que o aluno deseja atualizar para mensagem.

    Raises:
        [ERRO]: Falha ao atualizar aluno.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        if tipo == "Senha":
            parametro = criptografar(parametro)

        cursor.execute(f"UPDATE alunos_teste SET {atualizar} = %s WHERE id_aluno = %s", (parametro, id_aluno))
        print(f"'{tipo}' de aluno atualizado com sucesso!")
        conexao.commit()
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_aluno(id_aluno: int, alunos: list):
    """
    Deleta o aluno no banco de dados.

    Args:
        id_usuario (int): ID do aluno cadastrado no banco de dados.
    
    Raises:
        [ERRO]: Falha ao deletar aluno.
    """
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE from alunos_teste WHERE id_aluno = %s", (id_aluno,))
        conexao.commit()
        # TODO: Verificar se tem como colocar o nome do aluno aqui:
        # print(f"Aluno '{alunos}' deletado com sucesso!")
        print(f"Aluno deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()