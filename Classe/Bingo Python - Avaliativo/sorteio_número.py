import random

class Sorteio:
    def __init__(self):
        self.numeros_sorteados = []

    def SorteandoNumeros(self):
        if len(self.numeros_sorteados) == 75:
            print("")
            print("TODOS OS NÚMEROS JÁ FORAM SORTEADOS.")
            print("")
            print(30 * "--")
            return None
        while True:
            numero = random.randrange(1, 76)
            if numero not in self.numeros_sorteados:
                self.numeros_sorteados.append(numero)
                return numero

    def NumerosSorteados(self):
        print("Números sorteados:", self.numeros_sorteados)
        print(30 * "--")

    def FazerSorteio(self):
            while len(self.numeros_sorteados) < 75:
                print(30 * "--")
                input("Pressione Enter para sortear um número...")
                print("")
                numero = self.SorteandoNumeros()
                if numero:
                    print(f"Número sorteado: {numero}") 
                    self.NumerosSorteados()

s = Sorteio()
s.FazerSorteio()
s.SorteandoNumeros()
s.NumerosSorteados()