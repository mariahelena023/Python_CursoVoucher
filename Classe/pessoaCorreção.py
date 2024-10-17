class Pessoa:
    nome = ""
    idade = 0
    endereco = ""

    def MostrarDetalhes(self):
        print(30 * "--")
        print(f"{self.nome}")
        print(f"{self.idade}")
        print(f"{self.endereco}")
        print(30 * "--")

    def AlterarIdade(self):
        novaIdade = int(input("Insira sua nova idade: "))
        self.idade = novaIdade
        print("")
        print("Idade alterada com sucesso!")

pessoa1 = Pessoa()
pessoa1.nome = "Maria"
pessoa1.idade = 0
pessoa1.endereco = "Rua da Divisão"

pessoa1.MostrarDetalhes()
pessoa1.AlterarIdade()
pessoa1.MostrarDetalhes()