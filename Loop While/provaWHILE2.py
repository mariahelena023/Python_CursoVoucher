while True: 
    print(30 * "--")
    print("___CALCULADORA___")
    print("- Adição (1)")
    print("- Subtração (2)")
    print("- Multiplicação (3)")
    print("- Divisão (4)")
    print("- Sair da calculadora (5)")
    print(" ")

    operacao = int(input("Insira aqui a operação que deseja realizar: "))
    print(" ")

    if operacao == 5:
        print("Ok, até a próxima.")
        print(30 * "--")
        break

    elif operacao not in [1,2,3,4,5]:
        print("!!! NÚMERO DIGITADO NÃO ESTÁ DENTRO DO MENU. POR FAVOR, TENTE NOVAMENTE. !!!")
        print(" ")
        continue
    
    elif operacao == 1:
        
        a = float(input("insira aqui o seu primeiro número: "))
        b = float(input("insira aqui o seu segundo número: "))
        soma = a + b

        print(f"RESULTADO: {soma}")

    elif operacao == 2:
        
        a = float(input("insira aqui o seu primeiro número: "))
        b = float(input("insira aqui o seu segundo número: "))
        subtracao = a - b

        print(f"RESULTADO: {subtracao}")

    elif operacao == 3:
        
        a = float(input("insira aqui o seu primeiro número: "))
        b = float(input("insira aqui o seu segundo número: "))
        multiplicacao = a * b

        print(f"RESULTADO: {multiplicacao}")

    elif operacao == 4:
        
        a = float(input("insira aqui o seu primeiro número: "))
        b = float(input("insira aqui o seu segundo número: "))
        divisao = a / b

        print(f"RESULTADO: {divisao}")