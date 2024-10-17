data = input("Insira uma data em formato dd/mm/aaaa: ")

if data[2] == "/" and data[5] == "/":
    
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:])

    if(dia <= 0 or dia >= 32):
        print("Data inválida.")

    if(mes <= 0 or mes >= 13):
        print("Data inválida.")

    if(ano <= 0 or ano > 9999):
        print("Data inválida.")

else:
    print("Data inválida")
