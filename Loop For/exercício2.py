while True:

    usuario = input("Insira um nome de usuário: ")
    senha = input("Insira uma senha: ")

    if usuario == senha:
        print("Erro no cadatro. Nome de usuário não pode ser igual a senha e vice-versa. Tente novamente.")
        continue
    else:
        print("Cadastro concluído. Obrigado.")
        break

