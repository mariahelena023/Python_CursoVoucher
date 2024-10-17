while True:
    usuario = input("Insira um nome de usuário: ")
    senha = input("insira uma senha: ")

    if senha == usuario:
        print("Senha inválida. Ela não pode ser igual ao nome de usuário.")

    else:
        print("Nome de usuário e senha válidos. Obrigado(a).")
        break