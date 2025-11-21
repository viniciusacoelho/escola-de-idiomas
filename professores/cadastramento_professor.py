import getpass

from limpar_tela.limpar_tela import limpar_tela
from professores.validar_professor import validar_nome_completo, validar_email, validar_senha, validar_cpf, validar_numero_telefone, validar_endereco, validar_idioma_lecionado
from professores.crud_professor import cadastrar_professor

def cadastramento_professor():
    limpar_tela()

    print("--------------------------------------------")
    print("            Cadastro - Professor            ")
    print("--------------------------------------------")

    while True:
        nome_completo = input("Digite o seu nome completo:\n")
        erro_nome_completo = validar_nome_completo(nome_completo)

        if erro_nome_completo:
            print(erro_nome_completo)
            print("--------------------------------------------\n")
        else:
            break

    while True:
        email = input("Digite o seu e-mail:\n")
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
            cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            break

    while True:
        numero_telefone = input("Digite o seu número de telefone:\n")
        erro_numero_telefone = validar_numero_telefone(numero_telefone)
        
        if erro_numero_telefone:
            print(erro_numero_telefone)
            print("--------------------------------------------\n")
        else:
            numero_telefone = f"({numero_telefone[:2]}) {numero_telefone[2:7]}-{numero_telefone[7:]}"
            break

    while True:
        endereco = input("Digite o seu endereço:\n")
        erro_endereco = validar_endereco(endereco)
        
        if erro_endereco:
            print(erro_endereco)
            print("--------------------------------------------\n")
        else:
            break

    while True:
        idioma_lecionado = input("Digite o idioma que você leciona:\n")
        erro_idioma_lecionado = validar_idioma_lecionado(idioma_lecionado)
        
        if erro_idioma_lecionado:
            print(erro_idioma_lecionado)
            print("--------------------------------------------\n")
        else:
            break

    while True:
        senha = getpass.getpass("Digite a sua senha:\n")
        erro_senha = validar_senha(senha)
        
        if erro_senha:
            print(erro_senha)
            print("--------------------------------------------\n")
        else:
            break

    while True:
        print("--------------------------------------------\n")
        confirmar_senha = getpass.getpass("Confirme sua senha:\n")
        
        if confirmar_senha != senha:
            print("Digite a mesma senha!")
        else:
            break

    cadastrar_professor(nome_completo, email, cpf, numero_telefone, endereco, idioma_lecionado, senha)