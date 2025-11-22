from limpar_tela.limpar_tela import limpar_tela
from turmas.cadastramento_turma import cadastramento_turma
from turmas.crud_turmas import listar_turmas, buscar_turma, atualizar_turma, deletar_turma
from turmas.validar_turma import validar_dia_semana, validar_horario

def atualizar_turma(id_turma: int):
    menu = ["Atualizar Horário", "Atualizar Turma", "Voltar"]

    while True:
        limpar_tela()
        print("--------------------------------------------")
        print("              Escola de Idiomas             ")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    while True:
                        novo_dia_semana = input("Digite o novo nome da semana da turma: ")
                        erro_novo_dia_semana = validar_dia_semana(novo_dia_semana)

                        if erro_novo_dia_semana:
                            print(erro_novo_dia_semana)
                        else:
                            atualizar_turma(id_turma, novo_dia_semana, "dia_semana", "Dia da semana")
                        break

                case 2:
                    while True:
                        novo_horario = input("Digite o novo horário da turma: ")
                        erro_novo_horario = validar_horario(novo_horario)

                        if erro_novo_horario:
                            print(erro_novo_horario)
                        else:
                            atualizar_turma(id_turma, novo_horario, "horario", "Horário")
                        break

                case 3:  
                    print("Voltando...")
                    break
                case _:
                    print("Digite uma opção válida!")

        except ValueError:
            print("[ERRO]: Digite um número!")