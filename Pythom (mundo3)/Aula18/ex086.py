matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = input(
            (f"Digite o valor para a posição [{linha}],[{coluna}] : "))
print("-=-="*25)
for linha in range(0, 3): 
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]}]", end=" ")
    print()