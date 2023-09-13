'''
Clase cuenta bancaria constructor, metodos de deposito, estraccion, mostrar saldo y tranferencia
'''

class cuenta_bancaria():
    #saldo, nro de cuenta, titular
    def __init__(self, nro_de_cuenta, titular):
        self.nro_de_cuenta=nro_de_cuenta
        self.titular=titular
        self.saldo=0
    
    def __str__(self):
        return f"La cuenta nro: {self.nro_de_cuenta} a nombre de {self.titular} con saldo ${self.saldo}"
    
    def depositar(self, importe):
        self.saldo = self.saldo + importe

    def extraccion(self, importe):
        self.saldo = self.saldo - importe

    def transferencia(self,importe, cuenta_destino):
        self.saldo = self.saldo - importe
        cuenta_destino.depositar(importe)

#programa principal
nro_de_cuenta= int(input("ingrese un nro de cuenta"))
titular= str(input("ingrese su nombre"))
cuenta_bancaria1=cuenta_bancaria(nro_de_cuenta, titular)
print(cuenta_bancaria1)
importe_dep= int(input("ingrese numero a depositar"))
cuenta_bancaria1.depositar(importe_dep)
print(cuenta_bancaria1)
importe_ext= int(input("ingrese numero a extraer"))
cuenta_bancaria1.extraccion(importe_ext)
print(cuenta_bancaria1)

cuenta_bancaria2=cuenta_bancaria(2, "cosme fulanito")
cuenta_bancaria2.depositar(2000)
print(cuenta_bancaria2)

importe_trans= int(input("ingrese numero a transferir"))
cuenta_bancaria1.transferencia(importe_trans, cuenta_bancaria2)
print(cuenta_bancaria1)
print(cuenta_bancaria2)
