import re

def validar_dia_semana(dia_semana: str) -> str | None:
    """Valida o dia da semana da turma."""
    dias_semana = [
        "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo",
        "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"
    ]
    # TODO: Permitir o usuário não digitar exatamente como está na lista
    if dia_semana not in dias_semana:
            return "Dia da semana inválido! Esperava-se: 'Segunda ou Segunda-Feira'"
    
def validar_horario(horario: str) -> str | None:
    """Valida o horário da turma."""
    regex_horario = r"^[0-9]{2}:[0-9]{2}-[0-9]{2}:[0-9]{2}$"
    if not re.match(regex_horario, horario):
        return "Dia da semana inválido! Esperava-se: '12:34-56:78'"    