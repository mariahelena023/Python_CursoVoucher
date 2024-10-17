salario_inicial  = 1000

# representa o ano 1996
salario_atual = salario_inicial + (salario_inicial * 0.015)

ano = 1997

percentual_aumento = 0.015 * 2

while ano <= 2024:
    #print(f"{salario_atual} = {salario_atual} + ({salario_atual} * {percentual_aumento})")
    salario_atual = salario_atual + (salario_atual * percentual_aumento)
    percentual_aumento = percentual_aumento * 2
    ano = ano + 1
    print(f"{ano} = {salario_atual}")

#print(f"O salário atual do funcionário em 292024 é R$ {salario_atual: .2f}")