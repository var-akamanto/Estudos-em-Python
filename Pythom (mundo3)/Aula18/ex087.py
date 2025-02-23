# Soma de todos os valores pares digitados (feito)
# soma dos valores da terceira coluna (feito)
# o maior valor da segunda linha (feito)


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
linha3 = []
ver_num = soma_par = soma_coluna3 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = input(
            (f"Digite o valor para a posição [{linha}],[{coluna}] : "))
        if coluna == 2:  # verificar se o numero esta na coluna 3
            soma_coluna3 += int(matriz[linha][coluna])
        ver_num = int(matriz[linha][coluna])
        if ver_num % 2 == 0:  # verificar se é par
            soma_par += ver_num
        if linha == 1:  #verificar se o numero esta na terceira linha
            linha3.append(int(matriz[linha][coluna]))
print("-=-="*25)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]}]", end=" ")
    print()
print(f"A soma dos valores pares é {soma_par}")
print(f"A soma dos valores da terceira coluna é {soma_coluna3}")
linha3.sort()
print(f"O maior valor da terceira linha é o numero {linha3[2]}")
