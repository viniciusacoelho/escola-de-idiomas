import getpass

from limpar_tela.limpar_tela import limpar_tela
from professores.validar_professor import validar_nome_completo, validar_email, validar_senha, validar_cpf, validar_numero_telefone, validar_endereco, validar_idioma_lecionado
from unique.verificar_unique import verificar_unique
from professores.crud_professor import cadastrar_professor
from cursos.crud_cursos import listar_cursos

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
        email = input("Digite seu e-mail:\n")
        erro_email = validar_email(email)

        if erro_email:
            print(erro_email)
            print("--------------------------------------------\n")
        else:
            erro_verificar_unique = verificar_unique("Professores", email, 2, "E-mail")
            
            if erro_verificar_unique:
                print(erro_verificar_unique)
            else:
                break

    while True:
        print("--------------------------------------------\n")
        cpf = input("Digite seu CPF:\n")
        
        try:
            int(cpf)
            erro_cpf = validar_cpf(cpf)
            
            if erro_cpf:
                print(erro_cpf)
            else:
                cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
                erro_verificar_unique = verificar_unique("Professores", cpf, 3, "CPF")

                if erro_verificar_unique:
                    print(erro_verificar_unique)
                else:
                    break

        except ValueError:
            print("[ERRO]: Digite apenas números!")

    while True:
        print("--------------------------------------------\n")
        numero_telefone = input("Digite seu número de telefone:\n")   
        
        try:
            int(numero_telefone)
            erro_numero_telefone = validar_numero_telefone(numero_telefone)
            
            if erro_numero_telefone:
                print(erro_numero_telefone)
            else:
                numero_telefone = f"({numero_telefone[:2]}) {numero_telefone[2:7]}-{numero_telefone[7:]}"
                erro_verificar_unique = verificar_unique("Professores", numero_telefone, 4, "Número de telefone")

                if erro_verificar_unique:
                    print(erro_verificar_unique)
                else:
                    break

        except ValueError:
            print("[ERRO]: Digite apenas números!")

    while True:
        endereco = input("Digite o seu endereço:\n")
        erro_endereco = validar_endereco(endereco)
        
        if erro_endereco:
            print(erro_endereco)
            print("--------------------------------------------\n")
        else:
            break

    while True:
        cursos = listar_cursos()

        if len(cursos) > 0:
            for curso in cursos:
                print(f"{curso[0]} - {curso[1]}")
            
            print("0 - Nenhuma das opções acima.")
            idioma_lecionado = input("Digite o idioma que você leciona:\n")
            
            if idioma_lecionado == "0":
                break

            erro_idioma_lecionado = validar_idioma_lecionado(idioma_lecionado)
            
            if erro_idioma_lecionado:
                print(erro_idioma_lecionado)
                print("--------------------------------------------\n")
            else:
                break
            
        
        else:
            print("--------------------------------------------\n")
            print("Nenhum idioma para lecionar cadastrado anteriormente.")
            break

    while True:
        print("--------------------------------------------\n")
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