from typing import DefaultDict

from Persona.Persona import Persona


class Directivo(Persona):
    """Clase Empleado Tipo Persona"""

    def __init__(self, nombre, edad, nombre_e):
        Persona.__init__(self, nombre, edad)
        #Nuevos atributos
        self.nombre_e 

    def mostrar(self):
        #Método que devuelve cadena de Empleado
        return self.nombre, self.edad, self.nombre_e