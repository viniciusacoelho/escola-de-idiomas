import re

def validar_nome_completo(nome_completo: str) -> str:
    regex_nome_completo = r"^[a-zA-ZÀ-ÖØ-öø-ÿ ]{3,}$"
    if not re.match(regex_nome_completo, nome_completo):
        return f"Nome completo inválido!\nVocê digitou: {nome_completo}."

def validar_email(email: str) -> str:
    regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(regex_email, email):
        return f"E-mail inválido!\nEsperava-se: 'nome@dominio.com'."

def validar_cpf(cpf):
    TAMANHO_CPF = 11
    if len(cpf) != TAMANHO_CPF:
        return f"CPF inválido!\nEsperava-se: 'XXX.YYY.ZZZ.XY'."

def validar_numero_telefone(numero_telefone: str) -> str:
    TAMANHO_NUMERO_TELEFONE = 11
    if len(numero_telefone) != TAMANHO_NUMERO_TELEFONE:
        return f"Número de telefone inválido!\nEsperava-se: '+XX (XX) YYYYY-ZZZZ'."

def validar_endereco(endereco: str) -> str:
    pass

def validar_idioma_lecionado(idioma_lecionado: str) -> str:
    pass

def validar_senha(senha: str) -> str:
    # if len(senha) < 6:
    #     return "A senha deve ter pelo menos 8 caracteres."
    pass