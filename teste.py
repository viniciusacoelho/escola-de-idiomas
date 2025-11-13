import re

def validar_nome_completo(nome_completo: str) -> str:
    TAMANHO_MINIMO_NOME_COMPLETO = 3
    if len(nome_completo) < TAMANHO_MINIMO_NOME_COMPLETO:
        return f"Nome completo inválido!"

def validar_email(email: str) -> str:
    email_padrao = r"^[\w\.-]+@+[\w\.-]+\.\w+$"
    if not re.match(email_padrao, email):
        return "E-mail inválido!"

def validar_cpf(cpf: str) -> str:
    TAMANHO_CPF = 11
    if len(cpf) != TAMANHO_CPF:
        return f"CPF inválido!"

# while True:
#         nome_completo = input("Digite seu nome completo:\n")
#         erro_nome_completo = validar_nome_completo(nome_completo)
        
#         if erro_nome_completo:
#             print(erro_nome_completo)
#         else:
#             break

while True:
    email = input("Digite seu e-mail:\n").lower()
    erro_email = validar_email(email)  
    if erro_email:
        print(erro_email)
    else:
        break

# while True:
#     # TODO: Arrumar um jeito de colocar int e try/except e [ERRO]: Digite números!"
#     cpf = input("Digite seu CPF:\n")
#     erro_cpf = validar_cpf(cpf)
    
#     if erro_cpf:
#         print(erro_cpf)
#     else:
#         cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
#         print(cpf)
#         break

