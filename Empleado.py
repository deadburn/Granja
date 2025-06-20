from Animal import animal

class empleado():
    def __init__(self, cedula, nombre, cargo):
        self.cedula=cedula
        self.nombre=nombre
        self.cargo=cargo
        self._animales_alimentados=[]
        print("El Empleado fue creado.")
        
    def RealizarTarea(self):
        pass
    def RegistrarAsistencia(self):
        pass
    def Reportar_Incidencias(self):
        pass
    def imprimir_Empleado(self):
        print (self.cedula+" "+ self.nombre+" "+ self.cargo)
        
    def AlimentarAnimal(self, animal, tipo_alimento,cantidad):
        objAnimal=animal()
        objAnimal.alimentar()
        print(f"El Empleado {self.nombre} empieza tarea de alimentación...")
        