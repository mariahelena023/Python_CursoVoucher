n = int(input("Insira o número para ver a tabuada (1 a 10): "))

if 1 <= n <= 10:
    print(f"Tabuada do número {n}:")
    
    for i in range(1, 11):
        resultado = n * i
        print(f"{n} X {i} = {resultado}")
else:
    print("Erro ao escolher o número para tabuada. Por favor, informe um número de 1 a 10.")
