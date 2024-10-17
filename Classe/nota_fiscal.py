class Nota_Fiscal:
    def __init__(self, numero, tipo, serie, CNPJ, razao_social, data, valor_produtos, ICMS, frete, IPI):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.CNPJ = CNPJ
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.ICMS = ICMS
        self.frete = frete
        self.IPI = IPI
        self.valor_total = self.calcularValorTotal()

    def obterNumero(self):
        return self.numero

    def obterDataEmissao(self):
        return self.data

    def alterarRazaoSocial(self, nova_razao_social):
        self.razao_social = nova_razao_social

    def calcularValorTotal(self):
        return self.valor_produtos + self.ICMS + self.frete + self.IPI

    def exibirNotaFiscal(self):
        print(30 * "--")
        print(f"- Número: {self.numero}")
        print(f"- Tipo: {self.tipo}")
        print(f"- Série: {self.serie}")
        print(f"- CNPJ: {self.CNPJ}")
        print(f"- Razão Social: {self.razao_social}")
        print(f"- Data: {self.data}")
        print(f"- Valor dos Produtsos: {self.valor_produtos}")
        print(f"- ICMS: {self.ICMS}")
        print(f"- Frete: {self.frete}")
        print(f"- IPI: {self.IPI}")
        print(f"- Valor Total: {self.valor_total}")
        print(30 * "--")

nota = Nota_Fiscal(1503, "Entrada", 1, "12.345.678/0001-91", "T3ddy Atacadista", "23/07/2024" , 1000.0, 200.0, 50.0, 100.0,)

nota.exibirNotaFiscal()


