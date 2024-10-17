class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
        
    
    def CalculePerimetro(self):
        print(30 * "--")
        self.ladoA = float(input("Insira aqui o valor do ladoA do triângulo: "))
        self.ladoB = float(input("Insira aqui o valor do ladoB do triângulo: "))
        self.ladoC = float(input("Insira aqui o valor do ladoC do triângulo: "))
        print(30 * "--")

        perimetro = self.ladoA + self.ladoB + self.ladoC

        print(f"O perimetro do seu triângulo é: {perimetro}")
        print("")

    def MaiorLado(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            print("O maior lado é o lado A.")
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            print("O maior lado é o lado B.")
        else:
            print("O maior lado é o lado C.")

triangulo1 = Triangulo("","","")

triangulo1.CalculePerimetro()
triangulo1.MaiorLado()


    