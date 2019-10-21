#Hacer que el sistenam genere un numero aleatorio entre 1 y 10
#Hacer que el usuario adivine el numero
#Que la aplicacion termine cuando el usuario termine el numero
import random
s = random.randint(1,10)
while True:
    n = int(input("Adivina el numero del sistema:"))
    if n == s:
        print("Adivinaste!")
        break
    else:   
        print("Numero incorrecto!")