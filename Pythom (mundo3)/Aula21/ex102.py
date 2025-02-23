def fatorial(num: int = 1, show: bool = False) -> int:
    """
    Retorna o fatorial de um numero n
    n -> numero inteiro
    show -> mostrar ou não o processo de contagem, falso por padrão
    return -> fatorial de n
    """
    fatorial = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print('*', end='')
            else:
                print('=', end='')
        fatorial *= c
    return print(fatorial)
while True:
    num_fatorial = int(input("Deseja ver o fatorial de qual numero?\n"))
    show = int(input("""Deseja ver a operação completa?
                        [0] Não
                        [1] Sim\n"""))
    while show < 0 or show > 1:
        print("Digite uma resposta valida\n")
        show = int(input("""Deseja ver a operação completa?
                        [0] Não
                        [1] Sim\n"""))
    if show == 0:
        show = False
    else:
        show = True
    fatorial(num_fatorial, show=show)
    resp = str(input("Quer continuar ? [S/N]")).upper()[0]
    if resp in 'Nn':
        print("FIM!")
        break
    while resp not in 'NnSs':
        print("Responda corretamente.")
        resp = str(input("Quer continuar ? [S/N]")).upper()[0]
