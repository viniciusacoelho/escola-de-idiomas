from limpar_tela.limpar_tela import limpar_tela
from alunos.login_aluno import login_aluno
from alunos.matricular_aluno import matricular_aluno

def identificacao_aluno():
    """Página de identificação do aluno."""
    menu = ["Já sou aluno", "Não sou aluno", "Voltar"]

    while True:
        limpar_tela()

        print("--------------------------------------------")
        print("             Escola de Idiomas")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção:\n"))

            match opcao:
                case 1:
                    login_aluno()
                case 2:
                    matricular_aluno()
                case 3:
                    print("--------------------------------------------")
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida!")

        except ValueError:
            print("[ERRO]: Digite um número!")