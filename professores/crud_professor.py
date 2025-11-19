from banco_de_dados.bd import criar_conexao

def cadastrar_professor(nome_completo, email, senha, cpf, numero_telefone, endereco, idioma_lecionado):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        # TODO: Criptografar
        cursor.execute("INSERT INTO professor (nome_completo, email, senha, cpf, numero_telefone, endereco, idioma_lecionado) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nome_completo, email, senha, cpf, numero_telefone, endereco, idioma_lecionado))
        conexao.commit()
        print("Professor cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar professor: {e}")
    finally:
        cursor.close()
        conexao.close()

def autenticar_professor():
    pass

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

def atualizar_professor(id_professor, nome_completo, email, senha, cpf, numero_telefone, endereco, idioma_lecionado):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        # TODO: Melhorar isso
        cursor.execute("UPDATE professor SET nome_completo = %s, email = %s, senha = %s, cpf = %s, numero_telefone = %s, endereco = %s, idioma_lecionado = %s WHERE id_professor = %s", (nome_completo, email, senha, cpf, numero_telefone, endereco, idioma_lecionado, id_professor))
        conexao.commit()
        print("Professor atualizado com sucesso!")
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