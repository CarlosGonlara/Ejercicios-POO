#Clase
class CuentaBancaria:
    
    #Constructor
    def __init__(self, titular,nCuenta, saldo):
        self.titular = titular
        self.saldo = saldo
        self.nCuenta = nCuenta

    #Metodo Depositar
    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
    
    #Metodo Retirar
    def retirar(self, retiro):
        if retiro > self.saldo:
            print("Fondos Insuficientes")
            return 0
        self.saldo = self.saldo - retiro
    
    #Metodo Consultar Saldo
    def consultarSaldo(self):
        return f"El saldo actual es de {self.saldo} pesos"
    
    #Metodo mostrar informacion
    def mostrarInformacion(self):
        return f"{self.titular} Tu saldo es {self.saldo}"
    

#Objetos    
cuenta1 = CuentaBancaria("Carlos Gonzalez", "0001", 1000.00)
cuenta2 = CuentaBancaria("Samanta Alcantara", "0002", 500.00)
cuenta3 = CuentaBancaria("Jolliete Alcantara", "0003", 200.00)

cuenta1.retirar (500.00)
   
print(cuenta1.mostrarInformacion())
print(cuenta1.consultarSaldo())

cuenta2.retirar (500.00)
   
print(cuenta2.mostrarInformacion())
print(cuenta2.consultarSaldo())

cuenta3.retirar (500.00)
   
print(cuenta3.mostrarInformacion())
print(cuenta3.consultarSaldo())

cuenta1.depositar (500.00)
   
print(cuenta1.mostrarInformacion())
print(cuenta1.consultarSaldo())