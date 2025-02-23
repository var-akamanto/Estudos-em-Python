Dados1 = []
Dados2 = []

Lista_Maior = []  #lista final que mostra o mais pesado, ou os mais pesados, se houver valor igual.
Pivo_Maior =[]    #todos os numeros maiores que o primeiro numero da lista.

while True:   #cadastrar as pessoas
    Dados1.append(str(input('Nome : ')))
    Dados1.append(int(input('Peso : ')))
    resp = input('Quer continuar? [s/n]')              
    Dados2.append(Dados1[:])
    Dados1.clear()  
    if resp in ('N', 'n'):
        break

print(f'{len(Dados2)} pessoas foram cadastradas no sistema.')       #quantas pessoas
print("Lista das pessoas mais pesadas:")
print("Lista das pessoas mais leves : ")