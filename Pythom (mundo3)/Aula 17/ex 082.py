list = []
pares = []
impares = []

while True:
    list.append(int(input('Digite um número: ')))
    resp = input ('Quer continuar? [S/N]')
    if resp in ('Nao', 'NAO', 'N', 'n') :
        break
list.sort()

for n in list:
    if (n % 2) == 0 :
        pares.append(n)
        pares.sort
    else :
        impares.append(n)
        impares.sort()
print('-=-=-=-='*15)
print(f'Todos os valores : {list}')
print(f'Numeros pares: {pares}')
print(f'Numeros impares : {impares}')
