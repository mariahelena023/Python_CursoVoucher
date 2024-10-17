def imprimir_quantidade(numero):
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero% 10

    if centenas == 1:
        centenas_str = "centena"
    else:
        centenas_str = "centenas"

    if dezenas == 1:
        dezenas_str = "dezena"
    else:
        dezenas_str = "dezenas"

    if unidades == 1:
        unidades_str = "unidade"
    else:
        unidades_str = "unidades"

    print(f"{numero} = {centenas} {centenas_str}, {dezenas} {dezenas_str} e {unidades} {unidades_str}")

numero = int(input("Insira um número inteiro maior que 0 e menor que 1000: "))
imprimir_quantidade(numero)