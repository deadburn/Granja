from Empleado import empleado

class limpieza(empleado):
    def __init__(self, cedula, nombre, cargo, areaAsignada):
        super().__init__(cedula, nombre, cargo, areaAsignada)
        self.areaAsignada=areaAsignada


    def realizarLimpieza():
        pass        