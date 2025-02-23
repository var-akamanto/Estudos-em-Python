resp = 1
lista = list()
while resp == 1:
    lista.append(int(input('Digite um valor: ')))
    numero = lista[-1]
    if numero in lista[:-1]:
        print('ERRO! Valor já adicionado anteriormente.')
        lista.pop()
    else:
            print('Valor adicionado com sucesso!')
    resp = int(input('Quer continuar?\n[1]SIM\n[2]NÃO\n'))
print('FIM. Valores adicionados!')
lista.sort()
print(f'Os valores adicionados foram {lista}')