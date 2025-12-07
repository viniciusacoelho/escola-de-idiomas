from limpar_tela.limpar_tela import limpar_tela
from administrador.login_administrador import login_administrador
from professores.identificacao_professor import identificacao_professor
from alunos.identificacao_aluno import identificacao_aluno

menu = ["Administrador", "Professor", "Aluno", "Sair"]

while True:
    limpar_tela()

    print("--------------------------------------------")
    print("               Identifique-se               ")
    print("--------------------------------------------")

    for i in range(len(menu)):
        print(f"{i + 1} - {menu[i]}")

    try:
        print("--------------------------------------------")
        opcao = int(input("Digite uma opção:\n"))

        match opcao:
            case 1:  
                login_administrador()
            case 2:
                identificacao_professor()
            case 3:
                identificacao_aluno()
            case 4:
                print("--------------------------------------------")
                print("Saindo...")
                limpar_tela()

                print("--------------------------------------------")
                print("              Desenvolvedor")
                print("--------------------------------------------")
                print("@viniciusacoelho_")
                print("--------------------------------------------\n")
                break

            case _:
                print("Opção inválida!")

    except ValueError:
        print("--------------------------------------------")
        print("[ERRO]: Digite um número!")