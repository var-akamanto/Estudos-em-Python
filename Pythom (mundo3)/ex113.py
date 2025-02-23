def leiaInt(frase):
    while True:
        try:
            inteiro = int(input(frase))
        except:
            print("Erro!Digite um numero inteiro")
        else:
            break
    return print(f'Voce digitou o numero {inteiro}')

leiaInt('Digite um numero: ')