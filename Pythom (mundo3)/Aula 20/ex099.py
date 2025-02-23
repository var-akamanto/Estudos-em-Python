from random import randint


def linha():
    return print("-="*30)


def maior(*nums: list) -> int:
    maior = cont = 0
    for n in nums:
        if n > maior:
            maior = n
        cont += 1
    linha()
    print(f"Os valores digitados foram {nums}")
    print(f"Foram informados {cont} valores")
    print(f"O maior valor informado foi {maior}")
    return linha()


maior(1, 5, 3, 5, 3, 5, 7)
maior(3, 5, 8)
maior(5, 35, 6, 8, 89, 8, 0)
maior(0)
maior()
