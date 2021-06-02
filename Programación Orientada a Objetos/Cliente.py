from typing import DefaultDict

from Persona.Persona import Persona


class Cliente(Persona):
    """Clase Empleado Tipo Persona"""

    def __init__(self, nombre, edad, nombre_empresa, telefono_de_contacto):
        Persona.__init__(self, nombre, edad)
        #Atributos nuevos
        self.nombre_empresa 
        #Atributos nuevos
        self.telefono_de_contacto 

    def mostrar(self):
        #Devuelve cadena de Empleado
        return self.nombre, self.edad, self.nombre_empresa, self.telefono_de_contacto
        
