from limpar_tela.limpar_tela import limpar_tela
from cursos.menu_cursos import menu_curso
from alunos.menu_alunos import menu_aluno

def menu_administrador():
    
    menu = ["Cursos", "Professores", "Alunos", "Turmas", "Voltar"]
    
    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("              Escola de Idiomas")
        print("--------------------------------------------")
        print("Adiministrador\n")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        print("--------------------------------------------")
        try:
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1:
                   menu_curso() 
                case 2:
                    # menu_professores()
                    print("Em breve")
                case 3:
                   menu_aluno()
                case 4:
                #     menu_turmas()
                    print("Em breve")
                case 5:
                    print("Voltando...")
                    break
                case _:
                   print("Opção inválida!")

        except ValueError:
            print("[ERRO]: Digite um número!")