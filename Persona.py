# En el archivo Persona.py crear una clase Persona con atributo nombre. 
# Despues, instanciar un objeto de tipo Persona

class Persona:
    nombre = None

    def __init__(self, arg_nombre):
        set_Nombre(arg_nombre)

    def get_Nombre(self):
        return self.nombre

    def set_Nombre(self, arg_nombre):
        self.nombre = arg_nombre

p = Persona("Rrrrr")
print(p.nombre)