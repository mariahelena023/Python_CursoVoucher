lista_funcionarios = []
maior = 0 

for i in range(4):
    
    dados_funcionario = {}

    dados_funcionario["nome"] = input("Insira o nome: ")
    dados_funcionario["funcao"] = input("Insira a função: ")
    dados_funcionario["salario"] = float(input("Insira o valor do salário: "))
    print("")

    lista_funcionarios.append(dados_funcionario)

    if dados_funcionario["salario"] > maior:
        maior = dados_funcionario["salario"]
    
for i in lista_funcionarios:

    if i["salario"] == maior:
        print("")
        print(f"o funcincionário coom maior salário é: {i["nome"]}")



    