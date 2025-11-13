import getpass
from limpar_tela.limpar_tela import limpar_tela
from alunos.validar_alunos import validar_nome_completo, validar_usuario, validar_email, validar_cpf, validar_data_nascimento, validar_numero_telefone, validar_senha
from alunos.crud_alunos import cadastrar_aluno

def cadastramento_aluno():
    limpar_tela()

    print("--------------------------------------------")
    print("                   Cadastro")
    print("--------------------------------------------")
    
    while True:
        nome_completo = input("Digite seu nome completo:\n")
        erro_nome_completo = validar_nome_completo(nome_completo)
        
        if erro_nome_completo:
            print(erro_nome_completo)
        else:
            break
    
    while True:
        usuario = input("Digite seu usuário:\n").lower()
        # erro_usuario = validar_usuario(usuario)
        
        # if erro_usuario:
        #     print(erro_usuario)
        # else:
        #     break
        break
    
    while True:
        email = input("Digite seu e-mail:\n").lower()
        erro_email = validar_email(email)
        
        if erro_email:
            print(erro_email)
        else:
            break

    while True:
        # TODO: Arrumar um jeito de colocar int e try/except e [ERRO]: Digite números!"
        cpf = input("Digite seu CPF:\n")
        erro_cpf = validar_cpf(cpf)
        
        if erro_cpf:
            print(erro_cpf)
        else:
            cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            break
    
    while True:
        # TODO: Arrumar um jeito de colocar int e try/except e [ERRO]: Digite números!"
        data_nascimento = input("Digite sua data de nascimento:\n")
        erro_data_nascimento =  validar_data_nascimento(data_nascimento)
        
        if erro_data_nascimento:
            print(erro_data_nascimento)
        else:
            data_nascimento = f"{data_nascimento[:2]}/{data_nascimento[2:4]}/{data_nascimento[4:]}"
            break
    
    while True:
        numero_telefone = int(input("Digite seu número de telefone:\n"))
        erro_numero_telefone = validar_numero_telefone(numero_telefone)
        
        if erro_numero_telefone:
            print(erro_numero_telefone)
        else:
            numero_telefone = str(numero_telefone)
            numero_telefone = f"({numero_telefone[:2]}) {numero_telefone[2:7]}-{numero_telefone[7:]}"
            break
        
    while True:
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
        confirmar_senha = getpass.getpass("Confirme sua senha:\n")
        
        if confirmar_senha != senha:
            print("Digite a mesma senha!")
        else:
            break

    cadastrar_aluno(nome_completo, usuario, email, cpf, data_nascimento, numero_telefone, senha)
    # cadastrar_aluno(id_aluno, nome_completo, usuario, email, cpf, data_nascimento, numero_telefone, senha)