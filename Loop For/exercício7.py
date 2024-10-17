numeros = []

for i in range(5):
    n = int(input("Insira um número: "))
    numeros.append(n)

maior_numero = numeros[0]

for n in numeros:
    if n > maior_numero:
        maior_numero = n

print(f"O maior número inserido foi: {maior_numero}")
    