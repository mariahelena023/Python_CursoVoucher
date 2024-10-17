class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def Play(self):
        print(30 * "--")
        print(f"Foi dado play no filme: {self.nome}")
        print(f"Duração: {self.duracao} Minutos")

class Acao(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def Explodir(self):
        print("")
        print(f"EXXPLOSÃO!")
        print(30 * "--")

class Drama(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def Chorar(self):
        print("")
        print(f"Hora de chorar!")
        print(30 * "--")

class Suspense(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def Suspense(self):
        print("")
        print(f"O que acontecerá?")
        print(30 * "--")

filme_acao = Acao("MIB", 98)
filme_acao.Play()
filme_acao.Explodir()

filme_drama = Drama("Crepúsculo", 122)
filme_drama.Play()
filme_drama.Chorar()

filme_suspense = Suspense("O Homem Invisível", 125)
filme_suspense.Play()
filme_suspense.Suspense()


