def validar_nome_completo(nome_completo: str) -> str:
    TAMANHO_MINIMO_NOME_COMPLETO = 3
    if len(nome_completo) < TAMANHO_MINIMO_NOME_COMPLETO:
        return f"Nome completo inválido!"
    return f"Bem-vindo {nome_completo[0]} {nome_completo[-1]}"
def validar_cpf(cpf: int) -> str:
    TAMANHO_CPF = 11
    cpf_modificado = str(cpf)
    if len(cpf_modificado) != TAMANHO_CPF:
        return f"CPF inválido!"
    return f"{cpf_modificado[:3]}.{cpf_modificado[3:6]}.{cpf_modificado[6:9]}-{cpf_modificado[9:]}"

def validar_data_nascimento(data_nascimento: int) -> str:
    TAMANHO_DATA_NASCIMENTO = 8
    data_nascimento_modificado = str(data_nascimento)
    if len(data_nascimento_modificado) != TAMANHO_DATA_NASCIMENTO:
        return f"Data de nascimento inválida!"
    return f"{data_nascimento_modificado[:2]}/{data_nascimento_modificado[2:4]}/{data_nascimento_modificado[4:]}"

def validar_numero_telefone(numero_telefone: int) -> str:
    TAMANHO_NUMERO_TELEFONE = 11
    numero_telefone_modificado = str(numero_telefone)
    if len(numero_telefone_modificado) != TAMANHO_NUMERO_TELEFONE:
        return f"Número de telefone inválido!"
    return f"({numero_telefone_modificado[:2]}) {numero_telefone_modificado[2:7]}-{numero_telefone_modificado[7:]}"