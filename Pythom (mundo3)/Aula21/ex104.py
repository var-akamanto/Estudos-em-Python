def leiaInt(frase):
    inteiro = input(frase)
    while inteiro.isnumeric() is False:
        print("Digite um numero inteiro.")
        inteiro = input(frase)
    inteiro = int(inteiro)
    return print(f'Voce digitou o numero {inteiro}')

leiaInt('Digite um numero: ')