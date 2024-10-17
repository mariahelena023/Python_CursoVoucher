a = [5,9,10,-1,14,23,6,30]

soma = 0
for i in a:
    if i % 2 == 0:
        soma += i

print(f"A soma dos números pares da lista é: {soma}")
