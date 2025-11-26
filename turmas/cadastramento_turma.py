from limpar_tela.limpar_tela import limpar_tela
from turmas.crud_turmas import cadastrar_turma
from turmas.validar_turma import validar_dia_semana, validar_horario

def cadastramento_turma():
    """Página de cadastro da turma."""
    limpar_tela()
    print("--------------------------------------------")
    print("              Escola de Idiomas             ")
    print("--------------------------------------------")

    while True:
        dia_semana = input("Digite o dia da semana: \n")
        erro_novo_dia_semana = validar_dia_semana(dia_semana)

        if erro_novo_dia_semana:
            print(erro_novo_dia_semana)
            print("--------------------------------------------")
        else:
            break

    while True:
        print("--------------------------------------------")
        horario = input("Digite os horários de início e de término da turma (Ex.: 08:30-10:30): \n")
        erro_horario = validar_horario(horario)

        if erro_horario:
            print(erro_horario)
        else:
            break

    cadastrar_turma(dia_semana, horario)