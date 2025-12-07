import re

def validar_nome_completo(nome_completo: str) -> str:
    """
    Valida o nome completo do aluno, verificando se está entre letras minúsculas ou maiúsculas, acentos, espaços e se é maior que 3 (tamanho mínimo).

    Args:
        nome_completo (str): Nome completo do aluno.

    Returns:
        str: Nome completo inválido!
            Você digitou: 'nome_completo'
    """
    regex_nome_completo = r"^[a-zA-ZÀ-ÖØ-öø-ÿ ]{3,}$"
    if not re.match(regex_nome_completo, nome_completo):
        return f"Nome completo inválido!\nVocê digitou: {nome_completo}."

def validar_usuario(usuario: str) -> str:
    """
    Valida o usuário do aluno, verificando se está entre letras minúsculas ou maiúsculas, números, ponto e underline.

    Args:
        usuario (str): Usuário do aluno.

    Returns:
        str: Usuário inválido!
            Você digitou: 'usuario'.
    """
    regex_usuario = r"^[a-z0-9_][a-z0-9._]+$"
    if not re.match(regex_usuario, usuario):
        return f"Usuário inválido! Você digitou: {usuario}."

def validar_email(email: str) -> str:
    """
    Valida o e-mail do aluno, verificando se está entre letras minúsculas ou maiúsculas, números, ponto, underline, porcentagem, mais ou menos, se possui arroba e ponto.

    Args
        email (str): E-mail do aluno.

    Returns:
        str: E-mail inválido!
            Esperava-se: 'nome@dominio.com'.
    """
    regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(regex_email, email):
        return f"E-mail inválido!\nEsperava-se: 'nome@dominio.com'."

def validar_cpf(cpf: str) -> str:
    """
    Valida o CPF do aluno, verificando se não é igual a 11 (tamanho fixo).

    Args:
        cpf (str): CPF do aluno. 

    Returns:
        str: CPF inválido!
            Esperava-se: 'XXX.YYY.ZZZ.XY'.
    """
    TAMANHO_CPF = 11
    if len(cpf) != TAMANHO_CPF:
        return f"CPF inválido!\nEsperava-se: 'XXXYYYZZZXY'."

def validar_data_nascimento(data_nascimento: str) -> str:
    """
    Valida a data de nascimento do aluno, verificando se não é igual a 8 (tamanho fixo).

    Args:
        data_nascimento (str): Data de nascimento do aluno. 

    Returns:
        str: Data de nascimento inválida!
            Esperava-se: 'DD/MM/AAAA'.
    """
    TAMANHO_DATA_NASCIMENTO = 8
    if len(data_nascimento) != TAMANHO_DATA_NASCIMENTO:
        return f"Data de nascimento inválida!\nEsperava-se: 'DDMMAAAA'."

def validar_numero_telefone(numero_telefone: str) -> str:
    """
    Valida o número de telefone do aluno, verificando se não é igual a 11 (tamanho fixo).

    Args:
        numero_telefone (str): Número de telefone do aluno. 

    Returns:
        str: Número de telefone inválido!
            Esperava-se: '+XX (XX) YYYYY-ZZZZ'.
    """
    TAMANHO_NUMERO_TELEFONE = 11
    if len(numero_telefone) != TAMANHO_NUMERO_TELEFONE:
        return f"Número de telefone inválido!\nEsperava-se: 'XXYYYYYZZZZ'."

def validar_senha(senha: str) -> str:
    """
    Valida a senha do aluno, verificando se ela possui pelo menos 8 caracteres.

    Args:
        senha (str): Senha do aluno. 

    Returns:
        str: Senha inválida!
            A senha deve conter pelo menos 8 caracteres.
    """
    TAMANHO_MINIMO_SENHA = 8
    if len(senha) < TAMANHO_MINIMO_SENHA:
        return "Senha inválida!\nA senha deve conter pelo menos 8 caracteres."