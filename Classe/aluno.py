class Aluno:
    def __init__(self, nome, RA, n1, n2, n3, n4, media, resultado):
        self.nome = nome
        self.RA = RA
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.media = media
        self.resultado = resultado

    def MostrarDetalhes(self):
        print(30 * "--")
        print(f"Nome: {self.nome}")
        print(f"RA: {self.RA}")
        print(f"Nota 1: {self.n1}")
        print(f"Nota 2: {self.n2}")
        print(f"Nota 3: {self.n3}")
        print(f"Nota 4: {self.n4}")
        print(f"Média: {self.media}")
        print(f"Resultado: {self.resultado}")
        print(30 * "--")

    def InformeNome(self):
        cad_nome = input("Insira seu nome: ")
        self.nome = cad_nome
        print("")
        
    def InformeRA(self):
        cad_RA = int(input("Insira aqui o número do seu RA: "))
        self.RA = cad_RA
        print("")

    def InformeNotas(self):
        cad_n1 = float(input("Informe sua primeira nota: "))
        cad_n2 = float(input("Informe sua segunda nota: "))
        cad_n3 = float(input("Informe sua terceria nota: "))
        cad_n4 = float(input("Informe sua quarta nota: "))

        self.n1 = cad_n1
        self.n2 = cad_n2
        self.n3 = cad_n3
        self.n4 = cad_n4

    def CalculoMedia(self):
        ma = (self.n1 + self.n2 + self.n3 + self.n4) / 4

        self.media = ma

    def Resultado(self):
        if self.media >= 7:
            self.resultado = "Aprovado"
        elif self.media == 5 and self.media <= 6.9:
            self.resultado = "Exame"
        elif self.media < 5:
            self.resultado = "Reprovado"

aluno = Aluno("sem nome", "sem RA", "sem nota","sem nota", "sem nota", "sem nota", "sem média", "sem resultado")

aluno.MostrarDetalhes()
aluno.InformeNome()
aluno.InformeRA()
aluno.InformeNotas()
aluno.CalculoMedia()
aluno.Resultado()
aluno.MostrarDetalhes()