aluno = dict()
aluno["Nome"] = str(input('Nome do Aluno: ')).upper()
aluno["Media"] = float(input('Media : '))
if aluno["Media"] >= 6:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} - {v}')
