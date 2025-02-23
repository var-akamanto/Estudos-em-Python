principal = [[], []]
valor = 0
c = 1
for n in range(0,7):
    valor = (int(input(f"Digite o {c} numero: ")))
    c += 1
    if valor % 2 == 0:
        principal[0].append(valor)
    else :
        principal[1].append(valor)  
print()
principal[0].sort()
principal[1].sort()
print(f"Os numeros pares são {principal[0]}")
print(f"Os numeros impares são {principal[1]}")