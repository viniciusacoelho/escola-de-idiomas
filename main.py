from limpar_tela.limpar_tela import limpar_tela
# from identificacao.identificacao import identificacao
# from cursos.menu_cursos import menu_curso
from alunos.menu_alunos import menu_aluno

# menu = ["Administrador", "Professor", "Aluno", "Sair"]
# Teste
menu = ["Curso", "Professor", "Aluno", "Turma", "Sair"]
limpar_tela()
while True:
    print("--------------------------------------------")
    print("               Identifique-se               ")
    print("--------------------------------------------")

    for i in range(len(menu)):
        print(f"{i + 1} - {menu[i]}")

    print("--------------------------------------------")
    try:
        opcao = int(input("Digite uma opção:\n"))
        # identificacao(opcao)
        # menu_curso()
        menu_aluno()
        break
    except ValueError:
        print("[ERRO]: Digite um número!")
        limpar_tela()

# TODO: Tentar fazer um crud só para todas as entidades