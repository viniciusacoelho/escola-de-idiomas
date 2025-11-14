import re

def validar_nome_completo(nome_completo: str) -> str:
    """
    Valida o nome completo do aluno.

    Args:
        nome_completo (str): Nome completo do aluno.
        TAMANHO_MINIMO_NOME_COMPLETO: Tamanho mínimo do nome completo para ser válido.
    
    Returns:

    """
    TAMANHO_MINIMO_NOME_COMPLETO = 3
    if len(nome_completo) < TAMANHO_MINIMO_NOME_COMPLETO:
        return f"Nome completo inválido!\nVocê digitou: {nome_completo}"

# TODO: Verificar se há pessoas com o mesmo usuário porque ele é UNIQUE no BD
def validar_usuario(usuario: str) -> str:
    regex_usuario = r"^[a-z][a-z0-9._]+$"
    if not re.match(regex_usuario, usuario):
        return f"Usuário inválido! Você digitou: {usuario}"

# TODO: Verificar se há pessoas com o mesmo email porque ele é UNIQUE no BD
def validar_email(email: str) -> str:
    """
    Valida o e-mail do aluno.

    Args
        email (str): E-mail do aluno.
        regex_email (r): 

    Returns:


    """
    regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(regex_email, email):
        return f"E-mail inválido!\nEsperava-se: 'nome@dominio.com'"

# TODO: Verificar se há pessoas com o mesmo cpf porque ele é UNIQUE no BD
def validar_cpf(cpf: int) -> str:
    TAMANHO_CPF = 11
    if len(cpf) != TAMANHO_CPF:
        return f"CPF inválido!\nnEsperava-se: 'XXX.YYY.ZZZ.XY'"

def validar_data_nascimento(data_nascimento: int) -> str:
    TAMANHO_DATA_NASCIMENTO = 8
    if len(data_nascimento) != TAMANHO_DATA_NASCIMENTO:
        return f"Data de nascimento inválida!\nEsperava-se: 'DD/MM/AAAA'"

# TODO: Verificar se há pessoas com o mesmo telefone porque ele é UNIQUE no BD
def validar_numero_telefone(numero_telefone: str) -> str:
    TAMANHO_NUMERO_TELEFONE = 11
    if len(numero_telefone) != TAMANHO_NUMERO_TELEFONE:
        return f"Número de telefone inválido!\nEsperava-se: '+XX (XX) YYYYY-ZZZZ'"

def validar_senha(senha: str) -> str:
    regex_senha = r"^[\w0-9]+$"