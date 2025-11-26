import getpass

from limpar_tela.limpar_tela import limpar_tela
from professores.crud_professor import atualizar_professor
from professores.validar_professor import validar_cpf, validar_email, validar_endereco, validar_idioma_lecionado, validar_nome_completo, validar_numero_telefone, validar_senha
from unique.verificar_unique import verificar_unique

def menu_atualizar_professor(id_professor: int):
    """
    Menu de atualização dos dados do professor.

    Args:
        id_professor: ID do professor cadastrado no banco de dados.
    """
    menu_atualizar = ["Atualizar Nome Completo", "Atualizar E-mail", "Atualizar CPF",  "Atualizar Número de Telefone",
                      "Atualizar Endereço", "Atualizar Idioma Lecionado", "Atualizar Senha", "Voltar"]

    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("            Atualizar Professor")
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
                        novo_nome_completo = input("Digite o novo nome completo do professor:\n")
                        erro_novo_nome_completo = validar_nome_completo(novo_nome_completo)

                        if erro_novo_nome_completo:
                            print(erro_novo_nome_completo)
                        else:
                            atualizar_professor(id_professor, novo_nome_completo, "nome_completo", "Nome completo")
                            break

                case 2:
                    while True:
                        print("--------------------------------------------\n")
                        novo_email = input("Digite o novo e-mail do professor:\n").lower()
                        erro_novo_email = validar_email(novo_email)

                        if erro_novo_email:
                            print(erro_novo_email)
                        else:
                            erro_verificar_unique = verificar_unique("Professores", novo_email, 2, "E-mail")

                            if erro_verificar_unique:
                                print(erro_verificar_unique)
                            else:
                                atualizar_professor(id_professor, novo_email, "email", "E-mail")
                                break

                case 3:
                    while True:
                        print("--------------------------------------------\n")
                        novo_cpf = input("Digite o novo CPF do professor:\n")

                        try:
                            int(novo_cpf)
                            erro_cpf = validar_cpf(novo_cpf)

                            if erro_cpf:
                                print(erro_cpf)
                            else:
                                novo_cpf = f"{novo_cpf[:3]}.{novo_cpf[3:6]}.{novo_cpf[6:9]}-{novo_cpf[9:]}"
                                erro_verificar_unique = verificar_unique("professors", novo_cpf, 3, "CPF")

                                if erro_verificar_unique:
                                    print(erro_verificar_unique)
                                else:
                                    atualizar_professor(id_professor, novo_cpf, "cpf", "CPF")
                                    break

                        except ValueError:
                            print("[ERRO]: Digite apenas números!")

                case 4:
                    while True:
                        print("--------------------------------------------\n")
                        novo_numero_telefone = input("Digite o novo número de telefone do professor:\n")

                        try:
                            int(novo_numero_telefone)
                            erro_numero_telefone = validar_numero_telefone(novo_numero_telefone)

                            if erro_numero_telefone:
                                print(erro_numero_telefone)
                            else:
                                novo_numero_telefone = f"({novo_numero_telefone[:2]}) {novo_numero_telefone[2:7]}-{novo_numero_telefone[7:]}"
                                erro_verificar_unique = verificar_unique("professors", novo_numero_telefone, 4, "Número de telefone")

                                if erro_verificar_unique:
                                    print(erro_verificar_unique)
                                else:
                                    atualizar_professor(id_professor, novo_numero_telefone, "numero_telefone", "Número de Telefone")
                                    break

                        except ValueError:
                            print("[ERRO]: Digite apenas números!")

                case 5:
                    while True:
                        print("--------------------------------------------\n")
                        novo_endereco = input("Digite a novo endereço do professor:\n")
                        input(novo_endereco)
                        erro_novo_endereco = validar_endereco(novo_endereco)

                        if erro_novo_endereco:
                                print(erro_novo_endereco)
                        else:
                            novo_endereco_validado = f"{novo_endereco[:2]}/{novo_endereco[2:4]}/{novo_endereco[4:]}"
                            atualizar_professor(id_professor, novo_endereco_validado, "novo_endereco", "Novo Endereço")
                            break

                case 6:
                    while True:
                        print("--------------------------------------------\n")
                        novo_idioma_lecionado = input("Digite a nova data de nascimento do professor:\n")

                        try:
                            input(novo_idioma_lecionado)
                            erro_novo_idioma_lecionado = validar_idioma_lecionado(novo_idioma_lecionado)

                            if erro_novo_idioma_lecionado:
                                print(erro_novo_idioma_lecionado)
                            else:
                                novo_idioma_lecionado_validado = f"{novo_idioma_lecionado[:2]}/{novo_idioma_lecionado[2:4]}/{novo_idioma_lecionado[4:]}"
                                atualizar_professor(id_professor, novo_idioma_lecionado_validado, "idioma_lecionado", "Idioma Lecionado")
                                break

                        except ValueError:
                            print("[ERRO]: Digite apenas números!")
                

                case 7:
                    print("--------------------------------------------\n")
                    nova_senha = getpass.getpass("Digite a nova senha do professor:\n")
                    validar_senha(nova_senha)

                    while True:
                        confirmar_nova_senha = getpass.getpass("Confirme a nova senha do professor:\n")

                        if confirmar_nova_senha != nova_senha:
                            print("Digite a mesma senha!")
                        else:
                            atualizar_professor(id_professor, nova_senha, "senha", "Senha")
                            break

                case 8:
                    print("Voltando...")
                    break
                case _:
                    print(f"Opção inválida!")

        except ValueError:
            print("[ERRO]: Digite um número!")
            limpar_tela()