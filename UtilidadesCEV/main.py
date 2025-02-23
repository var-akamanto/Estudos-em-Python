from uteis import moeda
from uteis import dado
moeda.linha(25)
valor = dado.leiaDinheiro("Digite um Valor : ")
aumento = float(input("Quantos % de aumento :"))
decremento = float(input("Quantos % de decremento :"))
moeda.linha(25)
moeda.resumo(valor, aumento, decremento)
moeda.linha(25)
