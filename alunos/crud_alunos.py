from bando_de_dados.bd import criar_conexao

def cadastrar_aluno(nome, email, senha, telefone, curso):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, email) VALUES (%s, %s);", (nome, email, senha, telefone, curso))
        conexao.commit()
        print("Aluno cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_alunos(nome, email, senha, telefone, curso):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos;")
    lista_alunos = cursor.fetchall()
    return lista_alunos
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

def deletar_aluno(nome, email, senha, telefone, curso):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE from alunos WHERE id_usuario = %s AND nome = %s AND senha = %s AND telefone = %s AND curso = %s;", (nome, email, senha, telefone, curso))
        conexao.commit()
        print("Aluno deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()