from limpar_tela.limpar_tela import limpar_tela
from alunos.menu_atualizar_alunos import menu_atualizar_alunos

def home_alunos(aluno_autenticado):
    menu = ["Vizualizar Turma", "Atualizar Cadastro", "Sair"]
    # menu = ["Vizualizar Turma", "Atualizar Cadastro", "Mudar Curso", "Sair"]
    
    while True:    
        limpar_tela()

        print("--------------------------------------------")
        print("             Escola de Idiomas              ")
        print("--------------------------------------------")

        print(f"Bem-Vindo de Volta, {aluno_autenticado[1]}!\n")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")
        
        print("--------------------------------------------")
        try:
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    # TODO: Quando o aluno entra ele vê em qual curso ele tá matriculado, ve seus colegas de turma e seu professor
                    # Curso: Inglês
                    # Turma:
                    # 1 - Fulano
                    # 2 - Sicrano
                    # 3 - Beltrano
                    # Professor: José
                    print("Em breve")
                case 2:
                    menu_atualizar_alunos(aluno_autenticado[0])
                case 3:
                    break
                case _:
                    print("Opção inválida!")
                
        except ValueError:
            print("[ERRO]: Digite um número!")