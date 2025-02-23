dois_pos = list()
lista = list()
for n in range(1,6):
    lista.append(int(input('digita ai ')))
print(lista)
for index, valor in enumerate(lista) :
    if valor == 2:
        dois_pos.append(index)


print(f'O 2 ta nas posicoes {dois_pos}')


