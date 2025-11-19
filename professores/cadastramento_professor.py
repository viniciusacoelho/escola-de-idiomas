from professores.validar_professor import (
    validar_nome_completo, 
    validar_email, 
    validar_senha, 
    validar_cpf, 
    validar_numero_telefone, 
    validar_endereco, 
    validar_idioma_lecionado
)

def cadastramento_professor(): 
    print("--------------------------------------------")
    print("            Cadastro - Professor            ")
    print("--------------------------------------------")

    while True:
        nome_completo = input("Digite o seu nome completo: ")
        erro_nome_completo = validar_nome_completo(nome_completo)

        if erro_nome_completo:
            print(erro_nome_completo)
            print("--------------------------------------------\n")
        else:
            break

    while True:
        email = input("Digite o seu e-mail: ")
        erro_email = validar_email(email)
        
        if erro_email:
            print(erro_email)
            print("--------------------------------------------\n")
        else:
            break

    while True:
        cpf = input("Digite o seu CPF: ")
        erro_cpf = validar_cpf(cpf)
        
        if erro_cpf:
            print(erro_cpf)
            print("--------------------------------------------\n")
        else:
            break

    while True:
        numero_telefone = input("Digite o seu número de telefone: ")
        erro_numero_telefone = validar_numero_telefone(numero_telefone)
        
        if erro_numero_telefone:
            print(erro_numero_telefone)
            print("--------------------------------------------\n")
        else:
            break

    while True:
        endereco = input("Digite o seu endereço: ")
        erro_endereco = validar_endereco(endereco)
        
        if erro_endereco:
            print(erro_endereco)
            print("--------------------------------------------\n")
        else:
            break

    while True:
        idioma_lecionado = input("Digite o idioma que você leciona: ")
        erro_idioma_lecionado = validar_idioma_lecionado(idioma_lecionado)
        
        if erro_idioma_lecionado:
            print(erro_idioma_lecionado)
            print("--------------------------------------------\n")
        else:
            break

    while True:
        senha = input("Digite a sua senha: ")
        erro_senha = validar_senha(senha)
        
        if erro_senha:
            print(erro_senha)
            print("--------------------------------------------\n")
        else:
            break

    return nome_completo, email, senha, cpf, numero_telefone, endereco, idioma_lecionado