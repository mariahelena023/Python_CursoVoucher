from cliente import Cliente
from barbearia import Barbearia

def ExibirMenu():
    print(30 * "--")
    print("--- MENU DO CLIENTE ---")
    print()
    print("- Realizar Um Agendamento (1)")
    print("- Cancelar Um Agendamento (2)")
    print("- Vizualizar Lista De Agendamentos (3)")
    print("- Sair (0)")
    print()

barbearia = Barbearia()

while True:
    ExibirMenu()
    
    try:
        opcao = int(input("Insira aqui a opção escolhida: "))
        print(30 * "--")

        if opcao == 0:
            print()
            print("ATÉ A PRÓXIMA...")
            print()
            break

        elif opcao == 1:
            nome = input("Insira seu nome: ")

            try:
                data = input("Em qual data gostaria que fosse realizado o atendimento (DD/MM/AAAA)? ")
                hora = input("Em qual horário gostaria de ser atendida (00:00)? ")
            except ValueError:
                    print("FORMATO DE DATA OU HORA INVÁLIDOS. TENTE NOVAMENTE.")

            servico = input("Qual serviço quer que seja realizado? ")

            cliente = Cliente(nome, data, hora, servico)
            barbearia.AddAgendamentos(cliente)
            print()
            print("AGENDADO COM SUCESSO!")
        
        elif opcao == 2:
            barbearia.VisualizarAgendamentos()

            print()
            nome = input("Insira o nome do cliente que deseja cancelar o agendamentos: ")
            print()
            barbearia.Cancelar(nome)
        
        elif opcao == 3:
            barbearia.VisualizarAgendamentos()

    except ValueError:
        print()
        print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")



            

        
            

                



    

