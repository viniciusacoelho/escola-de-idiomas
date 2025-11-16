# import re

# def validar_senha(senha: str) -> str:
#     regex_senha = r"^[\w0-9]+$"
#     if not re.match(regex_senha, senha):
#         return f"Senha inválida!"

# while True:
#     senha = input("Digite sua senha:\n")
#     erro_cpf = validar_senha(senha)
#     if erro_cpf:
#         print(erro_cpf)
#     else:
#         break

# opcoes = [
#     {1: 'Nome completo'},
#     {2: 'Usuário'},
#     {3: 'E-mail'}
# ]
# while True:
#     try:
#         opcao = int(input("Digite uma opção: "))
#         for opcao in opcoes:
#             print(f"{opcao[1]}")
#         break
#     except ValueError:
#         print("Digite um número!")

# while True:
#     cursos = listar_cursos()

#     if len(cursos) > 0:
#         try:
#             print("--------------------------------------------")
#             id_curso = int(input("Digite o ID do curso que deseja atualizar:\n"))
            
#             for curso in cursos:
#                 lista_cursos_cadastrados = []
#                 lista_cursos_cadastrados.append(curso[1])
                
#                 if id_curso == curso[0]:
#                     novo_nome_curso = input("Digite o novo nome do curso:\n")    

#                     if novo_nome_curso not in lista_cursos_cadastrados:
#                         atualizar_curso(id_curso, novo_nome_curso)
#                     else:
#                         print(f"Curso '{novo_nome_curso}' já cadastrado anteriormente.")
#                     break

#             else:
#                 print("ID do curso não cadastrado anteriormente.")
#             break

#         except ValueError:
#             print("[ERRO]: Digite um número!")
#             break

#     else:
#         print("Nenhum curso cadastrado anteriormente.")
#         break