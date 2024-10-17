a = [5,9,10,-1,14,23,6,30]

soma = 0
contadora = 0

while contadora < len(a):
    if a[contadora] % 2 == 0:
        soma += a[contadora]
    contadora += 1

print(f"A soma dos números pares dessa lista resulta em: {soma}")

