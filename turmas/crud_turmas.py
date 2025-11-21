from banco_de_dados.bd import criar_conexao

# def cadastrar_turma(id_professor, id_alunos, id_curso, dia_semana, horario):
def cadastrar_turma(dia_semana: str, horario: str):
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

# def autenticar_professor(email: str, senha: str):
#     try:
#         conexao = criar_conexao()
#         cursor = conexao.cursor()
#         cursor.execute("SELECT * FROM professores_teste WHERE email=%s", (email,))
#         professores_teste = cursor.fetchone()
    
#         if professores_teste and checar_senha(senha, bytes(professores_teste[7])):
#             print(f"E-mail '{email}' logado com sucesso!")
#             return professores_teste
#         return None
    
#     except Exception as e:
#         return f"[ERRO]: Falha ao autenticar e-mail e/ou senha: {e}"
#     finally:
#         cursor.close()
#         conexao.close()

def listar_turmas():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM turmas_teste ORDER BY id_turma ASC")
        turmas_teste = cursor.fetchall()
        return turmas_teste
    except Exception as e:
        print(f"[ERRO]: Falha ao listar turmas: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_turma(id_turma: int, parametro: str, atualizar: str, tipo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        cursor.execute(f"UPDATE turmas_teste SET {atualizar} = %s WHERE id_turma = %s", (parametro, id_turma))
        conexao.commit()
        print(f"{tipo} atualizado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar turma: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_turma(id_turma: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM turmas_teste WHERE id_turma = %s", (id_turma,))
        conexao.commit()
        print("Turma deletado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao deletar turma: {e}")
    finally:
        cursor.close()
        conexao.close()