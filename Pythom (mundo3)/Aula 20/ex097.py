def escreva(texto):
    print("-"*len(texto))
    print(f"{texto}".center(len(texto)))
    print("-"*len(texto))
    
texto = str(input("Digite seu texto :"))
print(escreva(texto))