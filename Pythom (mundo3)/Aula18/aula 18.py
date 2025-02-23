temp = []
princ = []
maior = menor = 0

while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso :")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input("Quer continuar?"))
    if resp in 'Nn':
        break

print(f"Ao todo, voce cadastrout {len(princ)} pessoas")
print(f"O maior peso registrado foi {maior}, peso de ", end="")
for p in princ:
    if p[1] == maior:
        print(f"[{p[0]}]", end='')
print(f"O menor peso registradi foi de {menor}, peso de ", end="")
print()
for p in princ:
    if p[1] == menor:
        print(f"[{p[0]}]", end="")
print()
