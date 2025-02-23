def fatorial(n):
    fatorial = 1
    for n in range(1, n+1, 1):
        fatorial *= n
    return fatorial


num = int(input('Digite um numero : '))
print(fatorial(num))
