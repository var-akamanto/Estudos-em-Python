parenteses = []

expressao = input('Digite uma expressão numérica:\n')

for letra in expressao :
    if letra == '(' or letra == ')' :
        parenteses.append(letra)

cont_parenteses = len(parenteses)
if (cont_parenteses % 2 == 0) :
    print('A expressão é válida.')
else:
    print('A expressão NÃO é válida.')