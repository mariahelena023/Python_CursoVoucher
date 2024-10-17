class Carro:
    motor_ligado = False
    carro_andando = False

    cor = "sem cor"
    marca = "sem marca"
    modelo = "sem modelo"
    ano = 0
    km_rodados = 0

    def LigarMotor():
        
        if not Carro.motor_ligado:
            Carro.motor_ligado = True
            print("")
            print("OS MOTORES ESTÃO LIGADOS")
            print("")
        else:
            print("")
            print("OS MOTORES DOS CARROS JÁ ESTÃO DESLIGADOS")
            print("")

    def DesligarMotor():
        if Carro.motor_ligado:
            if not Carro.carro_andando:
                Carro.motor_ligado = False
                print("")
                print("OS MOTORES DOS CARROS JÁ ESTÃO DESLIGADOS")
                print("")
            else:
                print("")
                print("NÃO É POSSÍVEL DESLIGAR O MOTORES ENQUANTO OS CARROS ESTÃO ANDANDO")
                print("")
        else:
            print("")
            print("OS MOTORES DOS CARROS JÁ ESTÃO DESLIGADOS")
            print("")

    def Andar():
        if Carro.motor_ligado:
            if not Carro.carro_andando:
                Carro.carro_andando = True
                print("")
                print("CARROS ANDANDO")
                print("")
            else:
                print("")
                print("OS CARROS JÁ ESTÃO ANDANDO")
                print("")
        else:
            print("")
            print("NÃO É POSSÍVEL ANDAR COM OS CARROS DESLIGADOS")
            print("")

    def Parar():
        if Carro.carro_andando:
            Carro.carro_andando = False
            print("")
            print("CARRO PARADO")
            print("")
        else:
            print("")
            print("O CARRO JÁ ESTÁ PARADO")
            print("")

    def StatusMotor():
        status = "LIGADOS" if Carro.motor_ligado else "DESLIGADOS"
        print("")
        print(f"OS MOTORES ESTÃO {status}")
        print("")

    def StatusCarro():
        status = "ANDANDO" if Carro.carro_andando else "PARADOS"
        print("")
        print(f"OS CARROS ESTÃO {status}")
        print("")
    
    def detalhes(self):
        print("")
        print(f"- Cor: {self.cor}")
        print(f"- Marca: {self.marca}")
        print(f"- Modelo: {self.modelo}")
        print(f"- Ano: {self.ano}")
        print(f"- KMs rodados: {self.km_rodados}")
        print("")

carro1 = Carro()
carro1.cor = "Amarelo"
carro1.marca = "Honda"
carro1.modelo = "HR-V"
carro1.ano = 2024
carro1.km_rodados = 0

carro2 = Carro()
carro2.cor = "Vermelho"
carro2.marca = "Nissan"
carro2.modelo = "GTR"
carro2.ano = 2024
carro2.km_rodados = 0

def Menu():
    while True:
        print(30 * "--")
        print("---MENU---")
        print("- Ligar motores (1)")
        print("- Desligar motores (2)")
        print("- Fazer os carros andarem (3)")
        print("- Parar os carros (4)")
        print("- Ver status dos motores (5)")
        print("- Ver status dos carros (6)")
        print("- Ver detalhes do carro1 (7)")
        print("- Ver detalhes do carro2 (8)")
        print("- Sair (0)")
        print("")

        op = int(input("Insira o número da sua opção: "))
        print(30 * "--")

        if op == 1:
            Carro.LigarMotor()
        elif op == 2:
            Carro.DesligarMotor()
        elif op == 3:
            Carro.Andar()
        elif op == 4:
            Carro.Parar()
        elif op == 5:
            Carro.StatusMotor()
        elif op == 6:
            Carro.StatusCarro()
        elif op == 7:
            carro1.detalhes()
        elif op == 8:
            carro2.detalhes()
        elif op == 0:
            print("")
            print("Saindo...")
            print("")
            break
        else:
            print("")
            print("Opção inválida. Tente novamente.")
            print("")

Menu()