from Animal import animal
from Empleado import empleado
class granja():
    
    def __init__(self, nombre):
        self._nombre=nombre
        
    
    def __init__(self):
        pass
    
    def limpiar():
        pass
    def AsignarAnimal():
        pass
    def RegistrarAnimal(self, tipo, edad, sexo):
        objAnimal=animal(tipo, edad, sexo)
        objAnimal.imprimirDato()
    def RegistrarPeso(self, tipo, edad, sexo):
        objAnimal=animal(tipo, edad, sexo)
        objAnimal.RegistrarPeso()
    
    