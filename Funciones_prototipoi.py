#Universidad del Valle de Guatemala 
#Funciones Prototipo inicial
# Mauricio Montenegro - 23679
# Daniel Leal - 23614
# Gabriel Soto - 23900
# Carlos Coc - 23859

import csv
import time
import pandas as pd

def votar_presidente():
    # Abrir el archivo CSV en modo de escritura
    with open('candidatos.csv', mode='r') as file:
        # Crear un objeto reader del archivo CSV
        reader = csv.reader(file)
        # Leer los datos del archivo CSV en una lista
        data = list(reader)
        # Imprimir los candidatos a presidente
        print('Candidatos a presidente:')
        print('1. UNE - Sandra Torres y Juan Arevalo')
        time.sleep(1)
        print('2. FCN - Maria Gomez y Ricardo Quiñones')
        time.sleep(1)
        print('3. VALOR - Zury Rios y Pedro Rodriguez')
        time.sleep(1)
        print('4. VAMOS - Luisa Hernandez y Carlos Peñanieto')
        time.sleep(1)
        print('5. SEMILLA - Jose Ramirez y Jose Arevalo')
        time.sleep(1)
        print('6. PAN - Juan Pardo y Maria Quintana')
        time.sleep(1)
        # Pedir al usuario que seleccione un candidato
        opcion = input('Seleccione un candidato para votar (1-6): ')
        try:
            # Convertir la opción del usuario en un entero
            opcion = int(opcion)
            
            # Verificar si la opción es válida
            if opcion < 1 or opcion > 6:
                print('Error: opción inválida.')
                return
            # Obtener el índice del candidato seleccionado en la lista de datos
            if opcion == 1:
                indice = 1
            elif opcion == 2:
                indice = 2
            elif opcion == 3:
                indice = 3
            elif opcion == 4:
                indice = 4
            elif opcion == 5:
                indice = 5
            else:
                indice = 6
            # Obtener el partido y los votos del candidato seleccionado
            partido = data[indice][1]
            votos = int(data[indice][3])
            # Incrementar el número de votos del candidato seleccionado
            votos += 1
            # Actualizar los votos en la lista de datos
            data[indice][3] = str(votos)
            # Abrir el archivo CSV en modo de escritura
            with open('candidatos.csv', mode='w', newline='') as file:
                # Crear un objeto writer del archivo CSV
                writer = csv.writer(file)
                # Escribir los datos actualizados en el archivo CSV
                writer.writerows(data)
            print('Voto registrado exitosamente para', partido)
        except ValueError:
            print('Error: opción inválida.')

def votar_alcalde():
    # Abrir el archivo CSV en modo de escritura
    with open('candidatos.csv', mode='r') as file:
        # Crear un objeto reader del archivo CSV
        reader = csv.reader(file)
        # Leer los datos del archivo CSV en una lista
        data = list(reader)
        # Imprimir los candidatos a alcalde
        print('Candidatos a alcalde:')
        print('1. UNE - Carlos Sanchez')
        time.sleep(1)
        print('2. FCN - Ana Ramirez')
        time.sleep(1)
        print('3. VALOR - Miguel Hernandez')
        time.sleep(1)
        print('4. VAMOS - Luisa Rodriguez')
        time.sleep(1)
        print('5. SEMILLA - Rosa Perez')
        time.sleep(1)
        print('6. PAN - Juan Montenegro')
        time.sleep(1)
        # Pedir al usuario que seleccione un candidato
        opcion = input('Seleccione un candidato para votar (1-6): ')
        try:
            # Convertir la opción del usuario en un entero
            opcion = int(opcion)
            
            # Verificar si la opción es válida
            if opcion < 1 or opcion > 6:
                print('Error: opción inválida.')
                return
            # Obtener el índice del candidato seleccionado en la lista de datos
            if opcion == 1:
                indice = 8
            elif opcion == 2:
                indice = 9
            elif opcion == 3:
                indice = 10
            elif opcion == 4:
                indice = 11
            elif opcion == 5:
                indice = 12
            else:
                indice = 13
            # Obtener el partido y los votos del candidato seleccionado
            partido = data[indice][1]
            votos = int(data[indice][3])
            # Incrementar el número de votos del candidato seleccionado
            votos += 1
            # Actualizar los votos en la lista de datos
            data[indice][3] = str(votos)
            # Abrir el archivo CSV en modo de escritura
            with open('candidatos.csv', mode='w', newline='') as file:
                # Crear un objeto writer del archivo CSV
                writer = csv.writer(file)
                # Escribir los datos actualizados en el archivo CSV
                writer.writerows(data)
            print('Voto registrado exitosamente para', partido)
        except ValueError:
            print('Error: opción inválida.')

def votar_diputado():
    # Abrir el archivo CSV en modo de escritura
    with open('candidatos.csv', mode='r') as file:
        # Crear un objeto reader del archivo CSV
        reader = csv.reader(file)
        # Leer los datos del archivo CSV en una lista
        data = list(reader)
        # Imprimir los candidatos a alcalde
        print('Candidatos a alcalde:')
        print('1. UNE - Mario Estrada')
        time.sleep(1)
        print('2. FCN - Ana Garcia')
        time.sleep(1)
        print('3. VALOR - Raul Flores')
        time.sleep(1)
        print('4. VAMOS - Sofia Martinez')
        time.sleep(1)
        print('5. SEMILLA - Oscar Perez')
        time.sleep(1)
        print('6. PAN - Luis Coc')
        time.sleep(1)
        # Pedir al usuario que seleccione un candidato
        opcion = input('Seleccione un candidato para votar (1-6): ')
        try:
            # Convertir la opción del usuario en un entero
            opcion = int(opcion)
            
            # Verificar si la opción es válida
            if opcion < 1 or opcion > 6:
                print('Error: opción inválida.')
                return
            # Obtener el índice del candidato seleccionado en la lista de datos
            if opcion == 1:
                indice = 14
            elif opcion == 2:
                indice = 15
            elif opcion == 3:
                indice = 16
            elif opcion == 4:
                indice = 17
            elif opcion == 5:
                indice = 18
            else:
                indice = 19
            # Obtener el partido y los votos del candidato seleccionado
            partido = data[indice][1]
            votos = int(data[indice][3])
            # Incrementar el número de votos del candidato seleccionado
            votos += 1
            # Actualizar los votos en la lista de datos
            data[indice][3] = str(votos)
            # Abrir el archivo CSV en modo de escritura
            with open('candidatos.csv', mode='w', newline='') as file:
                # Crear un objeto writer del archivo CSV
                writer = csv.writer(file)
                # Escribir los datos actualizados en el archivo CSV
                writer.writerows(data)
            print('Voto registrado exitosamente para', partido)
        except ValueError:
            print('Error: opción inválida.')

def votante():
    # Variables booleanas para verificar si el usuario ya votó en cada elección
    voto_presidente = False
    voto_alcalde = False
    voto_diputado = False
    print("Bienvenido al programa de votación.")
    time.sleep(1)
    print("Este programa te permitirá votar por los candidatos a presidente, alcalde y diputado.")
    time.sleep(1)
    print("Para votar, simplemente ingresa el número correspondiente al candidato que deseas elegir.")
    time.sleep(1)
    print("A continuación, se te mostrará una lista de los candidatos para cada cargo y su partido político.")
    time.sleep(1)
    print("¡Comencemos!")
    time.sleep(1)
    
    while True:
        print("Selecciona una opción:")
        print("1. Votar por presidente y vicepresidente")
        print("2. Votar por alcalde")
        print("3. Votar por diputado")
        print("4. Salir")
        
        opcion = input("Ingresa el número de la opción que deseas: ")
        
        if opcion == "1":
            if voto_presidente:
                print("Ya has votado por presidente y vicepresidente.")
            else:
                votar_presidente()
                voto_presidente = True
        elif opcion == "2":
            if voto_alcalde:
                print("Ya has votado por alcalde.")
            else:
                votar_alcalde()
                voto_alcalde = True
        elif opcion == "3":
            if voto_diputado:
                print("Ya has votado por diputado.")
            else:
                votar_diputado()
                voto_diputado = True
        elif opcion == "4":
            print("Gracias por usar el programa de votación.")
            break
        else:
            print("Opción inválida. Ingresa un número del 1 al 4.")

def tp3_pr():
    # Cargar datos del archivo CSV en un DataFrame
    candidatos_df = pd.read_csv('candidatos.csv', encoding='Latin-1') #El latin se investigo y es por que el csv tiene una codificacion dicerente a UTF-8
    # Seleccionar sólo los candidatos a Presidente y Vicepresidente
    pres_df = candidatos_df[candidatos_df['Candidato'] == 'Presidente y Vicepresidente']
    # Agrupar por partido político y candidato para contar los votos
    pres_counts = pres_df.groupby(['Partido', 'Nombre'])['Votos'].sum()
    # Ordenar los resultados de mayor a menor cantidad de votos y obtener los 3 primeros
    pres_top3 = pres_counts.sort_values(ascending=False)[:3]
    # Imprimir los resultados
    print('Los 3 candidatos con más votos para Presidente y Vicepresidente son:')
    for c, (partido, nombre) in enumerate(pres_top3.index):
        votos = pres_top3[c]
        print(f'{c+1}. {nombre} ({partido}): {votos} votos')

def tp3_al():
    # Cargar datos del archivo CSV en un DataFrame
    candidatos_df = pd.read_csv('candidatos.csv', encoding='Latin-1') #El latin se investigo y es por que el csv tiene una codificacion dicerente a UTF-8
    # Seleccionar sólo los candidatos a Alcalde
    pres_df = candidatos_df[candidatos_df['Candidato'] == 'Alcalde']
    # Agrupar por partido político y candidato para contar los votos
    pres_counts = pres_df.groupby(['Partido', 'Nombre'])['Votos'].sum()
    # Ordenar los resultados de mayor a menor cantidad de votos y obtener los 3 primeros
    pres_top3 = pres_counts.sort_values(ascending=False)[:3]
    # Imprimir los resultados
    print('Los 3 candidatos con más votos para Alcalde son:')
    for c, (partido, nombre) in enumerate(pres_top3.index):
        votos = pres_top3[c]
        print(f'{c+1}. {nombre} ({partido}): {votos} votos')

def tp3_dp():
    # Cargar datos del archivo CSV en un DataFrame
    candidatos_df = pd.read_csv('candidatos.csv', encoding='Latin-1') #El latin se investigo y es por que el csv tiene una codificacion dicerente a UTF-8
    # Seleccionar sólo los candidatos a Diputado
    pres_df = candidatos_df[candidatos_df['Candidato'] == 'Diputado']
    # Agrupar por partido político y candidato para contar los votos
    pres_counts = pres_df.groupby(['Partido', 'Nombre'])['Votos'].sum()
    # Ordenar los resultados de mayor a menor cantidad de votos y obtener los 3 primeros
    pres_top3 = pres_counts.sort_values(ascending=False)[:3]
    # Imprimir los resultados
    print('Los 3 candidatos con más votos para Diputado son:')
    for c, (partido, nombre) in enumerate(pres_top3.index):
        votos = pres_top3[c]
        print(f'{c+1}. {nombre} ({partido}): {votos} votos')

def administrador():
    print('Bienvenido admin')
    time.sleep(1)
    print('Este programa podra mostrarle el conteo de votos en tiempo real')
    time.sleep(1)
    print('Que desea realizar?')
    time.sleep(1)
    print('1. Contar votos de los top 3 candidatos a Presidente y Vicepresidente')
    time.sleep(1)
    print('2. Contar votos de los top 3 candidatos a Diputados')
    time.sleep(1)
    print('3. Contar votos de los top 3 candidatos a Alcalde')
    time.sleep(1)
    print('4. Salir')
    time.sleep(1)
    
    opcion = input('Por favor, seleccione una opción (1-4): ')
    while True:
        
        if opcion == '1':
            tp3_pr()
            break
        elif opcion == '2':
            tp3_dp()
            break
        elif opcion == '3':
            tp3_al()
            break
        elif opcion == '4':
            print("Gracias por usar esta seccion")
            break
        else:
            print('Entrada inválida. Por favor seleccione una opción numérica entre 1 y 4.')