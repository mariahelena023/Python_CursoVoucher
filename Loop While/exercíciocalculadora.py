while True:
    print(" ")
    print("CALCULADORA:")
    print("1 - Multiplicação")
    print("2 - Divisão")
    print("3 - Adição")
    print("4 - Subtração")
    print("5 - Sair")
    print(" ")

    opcao = int(input("Escolha o tipo de operação que será realizada (1/2/3/4/5): "))
    print(" ")

    if opcao == 5:
        print("Adeus, até a próxima...")
        break

    if opcao not in [1,2,3,4]:
        print("Essa opção não existe. Escolha uma opção existente, por favor.")
        continue

    a = float(input("Insira aqui o valor do primeiro número: "))
    b = float(input("Insira aqui o valor do segundo número: "))
    print(" ")
    
    if opcao == 1:
        resultado = a * b
        print("O  resultado dessa  multiplicção é: ", resultado)
    elif opcao == 2:
        resultado = a / b
        print("O resultado dessa divisão é: ", resultado)
    elif opcao == 3:
        resultado = a + b
        print("O resultado dessa adição é: ", resultado)
    elif opcao == 4:
        resultado = a - b
        print("O resultado dessa subtração é: ", resultado)



