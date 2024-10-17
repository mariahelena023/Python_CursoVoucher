class Pessoa:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, nota1, nota2, nota3, nota4):
        super().__init__(matricula, nome, idade)
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

    def Estudar(self):
        print("")
        print(f"A aluna {self.nome} está estudando no momento.")

class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, carga_horaria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario

    def Lecionar(self):
        print(30 * "--")
        print(f"A professora {self.nome} está lecionando a disciplina {self.disciplina}.")
        print(30 * "--")

aluno = Aluno(1890, "Anna Laurah", 16, 6.0, 5.0, 5.0, 7.5)
print(30 * "--")
print(f"Média da aluna {aluno.nome}: {aluno.calcular_media()}")
aluno.Estudar()

professor = Professor(1500, "Mariana", 35, "História", "História", 20, 2500.0)
professor.Lecionar()


    