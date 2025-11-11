import getpass
from limpar_tela.limpar_tela import limpar_tela
from alunos.validar_alunos import validar_nome_completo, validar_usuario, validar_email, validar_cpf, validar_data_nascimento, validar_numero_telefone, validar_senha
from alunos.crud_alunos import cadastrar_aluno

def cadastramento_aluno():
    limpar_tela()

    print("--------------------------------------------")
    print("                   Cadastro")
    print("--------------------------------------------")
    
    nome_completo = input("Digite seu nome completo:\n")
    nome_completo_validado = validar_nome_completo(nome_completo)
    print(f"{nome_completo_validado}")
    
    usuario = input("Digite seu usuário:\n").lower()
    usuario_validado = validar_usuario(usuario)
    print(f"{usuario_validado}")
    
    email = input("Digite seu e-mail:\n").lower()   
    email_validado = validar_email(email)
    print(f"{email_validado}")

    while True:
        try:
            # TODO: Arrumar um jeito de colocar int
            cpf = input("Digite seu CPF:\n")
            
            cpf_validado = validar_cpf(cpf)
            print(f"{cpf_validado}")

            # TODO: Arrumar um jeito de colocar int
            data_nascimento = input("Digite sua data de nascimento:\n")
            data_nascimento_validada =  validar_data_nascimento(data_nascimento)
            print(f"{data_nascimento_validada}")

            numero_telefone = int(input("Digite seu número de telefone:\n"))
            numero_telefone_validado = validar_numero_telefone(numero_telefone)
            print(f"{numero_telefone_validado}")
            
            break
        except ValueError:
            print("[ERRO]: Digite números!")

    senha = getpass.getpass("Digite sua senha:\n")
    # senha_validada = validar_senha(senha)
    # print(f"{senha_validada}")

    while True:
        confirmar_senha = getpass.getpass("Confirme sua senha:\n")
        if confirmar_senha != senha:
            print("Digite a mesma senha!")
        else:
            break

    cadastrar_aluno(nome_completo, usuario, email, cpf_validado, data_nascimento_validada, numero_telefone_validado, senha)
    # cadastrar_aluno(nome_completo_validado, usuario_validado, email_validado, cpf_validado, data_nascimento_validada, numero_telefone_validado, senha)
    # cadastrar_aluno(id_aluno, nome_completo, usuario, cpf, data_nascimento, numero_telefone, senha)