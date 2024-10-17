class Carro:
    cor = "sem cor"
    marca = "sem marca"
    modelo = "sem modelo"
    ano = 2010
    km_rodados = 0

    def detalhes(self):
        print(f"{self.cor}")
        print(f"{self.marca}")
        print(f"{self.modelo}")
        print(f"{self.ano}")
        print(f"{self.km_rodados}")

    def adiciona_km_rodados(self, km):
        self.km_rodados = self.km_rodados + km


carro1 = Carro()
carro1.cor = "amarelo"
carro1.marca = "honda"
carro1.modelo = "hr-v"
carro1.ano = 2024
carro1.adiciona_km_rodados(10)
carro1.detalhes()

carro2 = Carro()
carro1.cor = "vermelho"
carro1.marca = "nissan"
carro1.modelo = "gtr"
carro1.ano = 2024
carro1.adiciona_km_rodados(50)
carro1.detalhes()