class ContaBancaria:

     def __init__(self,numero):
        self.saldo = 0
        self.numero = numero

     def getSaldo(Self):
        return Self.saldo
     
     def verSaldo(self):
         print(f"Saldo Atual: {self.getSaldo()}")

     def existeSaldo(self,valor):
         return valor <= self.getSaldo()
     
     def transferir (self,valor):
         destino = input("Informe a conta destino:")
         if(len(destino) !=5):
             print("Formato de conta inválido")
             return
         if (destino == self.numero):
            print("Conta não pode ser a mesma")
            return
         
         if (not (self.existeSaldo(valor))):
             print("Saldo Insuficiente")
             return
         
         self.saldo -= valor
         print("Transferencia efetuada com sucesso")

         
       
class ContaCorrente(ContaBancaria):
    def sacar(self,valor):
        total = valor + (valor * 0.05 )
        if(self.existeSaldo(total)):
            self.saldo += valor
            print("Saque efetuado com sucesso")
            return
        print("Saldo insuficiente")

    def depositar(self,valor):
        self.saldo += valor
        print("Depósito efetuado com sucesso")
    


class ContaSalario(ContaBancaria):
    def sacar(self,valor):
       if(self.existeSaldo(valor)):
         self.saldo += valor
         print("Saque efetuado com sucesso")
         return
       
       print("Saldo insuficiente")
    


class ContaPoupanca(ContaBancaria):
    def sacar(self,valor):
       if(self.existeSaldo(valor)):
         self.saldo += valor
         print("Saque efetuado com sucesso")
         return
       
       print("Saldo insuficiente")

    def depositar(self,valor):
        self.saldo += valor
        print("Depósito efetuado com sucesso")
