# pessoas = {'nome': 'Pedro', 'sexo': 'M', 'idade': 22}
# print(f"O {pessoas["nome"]} tem {pessoas["idade"]} anos e é {pessoas['sexo']}")

# pessoas['nome'] = 'Gabriel'
# pessoas['peso'] = 67

# for keys, values in pessoas.items():
# print(f'{keys} - {values}')
""""brasil = list()
estado = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado)
brasil.append(estado2)

print(estado.keys())
print(estado2.keys())

for k, v in enumerate(brasil):
    print(f'{brasil[k]["uf"]} - {brasil[k]["sigla"]}')"""

estado = dict()
brasil = list()

for e in range(0, 3):
    estado['uf'] = str(input('Estado : ')).title()
    estado['sigla'] = str(input('Sigla :')).upper()
    brasil.append(estado.copy())

print('-='*50)
for k, v in enumerate(brasil):
    print(f'{brasil[k]["uf"]} - {brasil[k]["sigla"]}')
print('-='*50)
for estado in brasil:
    for v in estado.values():
        print(f'{v}', end='')
        print()

