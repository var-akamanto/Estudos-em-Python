'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um 
jogador de futebol. O programa vai ler o nome do 
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gol
s feitos em cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.*'''

'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vári
os jogadores, incluindo um sistema de visualização de 
detalhes do aproveitamento de cada jogador.'''
jogador = {}
jogadores = []
while True:
    jogador["nome"] = str(input("Nome do jogador : ")).capitalize()
    jogador["qtd_partidas"] = int(input("Quantidade de partidas : "))
    tot_gols = 0
    for jogos in range(jogador["qtd_partidas"]):
        jogador[f"partida {jogos}"] = int(
            input(f"Gols na partida {jogos + 1} : "))
        tot_gols += jogador[f"partida {jogos}"]
    jogador["tot_gols"] = tot_gols
    resp = str(input("Quer continuar? [S/N]")).upper()[0]
    jogadores.append(jogador.copy())
    if resp == 'N':
        break
print()
for k, v in enumerate(jogadores):
    print(f'{k:>3}', end='')
    for values in v.values():
        print(f"{str(values):<15}", end='')
        print()
print()