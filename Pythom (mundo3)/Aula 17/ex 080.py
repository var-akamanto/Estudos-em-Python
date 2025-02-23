list = list()
index = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto']

print(index)
for valores in range(0,5):
    n = (int ( input ( f'Digite o {index[0]} valor:\n') ) )
    index.pop(0)
    if valores == 0 or n > list[-1]:
        list.append(n)
        print('Numero adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len (list) :
            if n <= list[pos] :
                list.insert(pos,n)
                print(f'Numeros digitados na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados, em ordem, foram {list}')