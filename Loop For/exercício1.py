while True:
    nota = float(input("Insira uma nota: "))

    if nota < 0 or nota > 10:
        print("A nota que você inseriu é inválida. Tente novamente.")
        continue
    else:
        print("Nota válida. Obrigado.")
        break