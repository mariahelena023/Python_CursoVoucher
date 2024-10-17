while True:
    total = 0
    contador = 0
    
    while True:
        produto = float(input("Digite o valor do produto:"))
        contador += 1
        total =  total + produto

        if produto == 0:
            print("Total:" , total)
        dinheiro = float(input("Dinheiro:"))
        print("Dinheiro:" , dinheiro)
        print("troco:" , (dinheiro - total))
        break

    print (f'Produto {contador}: R${produto}')
