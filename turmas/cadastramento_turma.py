from limpar_tela.limpar_tela import limpar_tela
from turmas.crud_turmas import cadastrar_turma

def cadastramento_turma():
    limpar_tela()
    print("--------------------------------------------")
    print("              Escola de Idiomas             ")
    print("--------------------------------------------")

    dia_semana = input("Digite o dia da semana: \n")
    horario = input("Digite os horários de início e de término da turma (Ex.: 08:30-10:30): \n")
    
    cadastrar_turma(dia_semana, horario)