"""
–Quantidade de notas                                                                                                                                                 
 –A maior nota                                                                                                                                                               
   –A menor nota
    –A média da turma                                                                                                                                                      
      –A situação (opcional)
"""

def notas(*nota, sit=False):
    notas = {}
    notas_provisorio = []
    maior = media = 0
    for n in nota:
        notas_provisorio.append(n)
    notas["qtd_notas"] = len(notas_provisorio)
    print(f"Foram digitadas {notas['qtd_notas']} notas")
    menor = notas_provisorio[0]
    for n in notas_provisorio:
        media += n
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    notas["maior_nota"] = maior
    print(f"A maior nota é {notas['maior_nota']}")
    notas["menor_nota"] = menor
    print(f"A menor nota é {notas['menor_nota']}")
    notas["media"] = float(media) / notas["qtd_notas"]
    print(f"A media das notas é {float(notas["media"]):.2f}")
    if sit:
        if notas["media"] > 6:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"
        print(situacao)

notas(3, 6, 9, 1, 5, 3, 4, 7, 4, 2, 5, 9, sit=True)
