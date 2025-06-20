class alimento():
    def __init__(self, tipo, cantidad,fechaCaducidad):
         self._tipo=tipo
         self._cantidad=cantidad
         self._fechaCaducidad=fechaCaducidad
         
         
#Getters
    def get_tipo(self):
        return self._tipo
    def get_cantidad(self):
        return self._cantidad
    def get_fechaCaducidad(self):
        return self._fechaCaducidad
         
         
#Metodos    
    def RegistrarAlimento():
         tipo_alimento= input("Seleccione el tipo de alimento")
         cantidad_alimento= input(float("Digite la cantidad de alimento en Gramos"))
         vencimiento=input(str("Digite la fecha de vencimiento: "))
         
         
    
    