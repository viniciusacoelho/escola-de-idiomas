import re

def validar_senha(senha: str) -> str:
    regex_senha = r"^[\w0-9]+$"
    if not re.match(regex_senha, senha):
        return f"Senha inválida!"

while True:
    senha = input("Digite sua senha:\n")
    erro_cpf = validar_senha(senha)
    if erro_cpf:
        print(erro_cpf)
    else:
        break