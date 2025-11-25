from banco_de_dados.bd import criar_conexao

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

def autenticar_turma(id_turma: int):
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

def inserir_turma(id_turma: int, atributo: str, entidade: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO {entidade.lower()}_turma VALUES (%s, %s)", (atributo, id_turma))
        conexao.commit()
        print(f"{entidade} inserido com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar turma: {e}")
    finally:
        cursor.close()
        conexao.close()

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

def buscar_turma(id_turma: int):
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