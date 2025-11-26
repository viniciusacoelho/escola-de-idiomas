from limpar_tela.limpar_tela import limpar_tela
from turmas.crud_turmas import autenticar_turma
from turmas.portal_turma import portal_turma

def login_turma():
    """Página de login da turma."""
    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("               Login - Turma")
        print("--------------------------------------------")

        try:
            id_turma = int(input("Digite o ID da turma que você deseja logar:\n"))
            turma_autenticada = autenticar_turma(id_turma)

            if turma_autenticada:
                portal_turma(turma_autenticada)
                break
            else:
                print("ID inválido!")

        except ValueError:
            print("[ERRO]: Digite um número!")