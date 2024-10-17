n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

if n1 > n2:
    n1, n2 = n2, n1

soma = 0

for num in range(n1 + 1, n2):
    print(num)
    soma += num

print(f"A soma dos números no intervalo é: {soma}")
