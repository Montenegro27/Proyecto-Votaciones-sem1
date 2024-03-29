# Universidad del Valle de Guatemala
# CountMaster by. VoteCount Solutions - Proyecto Final
# Mauricio Montenegro - 23679
# Daniel Leal - 23614
# Gabriel Soto - 23900
# Carlos Coc - 23859
# El proposito del programa es el poder realizar un conteo de votos correctos para las elecciones, existen dos opciones en el programa.
# Poder Votar, contar votos
from Funciones_e2023 import *
seguir_programa = True
while seguir_programa == True: #Creamos un ciclo para que siga ejecutando el programa y no truene :3
    # Creamos un menu :3
    print("CountMaster by. VoteCount Solutions")
    print("Elecciones 2023 Guatemala")
    # Solicitamos que desea realizar
    categoria = input("""Seleccione lo que desea realizar
        1. Usuario votante
        2. Usuario Administrador
        3. Salir
        """)
    if categoria.isdigit() == True:
        # Convertimos el valor de cateogoria a un tipo entero para poder ingresar solo valores enteros
        categoria_entero = int(categoria)
        # Validamos que el numero este en el rango 
        if categoria_entero >= 1 and categoria_entero <=3:
            # Validamos la accion
            if categoria_entero == 1:
                votante()
            elif categoria_entero == 2:
                #La contraseña para esta seccion es: contraseña123
                administrador()
            else:
                # Salimos del programa
                print("Gracias por usar nuestro programa")
                seguir_programa = False
        else:
            print("ERROR: Opcion no valida, Ingresar opcion entre 1-3")
    else:
        print("ERROR: Ingresar opcion entre 1-3")