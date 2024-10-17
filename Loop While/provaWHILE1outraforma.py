numero = input("Insira um número: ")
soma = 0

while True:
    
    if int(numero) > 0:
        while numero != "":
            soma = soma + int(numero[0])
            numero = numero[1:]
    
    elif int(numero) == 0:
        break

    print(soma)