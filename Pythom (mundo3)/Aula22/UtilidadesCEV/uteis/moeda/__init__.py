def moeda(valor):
    valor = float(valor)
    formatado = f"R${valor:.2f}".replace(".", ",")
    return formatado


def aumentar(valor: float = 0, porcentagem: float = 0, format=True):
    novo_valor = ((porcentagem/100) * valor) + valor
    return moeda(novo_valor) if format is True else novo_valor


def diminuir(valor: float, porcentagem: float, format=True):
    novo_valor = valor - ((porcentagem/100) * valor)
    return moeda(novo_valor) if format is True else novo_valor


def dobro(valor, format=True):
    dobro = valor*2
    return moeda(dobro) if format is True else dobro


def metade(valor, format=True):
    metade = valor / 2
    return moeda(metade) if format is True else metade


def linha(size: int):
    print("-=" * size)


def linha_texto(txt: str):
    print("-"*len(txt))


def resumo(valor=0, aumento=0, decremento=0):
    linha_texto("Resumo do Valor".center(40))
    print("Resumo do Valor".center(40))
    linha_texto("Resumo do Valor".center(40))
    print(f"Preço Analisado:\t\t{moeda(valor)}")
    print(f"Dobro do preço:\t\t\t{dobro(valor)}")
    print(f"Metade do preço:\t\t{metade(valor)}")
    print(f"Aumento de {aumento}%:\t\t{aumentar(valor, aumento)}")
    print(f"Decremento de {decremento}%:\t\t{
          diminuir(valor, decremento)}")
