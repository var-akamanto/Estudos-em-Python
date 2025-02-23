maior = menor = 0
valores = list()
pos_maior = list()
pos_menor = list()
for ind, num in enumerate(range(1, 6)):
    ind = ind + 1
    valores.append(int(input(f'Digite o {ind}º valor : ')))

print('-=-='*10)

print(f'Você digitou a lista {valores}')

for n in valores:
    if n > maior:  # maior numero
        maior = n
for index_maior, numero_maior in enumerate(valores): #posicao do maior numero\
    if numero_maior == maior:
        pos_maior.append(index_maior + 1)


if 0 in valores:
    menor = 0
else:
    menor = valores[0]
    for n in valores:     # menor numero
        if n < menor:
            menor = n
for index_menor,numero_menor in enumerate(valores) :  #posicao do menor numero
    if numero_menor == menor:
        pos_menor.append(index_menor + 1 )

print(f'O maior numero digitado foi {maior} nas posições ',end='')
for n_pos_maior in pos_maior:  #formatar as posicoes
    print(f'{n_pos_maior}',end='..')
print('')
print(f'O menor numero digitado foi {menor} nas posições ', end='')
for n_pos_menor in pos_menor:  #formatar as posicoes
    print(f'{n_pos_menor}',end='..')
print('')