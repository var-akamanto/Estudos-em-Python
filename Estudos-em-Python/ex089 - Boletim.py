#Feito pra estudo de listas
from time import sleep as s
boletim = []
aluno = []
nota = []
aprovados = []
cont_aluno = 0
print('-=-=-=Instituto Federal de Santa Catarina-=-=-='.center(70))
print("Gerador de boletim".center(70))
print("Média necessária para aprovação : 5 ".center(70))

while True:
    print(f"-=-=-=-=-=-=-=-=-=Aluno {cont_aluno}-=-=-=-=-=-=-=-=-=".center(70))
    aluno.append(str(input("Nome do aluno: ")))
    if aluno[-1] == "":
        print("ERRO! Nome é obrigatório.")
        break
    nota.append(float(input("Nota 1 : ")))
    nota.append(float(input("Nota 2 : ")))
    if nota[0] > 10 or nota[1] > 10:
        print("ERRO! Digite as notas corretamente.")
        break
    cont_aluno += 1
    media = (float(nota[0]) + float(nota[1])) / 2
    if media >= 5:
        aprovados.append(aluno[-1])
    print(aprovados)
    aluno.append(nota[:])
    nota.clear()
    aluno.append(media)
    boletim.append(aluno[:])
    aluno.clear()

    resp = str(input("Quer continuar? [S/N]"))
    if resp in 'Nn':
        break

print('Aguarde, estamos preparando seu boletim...')
s(2)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=Boletim-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='.center(70))
for index, aluno in enumerate(boletim):
    print()
    print(
        f'{index:>10}{boletim[index][0]:>15}{boletim[index][2]:>10}'.center(70))
print()

while True:
    opcoes = int(input(
        """    
    [1] Ver Notas
    [2] Gerar lista de aprovados
    [3] Finalizar o programa
    """
    ).center(70))
    if opcoes == 3:
        break
    elif opcoes == 1:
        s(0.7)
        cod_aluno = int(
            input("Digite o numero do aluno que deseja olhar as notas: "))
        print()
        print(
            f'({cod_aluno}) -> {boletim[cod_aluno][0]
                                } - {boletim[cod_aluno][1]}'.center(70)
        )
        print()
    elif opcoes == 2:
        s(0.7)
        for aluno in aprovados:
            print(f'{aluno} - APROVADO')
print("-=-=-=-=-=-=-=-=-=-=-=FIM-=-=-=-=-=-=-=-=-=-=-=".center(70))
