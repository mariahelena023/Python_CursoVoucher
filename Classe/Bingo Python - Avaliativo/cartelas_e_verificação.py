import random

class Cartela:
    def __init__(self):
        intervalos = [
            (1, 15),
            (16, 30), 
            (31, 45), 
            (46, 60), 
            (61, 75)
        ]
        self.cartela = [[self.GerarNumero(inicio, fim) for _ in range(5)] for inicio, fim in intervalos]
        self.cartela[2][2] = 0
        self.marcados = [[False] * 5 for _ in range(5)]
        self.marcados[2][2] = True

    def GerarNumero(self, inicio, fim):
        numeros = []
        while len(numeros) < 5:
            num = random.randrange(inicio, fim + 1)
            if num not in numeros:
                numeros.append(num)
        return numeros.pop()

    def VerificarBingo(self):
        for linha in self.marcados:
            if all(linha):
                return True

        for col in range(5):
            if all(self.marcados[linha][col] for linha in range(5)):
                return True

        if all(self.marcados[i][i] for i in range(5)) or all(self.marcados[i][4-i] for i in range(5)):
            return True

        return False

    def ExibirCartelaMarcada(self):
        print(30 * "--")
        cabecalho = [' B', ' I', ' N', ' G', ' O']
        print(" ".join(cabecalho))
        for linha in range(5):
            for col in range(5):
                if self.cartela[col][linha] == 0 or self.marcados[col][linha]:
                    print(" xx", end=" ")
                else:
                    print(f"{self.cartela[col][linha]:2}", end=" ")
            print()

cartela_bingo = Cartela()
cartela_bingo.ExibirCartelaMarcada()

while True:
    print(30 * "--")
    numero = int(input("Digite o número sorteado: "))
    for col in range(5):
        for linha in range(5):
            if cartela_bingo.cartela[col][linha] == numero:
                cartela_bingo.marcados[col][linha] = True
   
    cartela_bingo.ExibirCartelaMarcada()
   
    if cartela_bingo.VerificarBingo():
        print("")
        print("BINGO!")
        break
