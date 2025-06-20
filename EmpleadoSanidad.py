from Empleado import empleado

class Sanidad(empleado):
    def __init__(self, cedula, nombre, cargo, especialidad):
        super().__init__(cedula, nombre, cargo, especialidad)
        self.especialidad=especialidad
        
        
    def aplicarVacuna():
        pass
    
    def RealizarChequo():
        pass