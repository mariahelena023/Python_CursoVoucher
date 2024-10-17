chave = 0

def exibicaoMenu():
    print(30 * "--")
    print("---MENU---")
    print("")
    print("- Adicionar tarefas (1)")
    print("- Lista de tarefas (2)")
    print("- Marcar tarefa como concluída (3)")
    print("- Remover tarefas (4)")
    print("- sair (0)")

def addTerefa(tarefas):
    descricao = input("Insira aqui a tarefa que deseja realizar: ")
    t = {"Descrição": descricao,"Status": "Não concluída"}
    tarefas.append(t)
    print("")
    print("TAREFA ADICIONADA.")

def listaDeTarefas(tarefas):
    if not tarefas:
        print("")
        print("NÃO HÁ NENHUMA TAREFA EM SUA LISTA.")
        print("")
        return
    
    print("")
    print("---LISTA DE TAREFAS---")
    
    for i,t in enumerate(tarefas, 1):
        status = t["Status"]
        descricao = t["Descrição"]
        print("")
        print(f"{i}. {descricao} - {status}")

def concluidas(tarefas):
    listaDeTarefas(tarefas)
    if not tarefas:
        return
    
    print("")
    n = int(input("Insira o número da tarefa que você quer que seja marcada como concluída: "))
    
    if 1 <= n <= len(tarefas):
        tarefas[n - 1]["Status"] = "Concluída"
        print("")
        print("TAREFA MARCADA COMO CONCLUÍDA.")
    
    else:
        print("")
        print("OPÇÃO NÃO VÁLIDA.")

def removerTarefa(tarefas):
    listaDeTarefas(tarefas)
    
    if not tarefas:
        return
    
    print("")
    numero = int(input("Digite o número da tarefa a ser removida: "))
    
    if 1 <= numero <= len(tarefas):
        tarefas.pop(numero - 1)
        print("")
        print("TAREFA REMOVIDA DA LISTA DE TAREFAS.")
    
    else:
        print("")
        print("OPÇÃO NÃO VÁLIDA.")

def escolhaDeOpções():
    tarefas = []
    
    while True:
        exibicaoMenu()
        print("")
        opcao = int(input("Escolha uma opção: "))
        print(30 * "--")

        if opcao == 1:
            addTerefa(tarefas)
        
        elif opcao == 2:
            listaDeTarefas(tarefas)
        
        elif opcao == 3:
            concluidas(tarefas)
        
        elif opcao == 4:
            removerTarefa(tarefas)
        
        elif opcao == 0:
            print("")
            print("Saindo do sistema...")
            break
        
        else:
            print("")
            print("OPÇÃO NÃO VÁLIDA. TENTE NOVAMENTE.")

if chave == 0:
    escolhaDeOpções()