class Barbearia:
    def __init__(self):
        self.agendamentos = []

    def BuscarCliente(self, nome):
        for i in self.agendamentos:
            if i.nome == nome:
                return i
    
    def AddAgendamentos(self, cliente):
        self.agendamentos.append(cliente)

    def Cancelar(self, nome):
        cliente = self.BuscarCliente(nome)

        if cliente:
            if cliente.agendamento == "AGENDADO":
                cliente.agendamento= "CANCELADO"
                print("AGENDAMENTO CANCELADO!")
            else:
                print("O AGENDAMENTO JÁ FOI CANCELADO.")
        else:
            print("NENHUM AGENDAMENTO ENCONTRADO.")



    def VisualizarAgendamentos(self):
            print("---  LISTA DE AGENDAMENTOS  ---")
            print()

            if self.agendamentos:
                 for i in self.agendamentos:
                      print(i)
            else:
                print()
                print("NÃO HÁ NENHUM SERVIÇO MARCADO.")
            print()
    