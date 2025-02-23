def leiaDinheiro(frase_input: str):
    verify = 1
    frase = f"{frase_input}"
    while verify == 1:
        frase_input = input(f"{frase}")
        frase_float = frase_input.strip()
        frase_float = frase_input.replace(",", ".")
        try:
            frase_float = float(frase_float)
        except:
            print("Erro!Digite um número válido.")
        if type(frase_float) is float:
            verify = 0
    return (frase_float)