produto_1= float(input ('digite o valor:'))
produto_2= float(input("digite o valor:"))
produto_3= float(input ("digite o valor:"))

if produto_1 < produto_2 and produto_1 < produto_3:
    print("compre o produto 1")

if produto_2 <produto_3 and produto_2 < produto_1:
    print ("compre o produto 2")

if produto_3< produto_2 and produto_3 < produto_1:
    print ("compre o produto 3")