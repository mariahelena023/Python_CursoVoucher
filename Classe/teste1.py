class Cadastro:
    nome = "sem nome"
    senha = "sem senha"
    email = "sem e-mail"

    def MostrarDetalhes(self):
        print(30 * "--")
        print(f"Nome de usuário: {self.nome}")
        print(f"Senha: {self.senha}")
        print(f"E-mail: {self.email}")
        print(30 * "--")

    def AlterarNome(self):
        novo_nome = input("Insira aqui o nome que deseja cadastrar: ")
        self.nome = novo_nome
        print("")
        print("Nome cadastrado com sucesso!")
        print(30 * "--")

    def AlterarSenha(self):
        nova_senha = input("Insira aqui a senha que deseja cadastrar: ")
        self.senha = nova_senha
        print("")
        print("Senha cadastrada com sucesso!")
        print(30 * "--")

    def AlterarEmail(self):
        novo_email = input("Insira aqui o e-mail que você deseja cadastrar: ")
        self.email = novo_email
        print("")
        print("E-mail cadastrado com sucesso!")

cadastro1 = Cadastro()
cadastro1.MostrarDetalhes()
cadastro1.AlterarNome()
cadastro1.AlterarSenha()
cadastro1.AlterarEmail()
cadastro1.MostrarDetalhes()