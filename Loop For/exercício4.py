populacaoA = 80000
taxa_crescimentoA = 3 
populacaoB = 200000
taxa_crescimentoB = 1.5  
anos_maximo = 100

historico_a = [populacaoA]
historico_b = [populacaoB]

for ano in range(1, anos_maximo + 1):

    nova_populacaoA = historico_a[-1] * (1 + taxa_crescimentoA / 100)
    nova_populacaoB = historico_b[-1] * (1 + taxa_crescimentoB / 100)
    

    historico_a.append(nova_populacaoA)
    historico_b.append(nova_populacaoB)
    
    if nova_populacaoA >= nova_populacaoB:
        print(f"Vão ser necessários {ano} anos para que a população A ultrapasse ou se iguale a população B.")
        break