'''
sistema banco con clase cliente
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


class Banco():

    def __init__(self,nombre_banco):
        self.nombre_banco=nombre_banco
        self.clientes=[]


    def __str__(self):
        cad=f"Banco: {self.nombre_banco}   \n"
        for e in self.clientes:
            cad+= f"{e.__str__()} \n"
        return cad

    def add_cliente(self,cliente):
        self.clientes.append(cliente)

    def saldo_total(self):
        saldo_b=0
        for e in self.clientes:
            saldo_b+= e.saldo
        return f"Banco: {self.nombre_banco} \n tiene saldo: ${saldo_b}"

        


# programa principal

bna=Banco("BNA")
cuenta_corriente1=cuenta_bancaria(1,"Luciano Pagani")
cuenta_corriente1.depositar(1000)
print(cuenta_corriente1)
cuenta_corriente2=cuenta_bancaria(2,"Cosme Fulanito")
cuenta_corriente2.depositar(1000)
print(cuenta_corriente2)

bna.add_cliente(cuenta_corriente1)
bna.add_cliente(cuenta_corriente2)
print(bna)
print(bna.saldo_total())