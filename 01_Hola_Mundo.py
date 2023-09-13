'''Dado un numero n mostrar la tabla de multiplicar de n hasta el 10
'''
# def tabla_de_multiplicar(n):
#     for i in range(1,11,1):
#         print(f"{n} X {i} = {n*i}")


# #programa principal

# n=int(input("ingrese un nro entero"))
# tabla_de_multiplicar(n)


'''funcion suma que reciba 2 valores con parametro opcional
'''

# def suma(a=0,b=0):
#     return a+b

# #programa principal
# a=5
# b=5
# s=suma()
# print(s)

'''Dado un numero n mostrar la tabla de multiplicar de n hasta el input
'''
def tabla_de_multiplicar(n, hasta):
    for i in range(1,hasta + 1,1):
        print(f"{n} X {i} = {n*i}")


#programa principal

n=int(input("ingrese un nro entero"))
tabla_de_multiplicar(n,12)
