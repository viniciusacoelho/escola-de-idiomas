from limpar_tela.limpar_tela import limpar_tela
from professores.cadastramento_professor import cadastramento_professor
from professores.crud_professor import listar_professores, buscar_professor, atualizar_professor, deletar_professor
def menu_professor():
    "Página do menu do professor."
    menu = ["Cadastrar Professor", "Listar Professores", "Buscar Professor", "Atualizar Professor", "Deletar Professor", "Voltar"]

    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("              Escola de Idiomas             ")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    cadastramento_professor()
                case 2:
                    professores = listar_professores()

                    if len(professores) > 0:

                        for professor in professores:
                            print(f"Professor {professor[0]}:\nNome completo: {professor[1]}\nE-mail: {professor[2]}\nCPF: {professor[3]}\nNúmero de telefone: {professor[4]}\nEndereço: {professor[5]}\nIdioma lecionado: {professor[6]}\nSenha: *****")
                            print("--------------------------------------------")

                    else:
                        print("Nenhum professor cadastrada anteriormente.")

                case 3:
                    while True:    
                        professores = listar_professores()                                     

                        if len(professores) > 0:
                            email_professor = input("Digite o e-mail do professor que você deseja buscar:\n")
                            professores = buscar_professor(email_professor)

                            for professor in professores:
                                if email_professor == professor[2]:

                                    for professor in professores:
                                        print("--------------------------------------------")
                                        print(f"Professor {professor[0]}:\nNome completo: {professor[1]}\nE-mail: {professor[2]}\nCPF: {professor[3]}\nNúmero de telefone: {professor[4]}\nEndereço: {professor[5]}\nIdioma lecionado: {professor[6]}\nSenha: *****")
                                    break
                                
                                else:
                                    print("E-mail do professor não cadastrado anteriormente.")
                                    break
                            break
                        else:
                            print("Nenhum professor cadastrado anteriormente.")
                            break

                case 4:
                    while True:
                        professores = listar_professores()                    

                        if len(professores) > 0:
                            try:
                                id_professor = int(input("Digite o ID do professor que você deseja atualizar:\n"))

                                for professor in professores:
                                    if professores == professor[0]:
                                        atualizar_professor(id_professor)
                                        break

                                else:
                                    print("ID do professor inválido!")
                                    # break
                                break
                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break

                        else:
                            print("Nenhum professor cadastrado anteriormente.")
                            break

                case 5:
                    while True:
                        professores = listar_professores()                    

                        if len(professores) > 0:
                            try:
                                id_professor = int(input("Digite o ID do professor que você deseja deletar:\n"))
                                
                                for professor in professores:
                                    if id_professor == professor[0]:
                                        deletar_professor(id_professor)
                                        break

                                else:
                                    print("ID do professor inválido!")
                                    break
                                break

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break

                        else:
                            print("Nenhum professor cadastrada anteriormente.")
                            break

                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Digite uma opção válida!")

        except ValueError:
            print("[ERRO]: Digite um número!")