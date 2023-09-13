#errores y excepciones
'''
try:
    n=int(input("ingrese un numero:"))
    m=4
    print(f"{n}/{m} = {n/m}")
except:
    print("Ha ocurrido un error.")
    print("ingrese un NUMERO")   
'''
#en bucle hasta que se solucione
'''
while True:
    try:
        n=float(input("ingrese un numero: "))
        m=4
        print(f"{n}/{m} = {n/m}")
        break
    except:
        print("Ha ocurrido un error.")
        print("ingrese un NUMERO")   
'''
#en bucle hasta que se solucione y con mensaje de exito
'''
while True:
    try:
        n=float(input("ingrese un numero: "))
        m=4
        print(f"{n}/{m} = {n/m}")
    except:
        print("Ha ocurrido un error.")
        print("ingrese un NUMERO")  
    else:
        print("Todo funciono correctamente")
        break
'''
#en bucle hasta que se solucione, en caso de exito ejecuta algo y da mensaje final en caso de error o exito
'''
while True:
    try:
        n=float(input("ingrese un numero: "))
        m=4
        print(f"{n}/{m} = {n/m}")
    except:
        print("Ha ocurrido un error.")
        print("ingrese un NUMERO")  
    else:
        print(f"El numero ingresado es {n}")
        break
    finally:
        print("--finalizo el intento--")
'''
#capturo el tipo de error
'''
while True:
    try:
        n=float(input("ingrese un numero1: "))
        m=float(input("ingrese un numero2: "))
        print(f"{n}/{m} = {n/m}")
    except Exception as e:
        print("Ha ocurrido un error.")
        print(type(e).__name__)
        print("ingrese un NUMERO")  
    else:
        print(f"El numero ingresado es {n}")
        break
    finally:
        print("--finalizo el intento--")
'''
#dependiendo del tipo de error muestro un mensaje u otro
while True:
    try:
        n=float(input("ingrese un numero1: "))
        m=float(input("ingrese un numero2: "))
        print(f"{n}/{m} = {n/m}")
    except TypeError:
        print("Ha ocurrido un error.")
        print("No se puede dividir el numero entre una cadena")
        print("ingrese un NUMERO")  
    except ValueError:
        print("Ha ocurrido un error.")
        print("Debes introducir una cadena que sea un numero")
        print("ingrese un NUMERO")  
    except ZeroDivisionError:
        print("Ha ocurrido un error.")
        print("no se puede dividir por cero, aunque tiende a infinito")
        print("ingrese un NUMERO")  
    except Exception as e:
        print("Ha ocurrido un error.")
        print(type(e).__name__)
        print("ingrese un NUMERO")  
    else:
        print(f"El numero ingresado es {n}")
        break
    finally:
        print("--finalizo el intento--")