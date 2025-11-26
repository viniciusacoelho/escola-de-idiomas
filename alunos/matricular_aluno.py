import getpass
from limpar_tela.limpar_tela import limpar_tela
from alunos.validar_alunos import validar_nome_completo, validar_usuario, validar_email, validar_cpf, validar_data_nascimento, validar_numero_telefone, validar_senha
from alunos.crud_aluno import cadastrar_aluno
from unique.verificar_unique import verificar_unique

def matricular_aluno():
    """Cadastra os dados do aluno no banco de dados com uma série de informações."""
    limpar_tela()

    print("--------------------------------------------")
    print("                  Matrícula")
    print("--------------------------------------------")
    print("Matricule-se\n")

    while True:
        nome_completo = input("Digite seu nome completo:\n")
        erro_nome_completo = validar_nome_completo(nome_completo)

        if erro_nome_completo:
            print(erro_nome_completo)
            print("--------------------------------------------\n")
        else:
            break

    while True:
        print("--------------------------------------------\n")
        usuario = input("Digite seu usuário:\n").lower()
        erro_usuario = validar_usuario(usuario)

        if erro_usuario:
            print(erro_usuario)
        else:
            erro_verificar_unique = verificar_unique("Alunos", usuario, 2, "Usuário")

            if erro_verificar_unique:
                print(erro_verificar_unique)
            else:
                break

    while True:
        print("--------------------------------------------\n")
        email = input("Digite seu e-mail:\n").lower()
        erro_email = validar_email(email)

        if erro_email:
            print(erro_email)
        else:
            erro_verificar_unique = verificar_unique("Alunos", email, 3, "E-mail")

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
                erro_verificar_unique = verificar_unique("Alunos", cpf, 4, "CPF")

                if erro_verificar_unique:
                    print(erro_verificar_unique)
                else:
                    break

        except ValueError:
            print("[ERRO]: Digite apenas números!")

    while True:
        print("--------------------------------------------\n")
        data_nascimento = input("Digite sua data de nascimento:\n")

        try:
            int(data_nascimento)
            erro_data_nascimento =  validar_data_nascimento(data_nascimento)

            if erro_data_nascimento:
                print(erro_data_nascimento)
            else:
                data_nascimento = f"{data_nascimento[:2]}-{data_nascimento[2:4]}-{data_nascimento[4:]}"
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
                erro_verificar_unique = verificar_unique("Alunos", numero_telefone, 6, "Número de telefone")

                if erro_verificar_unique:
                    print(erro_verificar_unique)
                else:
                    break

        except ValueError:
            print("[ERRO]: Digite apenas números!")

    while True:
        print("--------------------------------------------\n")
        senha = getpass.getpass("Digite sua senha:\n")
        # TODO:
        # erro_senha = validar_senha(senha)
        
        # if erro_senha:
        #     print(erro_senha)
        # else:
        #     senha_validada = erro_senha
        #     break
        break

    while True:
        print("--------------------------------------------\n")
        confirmar_senha = getpass.getpass("Confirme sua senha:\n")
        
        if confirmar_senha != senha:
            print("Digite a mesma senha!")
        else:
            break

    cadastrar_aluno(nome_completo, usuario, email, cpf, data_nascimento, numero_telefone, senha)