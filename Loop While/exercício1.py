while True:
    nota = float(input("Insira uma nota entre  0 e 10: "))
    
    if nota > 10 or nota < 0:
        print("Nota inválida. Tente novamente.")

    elif nota <= 10 and nota >= 0:
        print("Nota válida. Obrigado(a).")
        break
