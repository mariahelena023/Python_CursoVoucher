soma = 0

while True:
    numero = int(input("Insira o número que você deseja adicionar a soma(caso queira encerrar digite 0): "))

    if numero > 0:
        while numero != 0:
            soma += numero % 10
            numero = numero // 10

    elif numero == 0:
        print(f"A soma dos números foi: {soma}")
        break

    else:
        print("Número inválido.")