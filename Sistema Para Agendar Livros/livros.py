class Livros:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def __str__(self):
        status = "Disponível"
        if self.emprestado == True:
            status = "Emprestado"
        return f"TÍTULO: {self.titulo} /AUTOR: {self.autor} - {status}"
    
    
    

