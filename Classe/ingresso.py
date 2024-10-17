class Ingresso:
    def __init__(self, preco, setor):
        self.preco = preco
        self.setor = setor

    def AlterarPreco(self, novo_preco):
        self.preco = novo_preco

    def MostrarSetor(self):
        return self.setor

class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote, open_bar, open_food, estacionamento):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def PegarBebida(self):
        if self.open_bar:
            print("Pegando uma bebida no Open Bar.")
        else:
            print("Esse ingresso não dá acesso ao Open Bar.")

    def AcessarCamarote(self):
        if self.camarote:
            print("Acessando o camarote.")
        else:
            print("Esse ingresso não dá acesso ao camarote.")

ingresso = Ingresso(100.0, "Setor A")
print(f"Setor do ingresso: {ingresso.MostrarSetor()}")
ingresso.AlterarPreco(120.0)

ingresso_vip = IngressoVIP(200.0, "Setor VIP", True, True, False, True)
print(ingresso_vip.PegarBebida())
print(ingresso_vip.AcessarCamarote())
