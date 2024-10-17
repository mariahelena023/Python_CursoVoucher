# CRIAR UM SISTEMA SIMPLES PARA AGENDAMENTO DE LIVROS:
# - Tem que ter uma classe livros e uma biblioteca
# ---------------------//----------------------------

from biblioteca import Biblioteca
from livros import Livros

def ExibirMenu():
    print(30 * "--")
    print("- Adicionar Livros (1)")
    print("- Consultar Detalhes do Livro (2)")
    print("- Emprestar Livro (3)")
    print("- Listar Todos os Livros da Biblioteca (4)")
    print("- Devolver Livro (5)")
    print("- Sair (0)")
    print()

biblioteca = Biblioteca()

while True:
    ExibirMenu()

    opcao = int(input("Digite a opção escolhida: "))
    print(30 * "--")

    if opcao == 0:
        print()
        print("ATÉ A PRÓXIMA...")
        print()
        break

    elif opcao == 1:
        titulo = input("Insira o título do livro que deseja adicionar: ")
        autor = input("Insira o nome do autor livro: ")
        livro = Livros(titulo, autor)
        biblioteca.AdicionarLivro(livro)
        print()
        print("LIVRO ADICIONADO COM SUCESSO!")

    elif opcao == 2:
        titulo = input("Insira o título do livro que deseja buscar: ")
        detalhes = biblioteca.ConsultarDetalhes(titulo)
        print()
        print(detalhes)
    
    elif opcao == 3:
        titulo = input("Insira aqui o título do livro que deseja pegar emprestado: ")
        biblioteca.EmprestarLivro(titulo)

    elif opcao == 4:
        biblioteca.ListarTodosOsLivros()

    elif opcao == 5:
        titulo = input("Insira aqui o título do livro que deseja devolver: ")
        biblioteca.DevolverLivro(titulo)

        