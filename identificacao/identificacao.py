from limpar_tela.limpar_tela import limpar_tela
from administrador.administrador import administrador
# from professores.professor import professor
# from professores.professor import professor
from alunos.cadastramento_aluno import cadastramento_aluno
from alunos.login_aluno import login_aluno

def identificacao(opcao_escolhida: int):

    while True:
        limpar_tela()
        menu = ["Criar Conta", "Login", "Voltar"]

        print("--------------------------------------------")
        print("             Escola de Idiomas              ")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")
        
        print("--------------------------------------------")
        try:
            opcao = int(input("Digite uma opção:\n"))

            if opcao == 1 and opcao_escolhida == 1:
                administrador()
            elif opcao == 2 and opcao_escolhida == 1:
                # administrador()
                print("Em breve")
                limpar_tela()
            elif opcao == 1 and opcao_escolhida == 2:
                # cadastrar_professor()
                print("Em breve")
                limpar_tela()
            elif opcao == 2 and opcao_escolhida == 2:
                # login_professor()
                print("Em breve")
                limpar_tela()
            elif opcao == 1 and opcao_escolhida == 3:
                cadastramento_aluno()
            elif opcao == 2 and opcao_escolhida == 3:
                login_aluno()
                # print("Em breve")
                limpar_tela()
            elif opcao == 1 and opcao_escolhida == 4:
                # cadastrar_turma()
                limpar_tela()
            elif opcao == 2 and opcao_escolhida == 4:
                # login_turmas()
                limpar_tela()
            elif opcao == 3:
                break
            else:
                print("Opção inválida!")
                limpar_tela()
        except ValueError:
            print("[ERRO]: Digite um número!")
            limpar_tela()