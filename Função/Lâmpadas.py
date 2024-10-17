def calculo_lampadas():
    tiposEpotencias = {0:12, 1:15, 2:18, 3:20, 4:22}

    while True:
        print(30 * "--")
        print("---TABELA---")
        print("- Tipo 0 (0)")
        print("- Tipo 1 (1)")
        print("- Tipo 2 (2)")
        print("- Tipo 3 (3)")
        print("- Tipo 4 (4)")
        print("- Sair (-1)")
        print("")

        tipo = int(input("Insira aqui o tipo que você deseja: "))
        print(30 * "--")

        if tipo == -1:
            print("")
            print("Saindo do sistema...")
            print("")
            break

        largura = float(input("Insira aqui a largura do cômodo: "))
        comprimento = float(input("Insira aqui o comprimento do seu cômodo: "))
        print(30 * "--")

        area = largura * comprimento

        numero_lampadas =  area / tiposEpotencias[tipo]

        print(f"O número de lâmpadas de 60 watts necessárias para iluminar seu cômodo é: {numero_lampadas}")

calculo_lampadas()
