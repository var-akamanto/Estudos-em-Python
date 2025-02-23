def menu():
    from time import sleep
    import funCad
    print(f"Arquivo {funCad.criaarquivo()} criado com sucesso.")
    while True:
        option = 0
        try:
            print("-="*len("\t\tMenu Principal"))
            print("\tMenu Principal")
            print("-="*len("\t\tMenu Principal"))
            option = int(input("""
[1] - Ver pessoas cadastradas
[2] - Cadastrar nova pessoa
[3] - Limpar listagem de pessoas                          
[4] - Sair do Sistema\n"""))
        except:
            print("Erro! Você digitou uma letra ou uma palavra. Digite uma opção válida")
        finally:
            if option == 1:
                print(f"{"Nome":<30}{"Idade":>3}")
                funCad.lertxt()
            elif option == 2:
                nome = str(input("Digite o nome que deseja cadastrar : "))
                idade = int(input(f"Digite a idade de {nome} : "))
                funCad.addnome(nome, idade)
                print("Nome adicionado com sucesso.")
            elif option == 3:
                funCad.limpartxt()
            elif option > 4 or option < 1:
                print("Digite uma opção válida.")
            elif option == 4:
                print("Finalizando tarefa. . .")
                sleep(2)
                print("Processo finalizado. Até a próxima!")
                break
