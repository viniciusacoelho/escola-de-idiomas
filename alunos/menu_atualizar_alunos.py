import getpass

from limpar_tela.limpar_tela import limpar_tela
from alunos.crud_alunos import atualizar_aluno
from alunos.validar_alunos import validar_nome_completo, validar_usuario, validar_email, validar_cpf, validar_data_nascimento, validar_numero_telefone, validar_senha

def menu_atualizar_alunos(id_aluno):
    # TODO: Perguntar o que quer atualizar do aluno
    menu_atualizar = ["Atualizar Nome Completo", "Atualizar Usuário", "Atualizar E-mail", "Atualizar CPF", 
                      "Atualizar Data de Nascimento", "Atualizar Número de Telefone", "Atualizar Senha", "Voltar"]
    
    limpar_tela()
    
    while True:
        print("--------------------------------------------")
        print("              Atualizar Aluno")
        print("--------------------------------------------")

        for i in range(len(menu_atualizar)):
            print(f"{i + 1} - {menu_atualizar[i]}")
                
        try:
            print("--------------------------------------------")
            opcao_atualizar = int(input("Digite uma opção: "))
            match opcao_atualizar:
                case 1:

                    while True:
                        novo_nome_completo = input("Digite o novo nome completo do aluno:\n")
                        erro_novo_nome_completo = validar_nome_completo(novo_nome_completo)
                        
                        if erro_novo_nome_completo:
                            print(erro_novo_nome_completo)
                        else:
                            atualizar_aluno(id_aluno, novo_nome_completo, opcao_atualizar)
                            limpar_tela()
                            break
                case 2:
                    novo_usuario = input("Digite o novo usuário do aluno:\n")
                    validar_usuario(novo_usuario)
                    atualizar_aluno(id_aluno, novo_usuario, opcao_atualizar)
                    limpar_tela()
                case 3:
                    novo_email = input("Digite o novo nome e-mail do aluno:\n")
                    validar_email(novo_email)
                    atualizar_aluno(id_aluno, novo_email, opcao_atualizar)
                    limpar_tela()
                case 4:
                    novo_cpf = input("Digite o novo CPF do aluno:\n")
                    cpf_validado = validar_cpf(novo_cpf)
                    atualizar_aluno(id_aluno, cpf_validado, opcao_atualizar)
                    limpar_tela()

                case 5:
                    while True:
                        nova_data_nascimento = input("Digite a nova data de nascimento do aluno:\n")
                        erro_nova_data_nascimento = validar_data_nascimento(nova_data_nascimento)

                        if erro_nova_data_nascimento:
                            print(erro_nova_data_nascimento)
                        else:
                            nova_data_nascimento_validada = f"{nova_data_nascimento[:2]}/{nova_data_nascimento[2:4]}/{nova_data_nascimento[4:]}"
                            atualizar_aluno(id_aluno, nova_data_nascimento_validada, opcao_atualizar)
                            limpar_tela()
                            break

                case 6:
                    novo_numero_telefone = input("Digite o novo número de telefone do aluno:\n")
                    numero_telefone_validado = validar_numero_telefone(novo_numero_telefone)
                    atualizar_aluno(id_aluno, numero_telefone_validado, opcao_atualizar)
                    limpar_tela()
                case 7:
                    nova_senha = getpass.getpass("Digite a nova senha do aluno:\n")
                    validar_senha(nova_senha)
                    confirmar_nova_senha = getpass.getpass("Confirme a nova senha do aluno:\n")
                    atualizar_aluno(id_aluno, nova_senha, opcao_atualizar)
                    limpar_tela()
                case 8:
                    print("Voltando...")
                    limpar_tela()
                    break
                case _:
                    print(f"Opção inválida!")
                    limpar_tela()
                    continue
        except ValueError:
            print("[ERRO]: Digite um número!")
            limpar_tela()