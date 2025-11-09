from limpar_tela.limpar_tela import limpar_tela
from administrador.administrador import administrador
from professores.professor import professor
from professores.professor import professor
from alunos.menu_alunos import cadastrar_aluno, login_aluno

def identificacao(opcao_escolhida):
    limpar_tela()

    menu = ["Criar Conta", "Login", "Voltar"]

    print("--------------------------------------------")
    print("              Escola de Idiomas             ")
    print("--------------------------------------------")

    for i in range(len(menu)):
        print(f"{i + 1} - {menu[i]}")
    
    while True:
        try:
            opcao = int(input("Digite uma opção:\n"))
            if opcao == 1 and opcao_escolhida == 1:
                administrador()
            # elif opcao == 2 and opcao_escolhida == 1:
            #     administrador()
            # elif opcao == 1 and opcao_escolhida == 2:
            #     cadastrar_professor()
            # elif opcao == 2 and opcao_escolhida == 2:
            #     login_professor()
            elif opcao == 1 and opcao_escolhida == 3:
                cadastrar_aluno()
            elif opcao == 2 and opcao_escolhida == 3:
                login_aluno()
            # elif opcao == 1 and opcao_escolhida == 4:
            #     cadastrar_turma()
            # elif opcao == 2 and opcao_escolhida == 4:
            #     login_turmas()
            elif opcao == 4:
                break
            else:
                print("Opção inválida!")
                limpar_tela()
                continue
            # break
        except ValueError:
            print("[ERRO]: Digite um número!")
            limpar_tela()