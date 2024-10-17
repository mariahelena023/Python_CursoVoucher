class Circulo: 
    def __init__(self, raio, area, circunferencia):
        self.raio = raio
        self.area = area
        self.circunferencia = circunferencia

    def MostrarDetalhes(self):
        print(30 * "--")
        print(f"Valor do raio: {self.raio}")
        print(f"Valor da área: {self.area}")
        print(f"Valor da circunferêcia: {self.circunferencia}")
        print(30 * "--")

    def CalculoRaio(self):
        d = float(input("Insira aqui o valor do seu diâmetro: "))

        self.raio = d / 2
    
    def CalculoArea(self):
        self.area = 3.14 * (float(self.raio) ** 2)

    def CalculoCircunferencia(self):
        self.circunferencia = (2 * 3.14) * float(self.raio)

caso1 = Circulo("", "", "")

caso1.CalculoRaio()
caso1.CalculoArea()
caso1.CalculoCircunferencia()
caso1.MostrarDetalhes()
        
