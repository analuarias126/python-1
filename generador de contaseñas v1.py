import random

# variable la cual contiene todos los caracteres que puede contener mi contraseña
caracteres_posibles = "*#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# variable la cual contiene de cuantos caracteres es la contraseña que se generara (los elige el usuario)
long = int(input("cual es la longitud de su contraseña(inserte numeros)-> "))

# variable que contiene la contraseña que se va a imprimir posteriormente
contasena_generada = ("")

# bucle for que permite ir agragndo caracteres aleatorios segun la longitud de la contraseña a la variable contasena_generada
for i in range(long):
    letras = random.choice(caracteres_posibles)
    contasena_generada += letras

# inprime la contraseña
print("Contraseña generada:", contasena_generada)
    


