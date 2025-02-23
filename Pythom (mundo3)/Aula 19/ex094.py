'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um 
jogador de futebol. O programa vai ler o nome do 
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gol
s feitos em cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.*'''
jogador = dict()
partidas = dict()
tot_gols = 0
jogador["nome"] = str(input('Nome do Jogador: '))
jogador["quant_partidas"] = int(input("Quantidade de partidas : "))
for partida in range(jogador["quant_partidas"]):
    partidas[f"{partida}"] = int(input(f'Gols na partida {partida + 1}: '))
    tot_gols += partidas[f"{partida}"]
jogador["tot_gols"] = tot_gols
jogador["aproveitamento"] = (jogador["tot_gols"]/jogador["quant_partidas"])*100
jogador['gols_por_partida'] = partidas.copy()
print(f'{jogador["nome"]} teve um aproveitamento de {jogador["aproveitamento"]}%')