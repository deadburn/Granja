from Empleado import empleado

class administrador(empleado):
    def __init__(self, cedula, nombre, cargo):
        super().__init__(cedula, nombre, cargo)



    def supervisarCorrales():
        pass
    
    def RegistrarAsistencia(self):
        return super().RegistrarAsistencia()
    
    def generarReportes():
        pass