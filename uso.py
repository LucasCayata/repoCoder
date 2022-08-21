from funciones_matematicas import sumar, restar, multiplicar #si uso * me trae todas las funciones
from clases import Persona

variable1=int(input("Ingrese un numero: "))
variable2=int(input("Ingrese otro numero: "))

print(sumar(variable1,variable2))
print(restar(variable1,variable2))

variable=Persona("Juan","Mansilla",41)

variable.saludar()
