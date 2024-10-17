print(" ")
print("--- LANCHONETE BURGÃO ---")
print(" ")
print(" CARDÁPIO: ")
print(" ")
print("LANCHES:")
print("- Cachorro Quente R$11,10 (100)")
print("- Ovo Simples R$8,30 (101)")
print("- Bauru com Ovo R$11,50 (102)")
print("- Hambúrguer R$16,20 (103)")
print(" ")
print("BEBIDAS:")
print("- Refrigerante R$6,00 (201)")
print("- Suco R$7,50 (202)")
print("- Água Mineral R$4,70 (203)")
print(" ")
print(" ")

pedido_lanche = int(input("Insira aquio número do seu lanche: "))
quant_lanche = int(input("Insira aqui quantia que você quer do seu lanche: "))
print(" ")
pedido_bebida = int(input("Insira aqui o número da sua bebida: "))
quant_bebida = int(input("Insira aqui quantia que você quer de bebida: "))

cachorro_quente = int(100)
ovo_simples = int(101)
bauru_com_ovo = int(102)
hamburguer = int(103)
refrigerante = int(201)
suco = int(202)
agua_mineral = int(203)

print(" ")
if pedido_lanche == 100:
    valor_lanche = 11.10
elif pedido_lanche == 101:
    valor_lanche = 8.30
elif pedido_lanche == 102:
    valor_lanche = 11.50
elif pedido_lanche == 103:
    valor_lanche = 16.20
else:
    print("Número de lanche não encontrado.")

if pedido_bebida == 201:
    valor_bebida = 6.00
elif pedido_bebida == 202:
    valor_bebida = 7.50
elif pedido_bebida == 203:
    valor_bebida = 4.70
else:
    print("Número de bebida não encontrado.")

pedido_final = (valor_lanche * quant_lanche) + (valor_bebida * quant_bebida)
print(" ")
print("O valor final do seu pedido ficou em: ", pedido_final)