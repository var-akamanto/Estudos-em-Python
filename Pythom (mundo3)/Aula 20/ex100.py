from random import randint


def sorteia(lista: list) -> list:
    lista = [randint(0, 100) for x in range(1, 6)]
    return lista


def soma_par(lista) -> list:
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    return soma


lista = []
lista = sorteia(lista)
print(f"Os valores sorteados foram {(sorteia(lista))}")
print(f"A soma dos valores pares é {soma_par(lista)}")
