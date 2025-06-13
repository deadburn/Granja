from Granja import granja 
#Zona De Funciones

##Funcion Para Mostrar Menu
def MostrarMenu():
        print("\nBienvenido, seleccione un opción: ")
        print ("1. Registrar Animal")
        print ("2. Registrar Empleado")
        print ("3. Mostrar Animales")
        print ("4. Mostrar Empleados")
        num=(input("Ingrese Su opción: "))
        return num
    
##Funcion Para Registrar animal
def auxRegistrarAnimal():
    tipo=input("Digite el tipo de Animal: ")
    edad=input("Digite la edad del Animal: ")
    sexo=input("Digite el sexo del Animal: ")
    objGranja=granja()
    objGranja.RegistrarAnimal(tipo,edad,sexo)
     

#Codigo principal de Python
while True:
    aux_Num=MostrarMenu()
    if aux_Num=='1':
       auxRegistrarAnimal()
    else:
        break


    
        
    
        
    
    
