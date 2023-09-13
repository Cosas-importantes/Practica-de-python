'''#crear la clase postulante y desde el programa principal la instaciamos con datos para probarla

class Postulante():
    def __init__(self, id, nombre, apellido, email, cv, area):
        self.id =id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.cv = cv
        self.area = area

    def __str__(self): #el metodo espacial __str__() va a ser ejecutado cuando haga un print()
        return f"Postulante Nro. {self.id}, {self.nombre} {self.apellido}, con email {self.email} y cv {self.cv}, se postulo para {self.area}."
    

#programa principal

postulante1=Postulante(45237377, "Luciano", "Pagani", "lpagani2003@gmail.com", "cvlink", "area tanto") #llamando al constructor de la clase postulante
print(postulante1)
'''
class rectangulo():
    #base y altura
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def __str__(self):
        return f"El rectangulo tiene base {self.base} y altura {self.altura}"
    
    def perimetro(self):
        return 2*(self.base + self.altura)
        
    
    def area(self):
        return (self.base * self.altura)
        
    
    def dibujar(self):
        print("*"*self.base)
        for i in range(0, self.altura-2,1):
            print("*"+" "*(self.base-2)+"*")
        print("*"*self.base)

#programa principal
b=int(input("ingrese un nro base"))
h=int(input("ingrese un nro altura"))
rectangulo1=rectangulo(b,h)
print(rectangulo1)
rectangulo1.dibujar()
print(f"el area del rectangulo es {rectangulo1.area()}")
print(f"el perimetro del rectangulo es {rectangulo1.perimetro()}")