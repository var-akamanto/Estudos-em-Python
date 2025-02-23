from time import sleep
from random import randint
from random import sample
palpites = []
print("PALPITES DA MEGA")
n_palp = int(input("Quantos palpites você deseja obter?\n"))
for n in range(0, n_palp):
    palpites.append(sample(range(0, 61), 6))
    print(palpites)
    palpites.clear()
    sleep(0.4)