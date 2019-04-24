# En el archivo Persona.py crear una clase Persona con atributo nombre. 
# Despues, instanciar un objeto de tipo Persona 
# Agregarle un atributo edad y un metodo cumple_anhos 
# y un metodo get_edad. 
# Inicializar un objeto de tipo Persona y hacerle cumplir anhos

class Persona:
    nombre = None
    edad = None

    def __init__(self, arg_nombre, arg_edad):
        self.set_Nombre(arg_nombre)
        self.set_Edad(arg_edad)

    def get_Nombre(self):
        return self.nombre
    def set_Nombre(self, arg_nombre):
        self.nombre = arg_nombre

    def get_Edad(self):
        return self.edad
    def set_Edad(self, arg_edad):
        self.edad = arg_edad

    def cumple_anhos(self):
        self.set_Edad(self.get_Edad() + 1)

from time import sleep

p = Persona("Ror", 10)
print("Te llamas", p.nombre, "y tenes", p.edad, "anhos")
for i in range(5):
    print("Ahora quiero que cumplas un anho mas!!!")
    p.cumple_anhos()
    print("Edad:", p.edad)
    sleep(2)

