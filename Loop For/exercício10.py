n1 = int(input("Insira o primeiro número inteiro: "))
n2 = int(input("Insira o segundo número inteiro: "))

if n1 > n2:
    n1, n2 = n2, n1

for num in range(n1 + 1, n2):
    print(num)