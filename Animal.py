class animal():
    def __init__(self,tipo, edad, sexo):
        self._tipo=tipo
        self._edad=edad
        self._sexo=sexo
        self._peso=0
        self._alimentado= False
        print("Animal Creado")
        
    def alimentar(self):
        print(f"El/la {self._tipo } esta siendo alimentado" )
        self._alimentado=True
        return True
    
    def vacunar(self):
        print(f"{self._tipo} Ha sido vacunado")
        
    def RegistrarPeso(self):
        print(f"{self._tipo} con edad {self._edad} de sexo {self._sexo} se le ha registrado el peso")
        
    def imprimirDato(self):
        print(self._tipo+" "+ self._edad+" "+ self._sexo)
    
    #Getters
    def get_tipo(self):
        return self._tipo
    
    def get_edad(self):
        return self._edad
    
    def get_sexo(self):
        return self._sexo
    
    def esta_alimentado(self):
        return self._alimentado
    