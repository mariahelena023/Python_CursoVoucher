contador = 0

while True:
    nome = input("Insira aqui um nome: ")
    
    if nome == "rafael" or nome == "RAFAEL" or nome == "Rafael":
        break
    
    contador = contador + 1
    print(f"Tentativas: {contador}")

print("Nome válido. Obrigado")