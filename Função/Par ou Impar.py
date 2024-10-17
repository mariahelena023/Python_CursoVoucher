numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = 0
impares = 0

def verificar_par_ou_impar(numero):
    
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

for numero in numeros:
    if verificar_par_ou_impar(numero) == "par":
        pares += numero
    else:
        impares += numero

print(f"Soma de números pares: {pares}" )
print(f"Soma de números ímpares: {impares}")
