numero = input("Digite um numero entre 0 e 999: ")

if(int(numero) > 1000):
    print("Número invalido")
else:
    if(int(numero) >= 100):
        centena = int(numero[0])
        dezena = int(numero[1])
        unidade = int(numero[2])

        centena_texto = "Centenas"
        dezena_texto = "Dezenas"
        unidade_texto = "Unidades"

        if(centena == 1):
            centena_texto = "Centena"
        if(dezena == 1):
            dezena_texto = "Dezena"
        if(unidade == 1):
            unidade_texto = "Unidade"
        
        print(f"{numero} = {centena} {centena_texto}, {dezena} {dezena_texto} e {unidade} {unidade_texto}")
    
    elif(int(numero) >= 10 and int(numero) < 99 ):
        dezena = int(numero[0])
        unidade = int(numero[1])

        dezena_texto = "Dezenas"
        unidade_texto = "Unidades"

        if(dezena == 1):
            dezena_texto = "Dezena"
        if(unidade == 1):
            unidade_texto = "Unidade"
        
        print(f"{numero} = {dezena} {dezena_texto} e {unidade} {unidade_texto}")

    else:
        unidade = int(numero)

        unidade_texto = "Unidades"

        if(unidade == 1):
            unidade_texto = "Unidade"

        print(f"{numero} = {unidade} {unidade_texto}")