class Cliente:
    def __init__(self, nome, data, hora, servico):
        self.nome = nome
        self.data = data
        self.hora = hora
        self.servico = servico
        self.agendamento = "AGENDADO"

    def __str__(self):
        return f"- Nome do Cliente: {self.nome}\n- Data Agendada: {self.data}\n- Hora Agendada: {self.hora}\n- Servico Escolhido: {self.servico}\n- Status: {self.agendamento}"
    