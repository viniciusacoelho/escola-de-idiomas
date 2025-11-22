from banco_de_dados.bd import criar_conexao
from criptografar.criptografar import criptografar, checar_senha

def cadastrar_professor(nome_completo, email, cpf, numero_telefone, endereco, idioma_lecionado, senha):
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
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM professores_teste WHERE email = %s", (email,))
        professores_teste = cursor.fetchone()
    
        if professores_teste and checar_senha(senha, bytes(professores_teste[7])):
            return professores_teste
        return None
    
    except Exception as e:
        return f"[ERRO]: Falha ao autenticar e-mail e/ou senha: {e}"
    finally:
        cursor.close()
        conexao.close()

def inserir_professor(id_professor: int, parametro: str, atualizar: str, tipo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO professor_{tipo.lower()} VALUES (%s, %s)", (parametro, id_professor))
        conexao.commit()
        print(f"{tipo} inserido com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar professor: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_professores():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM professores_teste ORDER BY id_professor ASC")
        professores_teste = cursor.fetchall()
        return professores_teste
    except Exception as e:
        print(f"[ERRO]: Falha ao listar professor: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_professor(id_professor: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM professores_teste WHERE id_professor = %s", (id_professor,))
        turma = cursor.fetchall()
        print(f"Professor buscado com sucesso!")
        return turma
    except Exception as e:
        print(f"[ERRO]: Falha ao buscar professor: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_professor(id_professor: int, parametro: str, atualizar: str, tipo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        # TODO: Criptografar a senha modificada
        if tipo == "Senha":
            parametro == criptografar(parametro)
        
        cursor.execute(f"UPDATE professores_teste SET {atualizar} = %s WHERE id_professor = %s", (parametro, id_professor))
        print(f"{tipo} atualizado com sucesso!")
        conexao.commit()
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar professor: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_professor(id_professor):
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