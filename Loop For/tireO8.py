lista = []

for i in range(5):
    lista.append(int(input("Insira im número inteiro: ")))

nova_lista = []
for i in lista:
    if i != 8:
        nova_lista.append(i)

print(nova_lista)