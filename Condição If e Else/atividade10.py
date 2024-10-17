print(" ")
print("FORMAS DE PAGAMENTPO: ")
print("- No pix você ganha 10% de desconto (1)")
print("- No crédito você ganha 5% de desconto (2)")
print("- Em duas vezes é o preço normal da etiqueta (3)")
print("- Em três vezes é o preço normal da etiqueta mais 10% de juros (4)")
print(" ")

valor = float(input("Insira o valor do seu produto: "))
pagamento = int(input("Insira a forma de pagamento: "))

if pagamento == 1:
    print("O valor final a se pagar pelo produto será: ", valor * 0.1)
if pagamento == 2:
    print("O valor final a se pagar pelo produto será: ", valor * 0.05)
if pagamento == 3:
    print("O valor final a se pagar pelo produto será duas parcelas de: ", valor / 2)
if pagamento == 4:
    print("O valor final a se pagar pelo produto será três parcelas de: ", valor * 1.10 / 3)