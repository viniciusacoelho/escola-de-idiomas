from cursos import menu_cursos

def administrador():
    menu = ["Cursos", "Professores", "Alunos", "Turmas"]
    
    while True:
        print("--------------------------------------------")
        print("              Escola de Idiomas")
        print("--------------------------------------------")

        for i in range(len(menu)):
            print(f"{i - 1} - {menu[i]}")

        try:
            opcao = input("Digite uma opção: ")
            match opcao:
                case 1:
                   menu_cursos() 
                case 2:
                   menu_professores()
                   pass 
                case 3:
                   menu_alunos()
                   pass 
                case 4:
                   menu_turmas()
                   pass 
                case _:
                   print("Opção inválida!")
        
            break
        except ValueError:
            print("[ERRO]: Digite um número!")

