def area(largura,comprimento):
    area = largura * comprimento
    area = (f"A area do seu terreno é {area}")
    return area

l = float(input("Digite a largura do terreno :"))
c = float(input("Digite o comprimento do terreno :"))
print(area(l,c))