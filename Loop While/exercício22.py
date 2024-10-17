numero = int(input("Insira um número: "))

contador = 1

while contador * (contador + 1) * (contador + 2) < numero:
    contador = contador + 1

    while contador * (contador + 1) * (contador + 2) == numero:
        print(f"{numero} é um produto de {contador}*{contador + 1}*{contador + 2}")
        break
    else:
        print(f"{numero} não é triangular.")
        break

