#PrincipalCalc.py
from Calculadora import calcu

c = calcu()

def menu():
    print (" ***      CALCULADORA PYTHON       *** ")
    print (" ")
    print ("   Por favor seleccione una opcion:")
    print ("   1 - Sumar")
    print ("   2 - Restar")
    print ("   3 - Multiplicar")
    print ("   4 - Dividir")
    print ("   0 - Salir")
    return int(input("Introduce la opcion: "))

while(True):
    opcion = menu()

    if(opcion == 0):
        break
    else:
        num1 = int(input("Introdusca el primer numero: "))
        num2 = int(input("Introdusca el segiindo numero: "))
        
        if (opcion == 1):
            c.suma (num1, num2)

        elif (opcion==2):
            c.resta (num1, num2)
        
        elif (opcion==3):
            c.multi(num1, num2)
        
        elif (opcion==4):
            c.div(num1, num2)
        
        else:
            print ("Opcion incorrecta...")

print ("Fin del programa calculadora...")