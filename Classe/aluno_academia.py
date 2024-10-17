class Aluno_Academia:
    def __init__(self, nome, peso, altura, idade, mensalidade):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.idade = idade
        self.mensalidade = mensalidade
    
    def CalcularIMC(self):
        IMC = self.peso / (self.altura * self.altura)
        print(30 * "--")
        print(f"{self.nome} tem o IMC de: {IMC}")

    def Mensalidade(self):
        if self.idade < 18:
            desconto = self.mensalidade * 0.5
            print(f"O valor de sua mensalidade será: {desconto}")
            print(30 * "--")
        else:
            print(f"O valor de sua mensalidade ser: {self.mensalidade}")
            print(30 * "--")
        
aluno1 = Aluno_Academia("Mario", 70, 1.80, 20, 120)
aluno2 = Aluno_Academia("Ana", 50, 1.60, 16, 120)
    
aluno1.CalcularIMC()
aluno1.Mensalidade()
aluno2.CalcularIMC()
aluno2.Mensalidade()