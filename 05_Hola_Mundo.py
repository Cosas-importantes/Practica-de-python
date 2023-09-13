'''class pasante:
    entrevistados=[]
    tomados=[]
    idp=[1]

    def __init__(self, nombre,apellido,cv,email,area):
        self.id=self.idp[0]
        self.idp[0]= self.idp[0]+1
        self.nombre=nombre
        self.apellido=apellido
        self.cv=cv
        self.email=email
        self.area=area
    
    def imprimir(self):
        print(f"Id: {self.id}")
        print(f"Nombre: {self.nombre}") 
        print(f"Apellido: {self.apellido}")
        print(f"Link de CV: {self.cv}")
        print(f"Email: {self.email}")
        print(f"Area: {self.area}")
        self.estado()
        self.instancia()
        
      
    
    def entrevistar(self):
        pasante.entrevistados.append(self.id)

    def contratado(self):
        pasante.tomados.append(self.id)

    def estado(self):
        if self.id in pasante.entrevistados:
            print("ya fue entrevistado")
        else:
            print("aun no fue entrevistado")
      

    def instancia(self):
        cad=""
        if self.id in pasante.tomados:
            cad="contratado"
        else:
            if self.id in pasante.entrevistados:
                cad="no fue contratado"
            else:
                cad="espera a ser evaluado, aun no fue contratado"
        print(cad)
        print("-"*20)
    



    #programa princial

p1=pasante("Luciano", "Pagani", "link cualquiera", "lpagani2003@gmail.com", "area de I+D")
p2=pasante("Demian", "Sotelo", "link cualquiera", "demso2004@gmail.com", "area de ventas")
p3=pasante("Ivan", "Rieiro", "link cualquiera", "irieiro139@gmail.com", "area de marketing")
p4=pasante("Facundo", "Reinero", "link cualquiera", "freinero1911@gmail.com", "area de I+D")
p1.entrevistar()
p2.entrevistar()
p1.contratado()
p1.imprimir()
p2.imprimir()
p3.imprimir()
p4.imprimir()
'''

#mismo programa pero con encapsulamiento de datos
        
'''
class pasante:
    entrevistados=[]
    tomados=[]
    idp=[1]

    def __init__(self, nombre, apellido, cv, email, area):
        self.id=self.idp[0]
        self.idp[0]= self.idp[0]+1
        self.nombre=nombre
        self.apellido=apellido
        self.__cv=cv
        self.__email=email          #con la barra baja protegi a los atributos para que no los puedan acceder desde afuera del programa
        self.__area=area
    
    def imprimir(self):
        print(f"Id: {self.id}")
        print(f"Nombre: {self.nombre}") 
        print(f"Apellido: {self.apellido}")
        self.estado()
        self.instancia()
        
      
    
    def entrevistar(self):
        pasante.entrevistados.append(self.id)

    def contratado(self):
        pasante.tomados.append(self.id)

    def estado(self):
        if self.id in pasante.entrevistados:
            print("ya fue entrevistado")
        else:
            print("aun no fue entrevistado")
      

    def instancia(self):
        cad=""
        if self.id in pasante.tomados:
            cad="contratado"
        else:
            if self.id in pasante.entrevistados:
                cad="no fue contratado"
            else:
                cad="espera a ser evaluado, aun no fue contratado"
        print(cad)
        print("-"*20)
    
    def get_informacion_sencible(self):
        print(f"Id: {self.id}")
        print(f"Nombre: {self.nombre}") 
        print(f"Apellido: {self.apellido}")
        print(f"Link de CV: {self.__cv}")
        print(f"Email: {self.__email}")
        print(f"Area: {self.__area}")
        self.estado()
        self.instancia()


    #programa princial

p1=pasante("Luciano", "Pagani", "link cualquiera", "lpagani2003@gmail.com", "area de I+D")
p2=pasante("Demian", "Sotelo", "link cualquiera", "demso2004@gmail.com", "area de ventas")
p3=pasante("Ivan", "Rieiro", "link cualquiera", "irieiro139@gmail.com", "area de marketing")
p4=pasante("Facundo", "Reinero", "link cualquiera", "freinero1911@gmail.com", "area de I+D")
p1.entrevistar()
p2.entrevistar()
p1.contratado()
# p1.imprimir()
# p2.imprimir() # este comando por mas que quiera acceder a la variable no me deja
# p3.imprimir()
# p4.imprimir()

# print(p1.__email) # este comando por mas que quiera acceder a la variable no me deja
p1.__area="principal" #tampoco deja modificar variables, solo se puede hacer por metodos
p1.get_informacion_sencible()
'''