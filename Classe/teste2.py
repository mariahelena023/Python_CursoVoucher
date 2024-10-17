class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

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
        print("IDADE ALTERADA COM SUCESSO!")

pessoa1 = Pessoa("Maria", 0, "Rua da Divisão")


pessoa1.MostrarDetalhes()
pessoa1.AlterarIdade()
pessoa1.MostrarDetalhes()