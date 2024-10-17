class Pessoa:
    nome = "sem nome"
    idade = 0
    endereco = "sem endereco"

    def MostrarNome(self):
        print(f"{self.nome}")
    
    def AlterarIdade(self):
        if self.idade == 0:
            print(f"{self.idade}")
        else:
            print(f"Sua idade foi alterada para {self.idade}")

    def ImprimirEndereco(self):
        print(f"{self.endereco}")

pessoa1 = Pessoa()
pessoa1.nome = "Maria"
pessoa1.idade = 16
pessoa1.endereco = "Rua da Divisão"

pessoa1.MostrarNome()
pessoa1.AlterarIdade()
pessoa1.ImprimirEndereco()