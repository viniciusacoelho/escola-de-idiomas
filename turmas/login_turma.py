from limpar_tela.limpar_tela import limpar_tela
from professores.crud_professor import listar_professores
from alunos.crud_alunos import listar_alunos 
from turmas.crud_turmas import cadastrar_turma

def login_turma():
    menu = ["Inserir Professor", "Inserir Alunos", "Inserir Curso", "Voltar"]

    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("                Login Turma                 ")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    professores = listar_professores()

                    for professor in professores:
                        print(f"{professor[0]} - {professor[1]}")

                    try:
                        id_professor = int(input("Digite o id do professor que deseja cadastrar: \n"))
                        cadastrar_turma(id_professor, "id_professor")
                        break
                    except ValueError:
                        print("[ERRO]: Digite apenas números!")
                        break
                case 2:
                    listar_alunos()
                    
                case 3:
                    pass
                case 4:
                    horario = int(input("Digite os horários de início e de término da turma: \n"))
                    
                case 5:    
                    print("Voltando...")
                    break
                case _:
                    print("Digite uma opção válida!")

        except ValueError:
            print("[ERRO]: Digite um número!")