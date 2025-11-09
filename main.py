from limpar_tela.limpar_tela import limpar_tela
from identificacao.identificacao import identificacao
from cursos.menu_cursos import menu_curso

# menu = ["Administrador", "Professor", "Aluno", "Sair"]
# Teste
menu = ["Curso", "Professor", "Aluno", "Sair"]
limpar_tela()
while True:
    print("--------------------------------------------")
    print("               Identifique-se               ")
    print("--------------------------------------------")

    for i in range(len(menu)):
        print(f"{i + 1} - {menu[i]}")

    print("--------------------------------------------")
    try:
        opcao = int(input("Digite uma opção: "))
        # identificacao(opcao)
        menu_curso()
        break
    except ValueError:
        print("[ERRO]: Digite um número!")
        limpar_tela()