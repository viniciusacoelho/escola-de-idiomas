from alunos.crud_alunos import listar_alunos
from cursos.crud_cursos import listar_cursos
from professores.crud_professor import listar_professores

def verificar_unique(tipo: str, parametro: str, posicao = int, nome = str) -> str:
    """
    Verifica se os dados únicos já foram cadastrados anteriormente no banco de dados.
    
    Args:
        tipo (str): O sistema está verificando se é 'Alunos' ou 'Cursos'.
        parametro (str): Os dados que o sistema vai verificar.
        posicao (int): Posição dos dados no banco de dados.
        nome (str): Os dados que o sistema vai verificar para mensagem.

    Returns:
        str: 'nome' já cadastrado anteriormente.
    """
    if tipo == "Alunos":
        itens = listar_alunos()
    elif tipo == "Cursos":
        itens = listar_cursos()
    elif tipo == "Professores":
        itens = listar_professores()
        
    lista_cadastrados = []

    for item in itens:
        lista_cadastrados.append(item[posicao])

    for item in itens:
        if parametro in lista_cadastrados:       
            return f"{nome} '{parametro}' já cadastrado anteriormente."