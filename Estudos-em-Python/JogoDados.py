from random import randint
from operator import itemgetter
from time import sleep as calmaporra
jogo = dict()
print('-=-Jogando os dados-=-'.center(50))
for nomes in range(1, 5):
    jogo[f"Jogador {nomes}"] = randint(1, 6)  # joga o dado de cada player
for keys, values in jogo.items():  # mostra as jogadas de cada player na tela
    print(f'{keys} caiu no numero {values}'.center(50))
    calmaporra(0.7)
print('Aguarde! Estamos gerando a classificação geral . . .')
calmaporra(2)
print('-=-Ranking-=-'.center(50))
ranking = sorted(
    jogo.items(), key=itemgetter(1), reverse=True   #cria o ranking baseado nas jogadas
)
c = 1
for players, values in ranking:
    print(f'{c} º Lugar - {players} - {values}'.center(50))   #mostra o ranking
    c += 1