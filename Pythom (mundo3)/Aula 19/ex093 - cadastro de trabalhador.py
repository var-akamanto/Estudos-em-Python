import datetime
empregado = dict()
ano_atual = datetime.datetime.now().year
empregado['nome'] = (str(input('Nome do empregado : '))).title().strip()
ano_nasc = int(input('Ano de nascimento do empregado : '))
empregado['idade'] = ano_atual - ano_nasc
empregado['ctps'] = int(input('Numero da Carteira de Trabalho [0 se nao tiver]'))
if empregado['ctps'] != 0:
    empregado['Ano_Admissao'] = (int(input('Ano de admissão do empregado : ')))
    empregado['Salário'] = (float(input('Salário : R$')))
    empregado['tempo de empresa'] = ano_atual - empregado['Ano_Admissao']
    print(f'Informações sobre o empregado -=-={empregado["nome"]}-=-='.center(50))
    for keys, values in empregado.items():
        print(f'{keys} : {values}')
else:
    for k, v in empregado.items():
        print(f'{k} : {v}')