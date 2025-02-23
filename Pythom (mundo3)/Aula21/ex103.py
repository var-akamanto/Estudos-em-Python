def ficha(nome, gols=0):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} gols no campeonato.'


nome = (input("Nome do jogador : "))
qtd_gols = (input(f"Quantos gols {nome} marcou? "))

print(ficha(nome, qtd_gols))
