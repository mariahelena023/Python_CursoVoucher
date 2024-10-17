consultas = []
historico = {}

while True:
    print(30 * "--")
    print("Escolha seu tipo de usuário: ")
    print("")
    print("- Médico (1)")
    print("- Paciente (2)")
    print("- Sair do hospital (0)")
    print("")

    usuario = int(input("Insira aqui o número da sua opção: "))
    print(30 * "--")

    if usuario == 0:
        print("")
        print("Saindo do hospital...")
        break
    
    elif usuario == 2:
        
        while True:
            print("")
            print("- Marcar uma consulta (1)")
            print("- Verificar histórico de consulta (2)")
            print("- Voltar para área de usuários (0)")
            print("")

            opc_usuario = int(input("Insira aqui sua opção: "))
            print(30 * "--")

            if opc_usuario == 0:
                print("")
                print("VOltando para área de usuários...")
                print("")
                break


            elif opc_usuario == 1:

                while True:
                    nome_paciente = input("Insira seu nome: ")
                    cpf_paciente = input("Insira seu CPF: ")
                    idade_paciente = int(input("Insira sua idade: "))
                    horario_consulta_paciente = input("Insira o horário da consulta: ")
                    print("")

                    consulta_agendada = {"Nome do paciente": nome_paciente, "CPF do paciente": cpf_paciente, "Idade do paciente": idade_paciente, "Horário da consulta": horario_consulta_paciente}
                    consultas.append(consulta_agendada)

                    print("Consulta marcada! Obrigado pela preferência.")
                    print(30 * "--")
                    print("")
                    break

            elif opc_usuario == 2:

                cpf_historico = input("Digite o CPF para ver o histórico: ")
                
                print("")
                print("---HISTÓRICO DE CONSULTAS---")
                print("")
                
                for consulta in consultas:
                    if consulta["CPF do paciente"] == cpf_historico:
                        print(f"Nome do paciente: {consulta["Nome do paciente"]}, CPF do paciente: {consulta["CPF do paciente"]}, Horário da consulta: {consulta["Horário da consulta"]}")
                        print(30 * "--")
            else:
                print("")
                print("Opção inválida. Por favor tente novamene.")
                print("")
                print(30 * "--")
                continue
    
    elif usuario == 1:
        
        while True:
            print("")
            print("- Consultar lista de pacientes (1)")
            print("- Realizar consulta (2)")
            print("- Voltar para área de usuários (0)")
            print("")
            
            opc_medico = int(input("Insira aqui a opção: "))
            print(30 * "--")

            if opc_medico == 1:
                print("---LISTA DE PACIENTES COM CONSULTA MARCADA---")
                print("")
                
                for consulta in consultas:
                    print(f"Nome do paciente: {consulta["Nome do paciente"]}, CPF do paciente: {consulta["CPF do paciente"]}, Horário da consulta: {consulta["Horário da consulta"]}")
                    print(30 * "--")
            
            elif opc_medico == 2:
                cpf_consulta = input("Insira o CPF do paciente que será atendido: ")
                print("")
                
                for consulta in consultas:
                    if consulta["CPF do paciente"] == cpf_consulta:
                        consultas.remove(consulta)
                        print("Consulta realizada e paciente liberado!")
                        print(30 * "--")
                        break
            
            elif opc_medico == 0:
                print("")
                print("VOltando para área de usuários...")
                print("")
                break

            else:
                print("")
                print("Opção inválida. Por favor tente novamene.")
                print("")
                print(30 * "--")
                continue

    else:
        print("")
        print("Opção inválida. Por favor tente novamene.")
        print("")
        print(30 * "--")
        continue