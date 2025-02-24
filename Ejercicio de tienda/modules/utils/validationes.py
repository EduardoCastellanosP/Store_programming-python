import os
def sololetras(msg):
    while True:
        x=input(msg)

        if x.isalpha():
            return x
        else:
            print("No se pueden ingresar numeros")
            os.system('pause')
            continue
#validationdigit
def solonumeros(msg:str)-> int:

    try:
        x=int(input(msg))
    except ValueError:
        print("Opcion invalida, solo numeros")
        return solonumeros(msg)
    else:
        return x
    


def numerosyletras (msg):
    while True:
        x=input(msg)
        if x.isalnum():
            return x
        else:
            print('Error al Ingresar los datos')
            os.system('pause')
            continue
            