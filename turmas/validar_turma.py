import re

def validar_dia_semana(dia_semana: str) -> str | None:
    """
    Valida o dia da semana da turma, verificando se ele está entre os dias inseridos na lista.

    Args:
        dia_semana (str): Dia da semana da turma.

    Returns:
        str: Dia da semana inválido!
            Esperava-se: 'Segunda ou Segunda-Feira'.
    """
    dias_semana = [
        "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo",
        "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"
    ]
    if dia_semana not in dias_semana:
        return "Dia da semana inválido! Esperava-se: 'Segunda ou Segunda-Feira'."

def validar_horario(horario: str) -> str | None:
    """
    Valida o horário da turma, verificando a sua estrutura.

    Args:
        horario (str): Horário da turma.

    Returns:
        str: Horário inválido!
            Esperava-se: '12:34-56:78'.
    """
    regex_horario = r"^[0-9]{2}:[0-9]{2}-[0-9]{2}:[0-9]{2}$"
    if not re.match(regex_horario, horario):
        return "Horário inválido! Esperava-se: '12:34-56:78'."