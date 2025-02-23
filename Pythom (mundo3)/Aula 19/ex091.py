from random import randint as dado
from time import sleep as perai
players1 = list()
jogadas = list()
players2 = dict()
maior = int
print('-=-Jogando os dados-=-'.center(50))
for c in range(1, 5):
    vDado = dado(1, 6)
    print(f'Jogador {c} jogou o número {vDado}')
    # perai(0.6)
    players1.append(f'Jogador {c}')
    players2["nomes"] = players1.copy()
    jogadas.append(vDado)
    players2["jogadas"] = jogadas
print('-=-Ranking-=-'.center(50))


# players2["ranking"] = sorted(players2['jogadas'], reverse=True)

print(players2['mergeNJ'])
