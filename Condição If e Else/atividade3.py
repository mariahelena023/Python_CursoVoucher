salario_atual = float(input("Digite seu salário atual: "))

if salario_atual < 500:
        novo_salario = salario_atual * 0.15
elif salario_atual <= 1000:
        novo_salario = salario_atual * 0.10
else:
        novo_salario = salario_atual * 0.05
print("Seu salário reajustado é equivalente a: ", novo_salario)

