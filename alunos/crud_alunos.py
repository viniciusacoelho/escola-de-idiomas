from banco_de_dados.bd import criar_conexao
from criptografar.criptografar import criptografar, checar_senha

# TODO: Verificar se o aluno coloca o curso no cadastro ou se o 'adm' que coloca 
# def cadastrar_aluno(id_aluno: int, nome_completo: str, usuario: str, cpf: str, data_nascimento: str, numero_telefone: str, senha: str):
def cadastrar_aluno(nome_completo: str, usuario: str, email: str, cpf: str, data_nascimento: str, numero_telefone: str, senha: str):
    """
        Cadastra os alunos no banco de dados.

        Args:
            nome_completo (str): Nome completo digitado pelo aluno.
            usuario (str): Usuário digitado pelo aluno.
            email (str): E-mail digitado pelo aluno.

        Raises:
            [ERRO]: Falha ao cadastrar aluno.
    """
    
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        senha = criptografar(senha)
        
        # cursor.execute("INSERT INTO alunos_teste (id_aluno, nome_completo, usuario, cpf, data_nascimento, numero_telefone, senha) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id_aluno, nome_completo, usuario, cpf, data_nascimento, numero_telefone, senha))
        cursor.execute("INSERT INTO alunos_teste (nome_completo, usuario, email, cpf, data_nascimento, numero_telefone, senha) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nome_completo, usuario, email, cpf, data_nascimento, numero_telefone, senha))
        conexao.commit()
        print("Aluno cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def login(usuario: str, senha: str):
    # TODO: Verificar melhor os Returns
    """
    Loga os alunos no banco de dados.

    Args:
        usuario (str): Usuário digitado pelo aluno.
        senha (str): Senha digitada pelo aluno.

    Returns:
        aluno: Aluno logado no banco de dados
        None: Aluno não logado no banco de dados

    Raises:
        [ERRO]: Falha ao logar aluno.
    """

    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos_teste WHERE usuario = %s", (usuario,))
        aluno = cursor.fetchone
        
        if aluno and checar_senha(senha, bytes[aluno[8]]):
            print(f"Usuário '{usuario}' logado com sucesso!")
            return aluno
        return None
    
    except Exception as e:
        print(f"[ERRO]: Falha ao logar usuário: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_alunos():
    """
    Cadastra os alunos no banco de dados

    Returns:
        lista_alunos: Lista dos alunos cadastrados.

    Raises:
        [ERRO]: Falha ao cadastrar aluno.
    """

    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos_teste")
        lista_alunos = cursor.fetchall()
        print("--------------------------------------------")
        print(f"Alunos listados com sucesso!")
        return lista_alunos
    except Exception as e:
        print(f"[ERRO] ao listar alunos: {e}")
    finally:
        cursor.close()
        conexao.close()
"""
def autenticar_aluno():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("", ())
        pass
        conexao.commit()
        print("Aluno autenticado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()
"""
"""
def atualizar_curso(id_aluno, nome, email, senha, telefone, curso, opcao):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        if opcao == 1:
            cursor.execute("UPDATE alunos SET nome WHERE  = %s AND nome = %s;", (id_aluno, nome))
        elif opcao == 2:
            cursor.execute("UPDATE alunos SET email WHERE id_aluno = %s AND email = %s;", (id_aluno, email))
        elif opcao == 3:
            cursor.execute("UPDATE alunos SET senha WHERE id_aluno = %s AND senha = %s;", (id_aluno, senha))
        elif opcao == 4:
            cursor.execute("UPDATE alunos SET telefone WHERE id_aluno = %s AND telefone = %s;", (id_aluno, telefone))
        elif opcao == 5:
            cursor.execute("UPDATE alunos SET curso WHERE id_aluno = %s AND curso = %s;", (id_aluno, curso))
        conexao.commit()
        print("Aluno atualizado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()
"""
def atualizar_aluno():
    pass    

def deletar_aluno(id_aluno: int):
    """
    Deleta os alunos no banco de dados.

    Args:
        id_usuario (int): ID do usuário cadastrado no banco de dados.
    
    Raises:
        [ERRO]: Falha ao deletar aluno.
    """

    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE from alunos_teste WHERE id_aluno = %s", (id_aluno,))
        conexao.commit()
        # TODO: Verificar se tem como colocar o nome do aluno aqui:
        # print(f"Aluno '{nome_completo}' deletado com sucesso!")
        print("Aluno deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()