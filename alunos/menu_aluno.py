from limpar_tela.limpar_tela import limpar_tela
from alunos.matricular_aluno import matricular_aluno
from alunos.crud_aluno import listar_alunos, buscar_aluno, deletar_aluno, aluno_curso
from alunos.menu_atualizar_alunos import menu_atualizar_alunos
from unique.verificar_unique import verificar_unique

def menu_aluno():
    """Menu principal dos alunos."""
    menu = ["Cadastrar Aluno", "Listar Alunos", "Buscar Aluno", "Atualizar Aluno", "Deletar Aluno", "Voltar"]

    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("                   Alunos")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção:\n"))

            match opcao:
                case 1:
                    matricular_aluno()
                case 2:
                    alunos = listar_alunos()

                    if len(alunos) > 0:
                        print(f"Alunos listados com sucesso!")
                        print("--------------------------------------------")

                        for aluno in alunos:
                            print(f"Aluno {aluno[0]}\nNome completo: {aluno[1]}\nUsuário: {aluno[2]}\nE-mail: {aluno[3]}\nCPF: {aluno[4]}\nData de nascimento: {aluno[5]}\nNúmero de telefone: {aluno[6]}\nSenha: *****")

                            cursos = aluno_curso(aluno[0])
                            if len(cursos) > 0:
                                print("Curso:")

                                for curso in cursos:
                                    print(curso[0])

                            else:
                                print("Curso: Nenhum curso escolhido anteriormente.")
                            print("--------------------------------------------")

                    else:
                        print("Nenhum aluno cadastrado anteriormente.")

                case 3:
                    while True:
                        alunos = listar_alunos()

                        if len(alunos) > 0:
                            print("--------------------------------------------")
                            buscar_usuario = input("Digite o usuário do aluno que deseja buscar:\n")
                            nome_busca_unique = verificar_unique("Alunos", buscar_usuario, 2, "Aluno")

                            if not nome_busca_unique:
                                print(f"Aluno '{buscar_usuario}' não cadastrado anteriormente.")
                                break
                            else:
                                alunos = buscar_aluno(buscar_usuario)

                                print("--------------------------------------------")
                                for aluno in alunos:
                                    print(f"Aluno {aluno[0]}\nNome completo: {aluno[1]}\nUsuário: {aluno[2]}\nE-mail: {aluno[3]}\nCPF: {aluno[4]}\nData de nascimento: {aluno[5]}\nNúmero de telefone: {aluno[6]}\nSenha: *****")

                                    cursos = aluno_curso(aluno[0])
                                    if len(cursos) > 0:
                                        print("Curso:")

                                        for curso in cursos:
                                            print(curso[0])

                                    else:
                                        print("Curso: Nenhum curso escolhido anteriormente.")
                                break

                        else:
                            print("Nenhum aluno cadastrado anteriormente")
                            break

                case 4:
                    while True:
                        alunos = listar_alunos()

                        if len(alunos) > 0:
                            try:
                                id_aluno = int(input("Digite o ID do aluno que deseja atualizar:\n"))

                                for aluno in alunos:
                                    if id_aluno == aluno[0]:
                                        menu_atualizar_alunos(id_aluno)
                                        break
                                else:
                                    print("ID do aluno inválido!")
                                    break
                                break
                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break

                        else:
                            print("Nenhum aluno cadastrado anteriormente.")
                            break

                case 5:
                    while True:
                        alunos = listar_alunos()

                        if len(alunos) > 0:
                            try:
                                id_aluno = int(input("Digite o ID do aluno que deseja deletar:\n"))

                                for aluno in alunos:
                                    if id_aluno == aluno[0]:
                                        deletar_aluno(id_aluno, alunos[1])
                                        break
                                else:
                                    print("ID do aluno inválido!")
                                    break
                                break

                            except ValueError:
                                print("[ERRO]: Digite um número!")
                                break

                        else:
                            print("Nenhum aluno cadastrado anteriormente.")
                            break

                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Digite uma opção válida!")

        except ValueError:
            print("--------------------------------------------")
            print("[ERRO]: Digite um número!")