class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo
    def depositar(self,cantidad):
        self.saldo+=cantidad
        
        def retirar(self,cantidad):
            if cantidad <=self.saldo:
                self.saldo-=cantidad
            else:
                print("saldo insuficiente")
    def mostrar_saldo(self):
        print(f"el saldo ce {self.titular}es{self.saldo}.")