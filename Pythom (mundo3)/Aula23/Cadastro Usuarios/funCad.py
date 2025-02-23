def criaarquivo():
    nome_arquivo = "Cadastro de pessoas.txt"
    try:
        open(nome_arquivo, "a")
    except:
        print("Não consegui criar o arquivo de texto.")
    else:
        return_arquivo = nome_arquivo
    finally:
        return return_arquivo


def addnome(nome: str, idade: int):
    nome_arquivo = criaarquivo()
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(f"{nome};{idade}\n")


def lertxt():
    nome_arquivo = criaarquivo()
    with open(nome_arquivo, "rt") as arquivo:
        for linha in arquivo:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")


def limpartxt():
    nome_arquivo = criaarquivo()
    open(nome_arquivo, "w").close()


criaarquivo()
addnome("Pedro", 18)
addnome("ana", 26)
lertxt()
