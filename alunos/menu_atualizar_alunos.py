import getpass

from limpar_tela.limpar_tela import limpar_tela
from alunos.crud_aluno import atualizar_aluno, listar_alunos
from alunos.validar_alunos import validar_nome_completo, validar_usuario, validar_email, validar_cpf, validar_data_nascimento, validar_numero_telefone, validar_senha
from unique.verificar_unique import verificar_unique

def menu_atualizar_alunos(id_aluno: int):
    """
    Menu de atualização dos dados do aluno.

    Args:
        id_aluno: ID do aluno cadastrado no banco de dados.
    """
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
                        print("--------------------------------------------\n")
                        novo_nome_completo = input("Digite o novo nome completo do aluno:\n")
                        erro_novo_nome_completo = validar_nome_completo(novo_nome_completo)

                        if erro_novo_nome_completo:
                            print(erro_novo_nome_completo)
                        else:
                            atualizar_aluno(id_aluno, novo_nome_completo, "nome_completo", "Nome completo")
                            break

                case 2:
                    while True:
                        print("--------------------------------------------\n")
                        novo_usuario = input("Digite o novo usuário do aluno:\n").lower()
                        erro_usuario = validar_usuario(novo_usuario)

                        if erro_usuario:
                            print(erro_usuario)
                        else:
                            erro_verificar_unique = verificar_unique("Alunos", novo_usuario, 2, "Usuário")

                            if erro_verificar_unique:
                                print(erro_verificar_unique)
                            else:
                                atualizar_aluno(id_aluno, novo_usuario, "usuario", "Usuário")
                                break

                case 3:
                    while True:
                        print("--------------------------------------------\n")
                        novo_email = input("Digite o novo e-mail do aluno:\n").lower()
                        erro_novo_email = validar_email(novo_email)

                        if erro_novo_email:
                            print(erro_novo_email)
                        else:
                            erro_verificar_unique = verificar_unique("Alunos", novo_email, 3, "E-mail")

                            if erro_verificar_unique:
                                print(erro_verificar_unique)
                            else:
                                atualizar_aluno(id_aluno, novo_email, "email", "E-mail")
                                break

                case 4:
                    while True:
                        print("--------------------------------------------\n")
                        novo_cpf = input("Digite o novo CPF do aluno:\n")

                        try:
                            int(novo_cpf)
                            erro_cpf = validar_cpf(novo_cpf)

                            if erro_cpf:
                                print(erro_cpf)
                            else:
                                novo_cpf = f"{novo_cpf[:3]}.{novo_cpf[3:6]}.{novo_cpf[6:9]}-{novo_cpf[9:]}"
                                erro_verificar_unique = verificar_unique("Alunos", novo_cpf, 4, "CPF")

                                if erro_verificar_unique:
                                    print(erro_verificar_unique)
                                else:
                                    atualizar_aluno(id_aluno, novo_cpf, "cpf", "CPF")
                                    break

                        except ValueError:
                            print("[ERRO]: Digite apenas números!")

                case 5:
                    while True:
                        print("--------------------------------------------\n")
                        nova_data_nascimento = input("Digite a nova data de nascimento do aluno:\n")

                        try:
                            int(nova_data_nascimento)
                            erro_nova_data_nascimento = validar_data_nascimento(nova_data_nascimento)

                            if erro_nova_data_nascimento:
                                print(erro_nova_data_nascimento)
                            else:
                                nova_data_nascimento_validada = f"{nova_data_nascimento[:2]}/{nova_data_nascimento[2:4]}/{nova_data_nascimento[4:]}"
                                atualizar_aluno(id_aluno, nova_data_nascimento_validada, "data_nascimento", "Data Nascimento")
                                break

                        except ValueError:
                            print("[ERRO]: Digite apenas números!")

                case 6:
                    while True:
                        print("--------------------------------------------\n")
                        novo_numero_telefone = input("Digite o novo número de telefone do aluno:\n")

                        try:
                            int(novo_numero_telefone)
                            erro_numero_telefone = validar_numero_telefone(novo_numero_telefone)

                            if erro_numero_telefone:
                                print(erro_numero_telefone)
                            else:
                                novo_numero_telefone = f"({novo_numero_telefone[:2]}) {novo_numero_telefone[2:7]}-{novo_numero_telefone[7:]}"
                                erro_verificar_unique = verificar_unique("Alunos", novo_numero_telefone, 6, "Número de telefone")

                                if erro_verificar_unique:
                                    print(erro_verificar_unique)
                                else:
                                    atualizar_aluno(id_aluno, novo_numero_telefone, "numero_telefone", "Número de Telefone")
                                    break

                        except ValueError:
                            print("[ERRO]: Digite apenas números!")

                case 7:
                    print("--------------------------------------------\n")
                    nova_senha = getpass.getpass("Digite a nova senha do aluno:\n")
                    validar_senha(nova_senha)

                    while True:
                        confirmar_nova_senha = getpass.getpass("Confirme a nova senha do aluno:\n")

                        if confirmar_nova_senha != nova_senha:
                            print("Digite a mesma senha!")
                        else:
                            atualizar_aluno(id_aluno, nova_senha, "senha", "Senha")
                            break

                case 8:
                    print("Voltando...")
                    break
                case _:
                    print(f"Opção inválida!")

        except ValueError:
            print("[ERRO]: Digite um número!")
            limpar_tela()