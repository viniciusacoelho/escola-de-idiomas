from limpar_tela.limpar_tela import limpar_tela
from cursos.menu_cursos import menu_curso
from professores.menu_professor import menu_professor
from alunos.menu_aluno import menu_aluno
from turmas.menu_turma import menu_turma

def menu_administrador():
    """Página do menu de administração da Escola de Idiomas."""
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
                    menu_professor()
                case 3:
                   menu_aluno()
                case 4:
                    menu_turma()
                case 5:
                    print("Voltando...")
                    break
                case _:
                   print("Opção inválida!")

        except ValueError:
            print("[ERRO]: Digite um número!")