from limpar_tela.limpar_tela import limpar_tela
from identificacao.identificacao import identificacao
# from cursos.menu_cursos import menu_curso
from administrador.menu_administrador import menu_administrador
# from alunos.menu_alunos import menu_aluno
from alunos.identificacao_aluno import identificacao_aluno
from professores.identificacao_professor import identificacao_professor

menu = ["Administrador", "Professor", "Aluno", "Sair"]
# menu = ["Curso", "Professor", "Aluno", "Turma", "Sair"]

while True:
    limpar_tela()

    print("--------------------------------------------")
    print("               Identifique-se               ")
    print("--------------------------------------------")

    for i in range(len(menu)):
        print(f"{i + 1} - {menu[i]}")

    print("--------------------------------------------")
    try:
        opcao = int(input("Digite uma opção:\n"))
        if opcao == 1:  
            menu_administrador()
        elif opcao == 2:
            identificacao_professor()
        elif opcao == 3:
            # identificacao(opcao)
            identificacao_aluno()
        elif opcao == 4:
            print("--------------------------------------------")
            print("Saindo...")
            limpar_tela()

            print("--------------------------------------------")
            print("              Desenvolvedores")
            print("--------------------------------------------")
            print("@viniciusacoelho_")
            print("@joao.coelho21")
            print("--------------------------------------------\n")
            break
        else:
            print("Opção inválida!")
        # menu_curso()
        # menu_aluno()
    except ValueError:
        print("--------------------------------------------")
        print("[ERRO]: Digite um número!")