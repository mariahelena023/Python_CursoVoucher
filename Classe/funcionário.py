class ContaCorrente:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_por_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_por_hora = valor_por_hora

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_por_hora

    def incrementar_horas(self, horas_adicionais):
        self.horas_trabalhadas += horas_adicionais

funcionario = ContaCorrente("Maria", "Toledo", 1200, 50)

print(30 * "--")
print(f"Nome Completo: {funcionario.nome_completo()}")
print("")
print(f"Salário: {funcionario.calcular_salario()}")
print("")
print(f"Horas Trabalhadas:")
funcionario.incrementar_horas(10)
print(funcionario.horas_trabalhadas) 
print(30 * "--")