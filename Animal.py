class animal():
    def __init__(self,tipo, edad, sexo):
        self._tipo=tipo
        self._edad=edad
        self._sexo=sexo
        print("Animal Creado")
        
    def almentar(self):
        print(f"El/la {self._tipo } esta siendo alimentado" )
    def vacunar(self):
        print(f"{self._tipo} Ha sido vacunado")
    def RegistrarPeso(self):
        print(f"{self._tipo} con edad {self._edad} de sexo {self._sexo} se le ha registrado el peso")
    def imprimirDato(self):
        print(self._tipo+" "+ self._edad+" "+ self._sexo)
    