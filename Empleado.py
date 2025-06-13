class empleado():
    def __init__(self, cedula, nombre, cargo):
        self.cedula=cedula
        self.nombre=nombre
        self.cargo=cargo
        print("El objeto Empleado fue creado.")
        
    def RealizarTarea(self):
        pass
    def RegistrarAsistencia(self):
        pass
    def Reportar_Incidencias(self):
        pass
    def imprimir_Empleado(self):
        print (self.cedula+" "+ self.nombre+" "+ self.cargo)
        