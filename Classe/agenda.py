class Agenda:
    def __init__(self, data, anotacoes):
        self.data = data
        self.anotacoes = anotacoes

    def MostrarDetalhes(self):
        print(30 * "--")
        print(f"Data: {self.data}")
        print("")
        print(f"Anotações: {self.anotacoes}")
        print(30 * "--")

    def ValidarData(self):
        d = input("Insira uma data em formato dd/mm/aaaa: ")

        if d[2] == "/" and d[5] == "/":
    
            dia = int(d[0:2])
            mes = int(d[3:5])
            ano = int(d[6:])

            if(dia <= 0 or dia >= 32):
                print("Data inválida.")

            if(mes <= 0 or mes >= 13):
                print("Data inválida.")

            if(ano <= 0 or ano > 9999):
                print("Data inválida.")

            elif not d[2] == "/" and not d[5] == "/":
                print("Data inválida")
        
            else:
                self.data = d
        
    def AnotarTarefas(self):
        print("")
        a = input("Insira aqui sua anotação: ")

        self.anotacoes = a

anotacao1 = Agenda("vazio", "vazio")

anotacao1.MostrarDetalhes()
anotacao1.ValidarData()
anotacao1.AnotarTarefas()
anotacao1.MostrarDetalhes()

    