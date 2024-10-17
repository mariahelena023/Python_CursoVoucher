x = int(input("Insira um número: "))
contador = 0

while True:
    x = x - 1
    contador += 1
    
    if x == 0:
        break
    
    print(x)
print(f"Contador: {contador}")


