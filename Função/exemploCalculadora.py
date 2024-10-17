def exibeMenu():
    print("")
    print("---CALCULADORA---\n")
    print("- Soma (1)")
    print("- Subtração (2)")
    print("- Divisão (3)")
    print("- Multiplicação (4)")
    print("- Sair (0)\n")
    
    opcao = int(input("Insira aqui o número da sua opção: "))
    print("")
    return opcao

def somar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado
def subtracao(numero1, numero2):
    resultado = numero1 - numero2
    return resultado
def divisao(numero1, numero2):
    resultado = numero1 / numero2
    return resultado
def multiplicacao(numero1, numero2):
    resultado = numero1 * numero2
    return resultado

i = 0
opcao = 0
num1 = 0
num2 = 0
resultado = 0

while opcao == 0:
    opcao = exibeMenu()

    if opcao <= 0:
        print("")
        print("Tchau, até mais...")
        break

    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))

    if opcao == 1:
        resultado = somar(num1, num2)
        print("")
        print(f"---RESULTADO---: {resultado}")
    
    elif opcao == 2:
        resultado = subtracao(num1, num2)
        print("")
        print(f"---RESULTADO---: {resultado}")
    
    elif opcao == 3:
        resultado = divisao(num1, num2)
        print("")
        print(f"---RESULTADO---: {resultado}")
    
    elif opcao == 4:
        resultado = multiplicacao(num1, num2)
        print("")
        print(f"---RESULTADO---: {resultado}")