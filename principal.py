
from Granja import granja 


print ("1. Registrar Animal")
tipo=input("Digite el tipo de Animal: ")
edad=input("Digite la edad del Animal: ")
sexo=input("Digite el sexo del Animal: ")

objGranja=granja()
objGranja.RegistrarAnimal(tipo,edad,sexo)