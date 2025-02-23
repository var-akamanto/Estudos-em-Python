list = []
pos_5 = []
resp = 'S'
lista_resp = ('sim', 'SIM', 'S', 's')

while resp in lista_resp:
    list.append(int(input('Digite um número: ')))
    resp = input ('Quer continuar? [S/N]')
list.sort(reverse=True)
print('FIM')
print('-=-=-='*15)
print(f'Foram digitados {len(list)} números.')
print(f'A lista na ordem decrescente: {list}')
if 5 in list:
    for pos, n in enumerate(list):
        if n == 5:
            pos_5.append(pos)
    print(f'O numero 5 está nas posições {pos_5}.')
else:
    print('O numero 5 não está na lista')