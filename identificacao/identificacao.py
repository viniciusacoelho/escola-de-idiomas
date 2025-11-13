from limpar_tela.limpar_tela import limpar_tela
from administrador.menu_administrador import menu_administrador
# from professores.professor import professor
# from professores.professor import professor
from alunos.cadastramento_aluno import cadastramento_aluno
from alunos.login_aluno import login_aluno

def identificacao(opcao_escolhida: int):
    while True:
        menu = ["Criar Conta", "Login", "Voltar"]
        
        limpar_tela()

        print("--------------------------------------------")
        print("             Escola de Idiomas              ")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")
        
        print("--------------------------------------------")
        try:
            opcao = int(input("Digite uma opção:\n"))

            if opcao == 1 and opcao_escolhida == 1:
                menu_administrador()
            elif opcao == 2 and opcao_escolhida == 1:
                # administrador()
                print("Em breve")
            elif opcao == 1 and opcao_escolhida == 2:
                # cadastrar_professor()
                print("Em breve")
            elif opcao == 2 and opcao_escolhida == 2:
                # login_professor() -> vizualizar turmas e atualizar cadastro (e talvez Adicionar notas) sair
                print("Em breve")
                # TODO: Verificar se precisa colocar a função 'limpar_tela' em todas as opções
            elif opcao == 1 and opcao_escolhida == 3:
                cadastramento_aluno()
            elif opcao == 2 and opcao_escolhida == 3:
                login_aluno()
            elif opcao == 1 and opcao_escolhida == 4:
                # cadastrar_turma()
                pass
            elif opcao == 2 and opcao_escolhida == 4:
                # login_turmas()
                pass
            elif opcao == 3:
                print("--------------------------------------------")
                print("Voltando...")
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("[ERRO]: Digite um número!")