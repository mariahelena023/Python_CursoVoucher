lampada = False

def ligarLampada():
    return True
def desligarLampada():
    return False

def consultarLampada():
    if lampada:
        print("Lâmpada Ligada")

    else:
        print("Lâmpada Desligada")

while True:
    print(30 * "--")
    print("---MENU---")
    print("- Ligar lâmpada (1)")
    print("- Desligar lâmpada (2)")
    print("- Consultar lâmpada (3)")
    print("")

    op = int(input("Funcionalidade: "))
    print(30 * "--")
    
    if op == 1:
        lampada = ligarLampada()
    elif op == 2:
        lampada = desligarLampada()
    elif op == 3:
        consultarLampada()