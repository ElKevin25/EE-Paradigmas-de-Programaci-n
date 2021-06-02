from Empleados import empleados

emp = empleados()


def main():
    op = 1

    while op < 5 :
        print("")
        print("-------------------------------------------------------------------------------------------------------------")
        print("Hola en este programa puede ingresar y consultar los datos de los empleados de la Empresa Patito S.A. de C.V.")
        print("*************************************************************************************************************")
        print("|                           Seleccione la opcion que desea llevar a cabo                                    |")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("|    1.- Ingrsar datos de un nuevo obreo                 2.- Ingresar los datos de un nuevo administrador   |")
        print("|    3.- Ingresar los datos de un intendente             4.- Mostrar todos los datos      5.- Salir         |")
        print("*************************************************************************************************************")
        print("")

        op = int(input("Inseterte el numero de la opcion deseada:"))

        while(True):
            if (op == 1):
                nombre = input("Ingrese el nombre del obrero:")
                salario = int(input("Ingrese el salario del obrero:"))
                asistencias = int(input("Ingrese las asistencias totales del mes del obrero (Se consideran 30 como un mes de trabajo):"))
                bono = 0
                if asistencias < 30:
                    while asistencias < 30:
                        salario - 100
                        salario = salario
                        asistencias + 1
                else:
                    bono + 1000
                    
                emp.obrero(nombre,salario,asistencias, bono)
            
            elif (op == 2):
                nombre = input("Ingrese el nombre del administrador:")
                salario = int(input("Ingrese el salario del administrador:"))
                asistencias = int(input("Ingrese el numero de asistencias del adinistrador:"))
                ventas = int(input("Ingrese el total de ventas realizadas en el mes:"))
                bono = 0
                if asistencias < 30:
                    while asistencias != 30:
                        salario - 100
                        salario = salario
                        asistencias + 1
                else:
                    bono + 1000
                    bono = salario
                if (ventas == 100000):
                    bono = bono + 5000
                emp.administrador(nombre,salario,asistencias,ventas, bono)
            elif (op == 3):
                nombre = input("Ingrese el nombre del administrador:")
                salario = int(input("Ingrese el salario del administrador:"))
                asistencias = int(input("Ingrese el numero de asistencias del adinistrador:"))
                turno = input("Ingrese el turno del intendente (Matutino, Vespertino, Nocturno):")
                bono = 0
                if (asistencias < 30):
                    while asistencias < 30:
                        salario - 100
                        salario = salario
                        asistencias + 1
                else:
                    bono + 1000
                    bono = bono
                emp.administrador(nombre,salario,asistencias,ventas)
            elif(op ==4):
                emp.administrador()
                emp.intendente()
                emp.obrero()
            else:
                print("Fin del programa")
                break
main()