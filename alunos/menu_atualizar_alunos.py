import getpass

from limpar_tela.limpar_tela import limpar_tela
from alunos.crud_alunos import atualizar_aluno
from alunos.validar_alunos import validar_nome_completo, validar_usuario, validar_email, validar_cpf, validar_data_nascimento, validar_numero_telefone, validar_senha

def menu_atualizar_alunos(id_aluno):
    # TODO: Perguntar o que quer atualizar do aluno
    menu_atualizar = ["Atualizar Nome Completo", "Atualizar Usuário", "Atualizar E-mail", "Atualizar CPF", 
                      "Atualizar Data de Nascimento", "Atualizar Número de Telefone", "Atualizar Senha", "Voltar"]
    
    while True:
        limpar_tela()
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
                            break
                case 2:
                    # TODO: Verificar erros
                    novo_usuario = input("Digite o novo usuário do aluno:\n")
                    validar_usuario(novo_usuario)
                    atualizar_aluno(id_aluno, novo_usuario, opcao_atualizar)
                case 3:
                    while True:
                        novo_email = input("Digite o novo nome e-mail do aluno:\n")
                        erro_novo_email = validar_email(novo_email)
                        
                        if erro_novo_email:
                            print(erro_novo_email)
                        else:
                            atualizar_aluno(id_aluno, novo_email, opcao_atualizar)
                            break
                case 4:
                    while True:
                        novo_cpf = input("Digite o novo CPF do aluno:\n")
                        erro_cpf = validar_cpf(novo_cpf)
                        
                        if erro_cpf:
                            print(erro_cpf)
                        else:
                            atualizar_aluno(id_aluno, novo_cpf, opcao_atualizar)
                            break
                case 5:
                    while True:
                        nova_data_nascimento = input("Digite a nova data de nascimento do aluno:\n")
                        erro_nova_data_nascimento = validar_data_nascimento(nova_data_nascimento)

                        if erro_nova_data_nascimento:
                            print(erro_nova_data_nascimento)
                        else:
                            nova_data_nascimento_validada = f"{nova_data_nascimento[:2]}/{nova_data_nascimento[2:4]}/{nova_data_nascimento[4:]}"
                            atualizar_aluno(id_aluno, nova_data_nascimento_validada, opcao_atualizar)
                            break
                case 6:
                    while True:
                        novo_numero_telefone = input("Digite o novo número de telefone do aluno:\n")
                        erro_numero_telefone = validar_numero_telefone(novo_numero_telefone)
                        
                        if erro_numero_telefone:
                            print(erro_numero_telefone)
                        else:
                            atualizar_aluno(id_aluno, novo_numero_telefone, opcao_atualizar)
                case 7:
                    # TODO: Verificar erros
                    nova_senha = getpass.getpass("Digite a nova senha do aluno:\n")
                    validar_senha(nova_senha)
                    while True:
                        confirmar_nova_senha = getpass.getpass("Confirme a nova senha do aluno:\n")
                        if confirmar_nova_senha != nova_senha:
                            print("Digite a mesma senha!")
                        else:
                            atualizar_aluno(id_aluno, nova_senha, opcao_atualizar)
                            
                case 8:
                    print("Voltando...")
                    break
                case _:
                    print(f"Opção inválida!")
                    
        except ValueError:
            print("[ERRO]: Digite um número!")
            limpar_tela()