class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def MostrarDetalhes(self):
        print(30 * "--")
        print(f"Nome do livro: {self.nome}")
        print(f"Autor do livro: {self.autor}")
        print(f"Editora do livro: {self.editora}")
        print(f"Número de páginas: {self.paginas}")
        print(30 * "--")

    def AlterarEditora(self):
        novaEditora = input("Insira o nome da nova editora: ")
        self.editora = novaEditora
        print("")
        print("Editora alterada com sucesso!")

livro = Livro("O vilarejo", "Raphael Montes", "Objetiva", 96)

livro.MostrarDetalhes()
livro.AlterarEditora()
livro.MostrarDetalhes()
