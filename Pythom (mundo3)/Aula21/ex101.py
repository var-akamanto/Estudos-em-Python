import datetime
ano_atual = datetime.date.today().year


def votar(ano_nasc : int =0):
    """
    Recebe o ano de nascimento e retorna a situaçao eleitoral
    Entre 16 e 18 : Voto facultativo
    Maior que 70 : Voto facultativo
    Menor que 16 : Voto negado
    Maior de 18 : Voto Obrigatorio
    """
    global ano_atual
    idade: int = ano_atual - ano_nasc
    resp = str
    if 18 > idade >= 16 or idade >= 70:
        resp = "Voto Facultativo"
    elif idade < 16:
        resp = "Voto Negado"
    else:
        resp = "Voto Obrigatorio"
    return resp


ano_nasc = int(input("Ano de nascimento\n"))
print(votar(ano_nasc))
