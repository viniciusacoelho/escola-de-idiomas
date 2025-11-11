import getpass

from limpar_tela.limpar_tela import limpar_tela
from alunos.crud_alunos import atualizar_aluno

def atualizar_alunos(id_aluno):
    # TODO: Perguntar o que quer atualizar do aluno
    menu_atualizar = ["Atualizar Nome Completo", "Atualizar Usuário", "Atualizar E-mail", "Atualizar CPF", "Atualizar Data de Nascimento", "Atualizar Número de Telefone", "Atualizar Senha", "Voltar"]
    limpar_tela()
    
    while True:
        print("--------------------------------------------")
        print("             Atualizar Cadastro")
        print("--------------------------------------------")

        for i in range(len(menu_atualizar)):
            print(f"{i + 1} - {menu_atualizar[i]}")
                
        try:
            print("--------------------------------------------")
            opcao_atualizar = int(input("Digite uma opção: "))
            break
        except ValueError:
            print("[ERRO]: Digite um número!")
            limpar_tela()
            
    match opcao_atualizar:
        case 1:
            novo_nome_completo = input("Digite o novo nome completo do aluno:\n")
            atualizar_aluno(id_aluno, novo_nome_completo, opcao_atualizar)
        case 2:
            novo_usuario = input("Digite o novo usuário do aluno:\n")
            atualizar_aluno(id_aluno, novo_usuario)
        case 3:
            novo_email = input("Digite o novo nome e-mail do aluno:\n")
            atualizar_aluno(id_aluno, novo_email, opcao_atualizar)
        case 4:
            novo_cpf = input("Digite o novo CPF do aluno:\n")
            atualizar_aluno(id_aluno, novo_cpf, opcao_atualizar)
        case 5:
            nova_data_nascimento = input("Digite a nova data de nascimento do aluno:\n")
            atualizar_aluno(id_aluno, nova_data_nascimento, opcao_atualizar)
        case 6:
            novo_numero_telefone = input("Digite o novo número de telefone do aluno:\n")
            atualizar_aluno(id_aluno, novo_numero_telefone, opcao_atualizar)
        case 7:
            nova_senha = getpass.getpass("Digite a nova senha do aluno:\n")
            atualizar_aluno(id_aluno, nova_senha, opcao_atualizar)
        case 8:
            print("Voltando...")
            limpar_tela()
        case _:
            print(f"Opção inválida!")
            limpar_tela()