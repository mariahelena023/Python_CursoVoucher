class Conta:
    def __init__(self, nome, CPF, numero, saldo):
        self.nome = nome
        self.CPF = CPF
        self.numero = numero
        self.saldo = saldo
    
    def MostrarDetalhes(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.CPF}")
        print(f"Número da conta: {self.numero}")
        print(f"Saldo: {self.saldo}")

    def Saque(self):
    
        sacar = float(input("Insira aqui a quantia que deseja sacar: "))
        
        if sacar > self.saldo:
            print("")
            print("Não foi possível sacar o valor desejado. Não a saldo o suficiente.")

        else:
            self.saldo -= sacar
            print("")
            print("Saque realizado com sucesso!")

    def Deposito(self):
        depositar = float(input("Insira aqui o valor que deseja depositar: "))

        self.saldo += depositar
        print("")
        print("Depósito feito com sucesso!")

    def DepositoOuSaque(self):
        while True:
            print(30 * "--")
            print("---CONTA---")
            print("- Depositar (1)")
            print("- Sacar (2)")
            print("- Detalhes da conta (3)")
            print("- Sair (0)")
            print("")

            op = int(input("Insira aqui o número da operação que deseja realizar: "))
            print(30 * "--")
         
            if op == 1: 
                self.Deposito()
            elif op == 2:
                self.Saque()
            elif op == 3:
                self.MostrarDetalhes()
            elif op == 0:
                print("")
                print("Saindo da conta...")
                print("")
                break
            

pessoa = Conta("Maria", 12345678911, 20242323, 10)


pessoa.DepositoOuSaque()



        