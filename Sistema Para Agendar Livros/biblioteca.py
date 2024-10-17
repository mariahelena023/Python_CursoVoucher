class Biblioteca:
    def __init__(self):
        self.livros = []

    def AdicionarLivro(self, livro):
        self.livros.append(livro)
    
    def BuscarLivro(self, titulo):
        for i in self.livros:
            if i.titulo == titulo:
                return i
    def ConsultarDetalhes(self, titulo):
        livro = self.BuscarLivro(titulo)

        if livro:
            return livro #se tiver algo dentro de "livro" ele será VERDADEIRO.
        else:
            print()
            print("LIVRO NÃO ENCONTRADO.")
    
    def EmprestarLivro(self, titulo):
        livro = self.BuscarLivro(titulo)

        if livro:
            if livro.emprestado == False:
                print()
                print("EMPRÉSTIMO REALIZADO!")
                livro.emprestado = True
            else:
                print()
                print("O LIVRO JÁ FOI EMPRESTADO.")

        else:
            print()
            print("LIVRO NÃO ENCONTRADO.")
        
    def ListarTodosOsLivros(self):
        print()
        print("--- LISTA DE LIVROS ---")
        if self.livros:
            for i in self.livros:
                print(i)
        else:
            print()
            print("A BIBLIOTECA NÃO POSSUÍ NENHUM LIVRO.")
        print()

    def DevolverLivro(self, titulo):
        livro = self.BuscarLivro(titulo)

        if livro:
            if livro.emprestado == True:
                print()
                print("O LIVRO FOI DEVOLVIDO A BIBLIOTECA!")
                livro.emprestado = False
            else:
                print()
                print("O LIVRO JÁ ESTÁ NA BIBLIOTECA.")
        


    

    

