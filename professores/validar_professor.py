import re

def validar_nome_completo(nome_completo: str) -> str:
    """
    Valida o nome completo do professor, verificando se está entre letras minúsculas ou maiúsculas, acentos, espaços e se é maior que 3 (tamanho mínimo).

    Args:
        nome_completo (str): Nome completo do professor.

    Returns:
        str: Nome completo inválido!
            Você digitou: 'nome_completo'
    """
    regex_nome_completo = r"^[a-zA-ZÀ-ÖØ-öø-ÿ ]{3,}$"
    if not re.match(regex_nome_completo, nome_completo):
        return f"Nome completo inválido!\nVocê digitou: {nome_completo}."

def validar_email(email: str) -> str:
    """
    Valida o e-mail do professor, verificando se está entre letras minúsculas ou maiúsculas, números, ponto, underline, porcentagem, mais ou menos, se possui arroba e ponto.

    Args
        email (str): E-mail do professor.

    Returns:
        str: E-mail inválido!
            Esperava-se: 'nome@dominio.com'.
    """
    regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(regex_email, email):
        return f"E-mail inválido!\nEsperava-se: 'nome@dominio.com'."

def validar_genero(genero: str) -> str:
    """
    Valida o gênero do professor.

    Args:
        genero (str): Gênero do professor. 

    Returns:
        str: Gênero inválido!
            Esperava-se 'M' ou 'F'.
    """
    if genero != "M" and genero != "F":
        return f"Gênero inválido! Esperava-se 'M' ou 'F'."

def validar_cpf(cpf: str) -> str:
    """
    Valida o CPF do professor, verificando se não é igual a 11 (tamanho fixo).

    Args:
        cpf (str): CPF do professor. 

    Returns:
        str: CPF inválido!
            Esperava-se: 'XXX.YYY.ZZZ.XY'.
    """
    TAMANHO_CPF = 11
    if len(cpf) != TAMANHO_CPF:
        return f"CPF inválido!\nEsperava-se: 'XXX.YYY.ZZZ.XY'."

def validar_numero_telefone(numero_telefone: str) -> str:
    """
    Valida o número de telefone do professor, verificando se não é igual a 11 (tamanho fixo).

    Args:
        numero_telefone (str): Número de telefone do professor. 

    Returns:
        str: Número de telefone inválido!
            Esperava-se: '+XX (XX) YYYYY-ZZZZ'.
    """
    TAMANHO_NUMERO_TELEFONE = 11
    if len(numero_telefone) != TAMANHO_NUMERO_TELEFONE:
        return f"Número de telefone inválido!\nEsperava-se: 'XXYYYYYZZZZ'."

def validar_endereco(endereco: str) -> str:
    """
    Valida o endereço do professor, verificando se não é igual a 11 (tamanho fixo).

    Args:
        endereco (str): Endereço do professor. 

    Returns:
        str: Endereço inválido!
    """
    TAMANHO_MINIMO_ENDERECO = 10
    if len(endereco) < TAMANHO_MINIMO_ENDERECO:
        return f"Endereço inválido!"

def validar_senha(senha: str) -> str:
    """
    Valida a senha do professor, verificando se ela possui pelo menos 8 caracteres.

    Args:
        senha (str): Senha do professor. 

    Returns:
        str: Senha inválida!
            A senha deve conter pelo menos 8 caracteres.
    """
    # TAMANHO_MINIMO_SENHA = 6
    TAMANHO_MINIMO_SENHA = 4
    if len(senha) < TAMANHO_MINIMO_SENHA:
        return "Senha inválida!\nA senha deve conter pelo menos 8 caracteres."