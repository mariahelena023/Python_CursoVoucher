class Carro:
    cor = "sem cor"
    marca = "sem marca"
    modelo = "sem modelo"
    ano = 2010
    km_rodados = 0
    statusMotor = 0
    statusMovimento = 0
    

    def detalhes(self):
        print(f"{self.cor}")
        print(f"{self.marca}")
        print(f"{self.modelo}")
        print(f"{self.ano}")
        print(f"{self.km_rodados}")

    def LigarMotor(self):
        if self.statusMotor == 1:
            print("Motor já está ligado")
        else:
            self.statusMotor = 1
            print("Motor ligado")

    def DesligarMotor(self):
        self.statusMotor = 0
        print("Motor desligado")

    def Andar(self):
        self.statusMovimento = 1
        print("Em movimento")
    
    def Parar(self):
        self.statusMovimento = 0
        print("Parado")

    
    def AdicionarKm(self,km):
        self.km_rodados += km


carro1 = Carro()
carro1.cor = "AMARELO"
carro1.marca = "Honda"
carro1.modelo = "HR-V"
carro1.ano = 2024
carro1.AdicionarKm(10)
carro1.detalhes()
carro1.LigarMotor()
carro1.LigarMotor()
carro1.DesligarMotor()