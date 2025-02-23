'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias
pessoas, guardando os dados de cada pessoa em um dicionário e todos os dici
onários em uma lista. No final, mostre: A) Quantas pessoas foram cadastrada
s B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas c
om idade acima da média'''
pessoa = {}
pessoas = []
media = 0
c = 1
while True:
    print(f"------Pessoa {c}------".center(50))
    pessoa["nome"] = str(input("Nome : ")).capitalize()
    while True:
        pessoa["sexo"] = str(input("Sexo [M/F] : ")).upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Digite um sexo valido.")
    pessoa["idade"] = int(input("Idade : "))
    media += pessoa["idade"]
    c += 1
    pessoas.append(pessoa.copy())
    resp = str(input("Quer continuar? [S/N]")).upper()[0]
    if resp in 'N':
        break
print("-="*30)
print(f"{len(pessoas)} foram cadastradas.")
media = media / len(pessoas)
print(f"A media de idade é {media}")
print("As mulheres digitadas são : ")
for pessoa in pessoas:
    if pessoa["sexo"] == 'F':
        print(pessoa["nome"],end=" ")
print()
print("As pessoas com a idade acima da media sao : ")
for pessoa in pessoas:
    if pessoa["idade"] > media:
        print(pessoa)
