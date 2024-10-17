produtos = ["CAMISETA","CALÇA","MEIA","MOLETOM"]
carrinho = []

while True:
    print(30 * "--")
    print("---MENU---")
    print("- Ver lista de produtos (1)")
    print("- Ver carrinho de compras (2)")
    print("- Adiconar produtos ao carrinho (3)")
    print("- Sair do menu (4)")
    print(30 * "--")
   
    menu = int(input("Insira a opção que deseja: "))
    print(" ")
   
    if menu == 1:
        print("Lista de Produtos:")
        for i in range(len(produtos)):
            print(f"{i + 1}. {produtos[i]}")
            print(" ")
           
    elif menu == 2:
        if carrinho:
            print("Carrinho de Compras:")
            for i in range(len(carrinho)):
                print(f"{i + 1}. {carrinho[i]}")
                print(" ")
        else:
            print("O carrinho está vazio.")
           
    elif menu == 3:
        print("Lista de Produtos:")
        for i in range(len(produtos)):
            print(f"{i + 1}. {produtos[i]}")
            print(" ")
       
        add_carrinho = int(input("Digite o número do produto que deseja adicionar ao carrinho: "))
        if 0 <= add_carrinho < len(produtos):
            carrinho.append(produtos[add_carrinho])
            print(f"{produtos[add_carrinho]} FOI ADICONADO AO CARRINHO.")
            print(" ")
        else:
            print("ESCOLHA INVÁLIDA.")
            print(" ")
           
    elif menu == 4:
        print("SAINDO DO MENU.")
        break
       
    else:
        print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
        print(" ")