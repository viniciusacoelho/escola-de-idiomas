from alunos.crud_alunos import login

def login_aluno():
    print("--------------------------------------------")
    print("              Escola de Idiomas")
    print("--------------------------------------------")
    print("Começe a aprender agora!")
    usuario = input("Digite seu usuário: ").lower()
    senha = input("Digite sua senha: ")

    login(usuario, senha)