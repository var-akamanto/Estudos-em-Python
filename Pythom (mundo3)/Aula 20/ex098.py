from math import fabs
from time import sleep


def linha():
    return print("-="*30)


def contador(inicio, fim, passo):
        if passo == 0:
            passo = 1
        if inicio > fim:
            n = -1
        else:
            n = 1
        linha()
        print(f"Contagem de {inicio} ate {fim}, de {int(fabs(passo))} em {int(fabs(passo))}")
        for n in range(inicio, fim + n, passo):
            print(n, end=" ")
        print("Fim!")
        linha()


contador(1, 10, 1)
sleep(1)
contador(10, 0, -2)
sleep(1)
linha()
print("Agora é a sua vez de personalizar a contagem!")
while True:
    inicio =  int(input("Inicio :"))
    fim = int(input("Fim :"))
    passo = int(input("Passo :"))
    sleep(1)
    contador(inicio,fim,passo)
    resp = int(input("Digite 0 pra parar ou 1 pra continuar :"))
    if resp == 0:
        break