populacaoA = int(input("Insira o valor da população A: "))
taxa_crescimentoA = float(input("Insira a taxa de crescimento da população A: "))
populacaoB = int(input("Insira o valor da população B: "))
taxa_crescimentoB = float(input("Insira a taxa de crescimento da população B: "))
anos_maximo = 100

historico_a = [populacaoA]
historico_b = [populacaoB]

for ano in range(1, anos_maximo + 1):

    nova_populacaoA = historico_a[-1] * (1 + taxa_crescimentoA / 100)
    nova_populacaoB = historico_b[-1] * (1 + taxa_crescimentoB / 100)
    

    historico_a.append(nova_populacaoA)
    historico_b.append(nova_populacaoB)
    
    if nova_populacaoA >= nova_populacaoB:
        print(f"Serão necessários {ano} anos para que a população do país A ultrapasse ou iguale a população do país B.")
        break
