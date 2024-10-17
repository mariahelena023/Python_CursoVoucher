class Carro:
    def __init__(self, modelo, marca, cor, ano, valor, nivel, consumo, IPVA, distancia):
        self.modelo = modelo 
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel
        self.consumo = consumo
        self.IPVA = IPVA
        self.distancia = distancia

    def Abastecer(self):
        return self.nivel

    def Andar(self):
        return self.distancia

    def VerificarNivel(self):
        self.consumo = self.distancia / self.nivel
        return self.consumo
    
    def CalcularIPVA(self):
        self.IPVA = self.valor * 0.025
        return self.IPVA
    
    def MostrarDetalhes(self):
        print(30 * "--")
        print(f"- Modelo: {self.modelo}")
        print(f"- Marca: {self.marca}")
        print(f"- Cor: {self.cor}")
        print(f"- Ano: {self.ano}")
        print(f"- Valor: {self.valor}")
        print(f"- Nível: {self.nivel} litros")
        print(f"- Distância: {self.distancia} km")
        print(f"- Consumo: {self.consumo}")
        print(f"- IPVA: {self.IPVA}")
        print(30 * "--")
    
carro1 = Carro("Fusca", "Volkswagen", "Azul", 2005, 25000, 10, 200, 2000, 200)
carro2 = Carro("Gol", "Volkswagen", "Branco", 2004, 12193, 20, 400, 4000, 400)

carro1.Abastecer()
carro1.Andar()
carro1.VerificarNivel()
carro1.CalcularIPVA()
carro1.MostrarDetalhes()

carro2.Abastecer()
carro2.Andar()
carro2.VerificarNivel()
carro2.CalcularIPVA()
carro2.MostrarDetalhes()

