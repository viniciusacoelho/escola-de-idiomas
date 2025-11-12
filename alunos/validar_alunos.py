def validar_nome_completo(nome_completo: str) -> str:
    TAMANHO_MINIMO_NOME_COMPLETO = 3
    if len(nome_completo) < TAMANHO_MINIMO_NOME_COMPLETO:
        # TODO: Colocar isso para todos de vc digitou
        return f"Nome completo inválido!\nVocê digitou: {nome_completo}"

# TODO: Verificar se há pessoas com o mesmo usuário porque ele é UNIQUE no BD
def validar_usuario(usuario: str) -> str:
    pass

# TODO: Verificar se há pessoas com o mesmo email porque ele é UNIQUE no BD
# TODO: Pesquisar sobre REGEX
def validar_email(email: str) -> str: # REGEX
    # TODO: split()
    if "@" not in email and "." not in email:
        return f"E-mail inválido!\nVocê digitou: {email}"

# TODO: Verificar se há pessoas com o mesmo cpf porque ele é UNIQUE no BD
def validar_cpf(cpf: int) -> str:
    TAMANHO_CPF = 11
    if len(cpf) != TAMANHO_CPF:
        return f"CPF inválido!\nVocê digitou: {cpf}"
    # return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    # cpf_modificado = str(cpf)
    # if len(cpf_modificado) != TAMANHO_CPF:
    #     return f"CPF inválido!"
    # return f"{cpf_modificado[:3]}.{cpf_modificado[3:6]}.{cpf_modificado[6:9]}-{cpf_modificado[9:]}"

def validar_data_nascimento(data_nascimento: int) -> str:
    TAMANHO_DATA_NASCIMENTO = 8
    if len(data_nascimento) != TAMANHO_DATA_NASCIMENTO:
        return f"Data de nascimento inválida!\nVocê digitou: {data_nascimento}"
    # return f"{data_nascimento[:2]}/{data_nascimento[2:4]}/{data_nascimento[4:]}"
    # data_nascimento_modificado = str(data_nascimento)
    # if len(data_nascimento_modificado) != TAMANHO_DATA_NASCIMENTO:
    #     return f"Data de nascimento inválida!"
    # return f"{data_nascimento_modificado[:2]}/{data_nascimento_modificado[2:4]}/{data_nascimento_modificado[4:]}"

# TODO: Verificar se há pessoas com o mesmo telefone porque ele é UNIQUE no BD
def validar_numero_telefone(numero_telefone: int) -> str:
    TAMANHO_NUMERO_TELEFONE = 11
    numero_telefone_modificado = str(numero_telefone)
    if len(numero_telefone_modificado) != TAMANHO_NUMERO_TELEFONE:
        return f"Número de telefone inválido!\nVocê digitou: {numero_telefone}"
    # return
    # TODO: Verificar se precisa disso
    # print(f"+{numero_telefone_modificado[:2]} ({numero_telefone_modificado[2:4]}) {numero_telefone_modificado[4]} {numero_telefone_modificado[5:9]}-{numero_telefone_modificado[9:13]}")

def validar_senha(senha: str) -> str:
    pass