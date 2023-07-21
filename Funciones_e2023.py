# Universidad del Valle de Guatemala 
# Funciones CountMaster
# Mauricio Montenegro - 23679
# Daniel Leal - 23614
# Gabriel Soto - 23900
# Carlos Coc - 23859

import csv
import time
import pandas as pd
import matplotlib.pyplot as plt

def votar_presidente():
    while True:
        # Abrir el archivo CSV en modo de lectura
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
        print('7. Voto Nulo')
        time.sleep(1)
        # Pedir al usuario que seleccione un candidato
        opcion = input('Seleccione un candidato para votar (1-7): ')
        try:
            # Convertir la opción del usuario en un entero
            opcion = int(opcion)
            # Verificar si la opción es válida
            if opcion < 1 or opcion > 7:
                print('Error: opción inválida.')
                continue
            # Obtener el índice del candidato seleccionado en la lista de datos
            indice = opcion
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
            time.sleep(1)
            break
        except ValueError:
            print('Error: opción inválida.')

def votar_alcalde():
    while True:
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
            print('7. Voto Nulo')
            time.sleep(1)
            # Pedir al usuario que seleccione un candidato
            opcion = input('Seleccione un candidato para votar (1-7): ')
        try:
            # Convertir la opción del usuario en un entero
            opcion = int(opcion)
            
            # Verificar si la opción es válida
            if opcion < 1 or opcion > 7:
                print('Error: opción inválida.')
                continue
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
            elif opcion == 6:
                indice = 13
            else:
                indice = 14
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
            time.sleep(1)
            break
        except ValueError:
            print('Error: opción inválida.')

def votar_diputado():
    while True:
        # Abrir el archivo CSV en modo de escritura
        with open('candidatos.csv', mode='r') as file:
            # Crear un objeto reader del archivo CSV
            reader = csv.reader(file)
            # Leer los datos del archivo CSV en una lista
            data = list(reader)
            # Imprimir los candidatos a alcalde
            print('Candidatos a diputado:')
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
            print('7. Voto Nulo')
            time.sleep(1)
            # Pedir al usuario que seleccione un candidato
            opcion = input('Seleccione un candidato para votar (1-7): ')
            try:
                # Convertir la opción del usuario en un entero
                opcion = int(opcion)
                
                # Verificar si la opción es válida
                if opcion < 1 or opcion > 7:
                    print('Error: opción inválida.')
                    continue
                # Obtener el índice del candidato seleccionado en la lista de datos
                if opcion == 1:
                    indice = 15
                elif opcion == 2:
                    indice = 16
                elif opcion == 3:
                    indice = 17
                elif opcion == 4:
                    indice = 18
                elif opcion == 5:
                    indice = 19
                elif opcion == 6:
                    indice = 20
                else:
                    indice = 21
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
                time.sleep(1)
                break
            except ValueError:
                print('Error: opción inválida.')

def votante():
    # Variables booleanas para verificar si el usuario ya votó en cada elección
    voto_presidente = False
    voto_alcalde = False
    voto_diputado = False
    print("Bienvenido a la sección de votación.")
    time.sleep(1)
    print("Esta sección te permitirá votar por los candidatos a presidente, alcalde y diputado.")
    time.sleep(1)
    print("Para votar, simplemente ingresa el número correspondiente al candidato que deseas elegir.")
    time.sleep(1)
    print("A continuación, se te mostrará una lista de los candidatos para cada cargo y su partido político.")
    time.sleep(1)
    print("¡Comencemos!")
    time.sleep(1)
    # Solicitar nombre y número de DPI al usuario
    nombre = input("Ingrese su nombre: ")
    while True:
        dpi = input("Ingrese su número de DPI: ")
        # Verificar si el DPI contiene solo dígitos numéricos
        if dpi.isdigit():
            break
        else:
            print("Error: El número de DPI solo puede contener dígitos numéricos. Inténtelo nuevamente.")

    while True:
        print("Selecciona una opción:")
        print("1. Votar por presidente y vicepresidente")
        print("2. Votar por alcalde")
        print("3. Votar por diputado")
        time.sleep(1)
        opcion = input("""Ingresa el número de la opción que deseas: """)
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
        else:
            print("Opción inválida. Ingresa un número del 1 al 3.")
        # Verificar si el usuario ha votado en las tres opciones
        if voto_presidente and voto_alcalde and voto_diputado:
            print("¡Has votado en todas las opciones! Gracias por tu participación,", nombre + ".")
            time.sleep(3)
            break

def tp3_pr():
    # Cargar datos del archivo CSV en un DataFrame
    candidatos_df = pd.read_csv('candidatos.csv', encoding='Latin-1') #El latin se investigo y es por que el csv tiene una codificacion dicerente a UTF-8
    # Seleccionar sólo los candidatos a Presidente y Vicepresidente
    pres_df = candidatos_df[candidatos_df['Candidato'] == 'Presidente y Vicepresidente']
    # Agrupar por partido político y candidato para contar los votos
    pres_counts = pres_df.groupby(['Partido', 'Nombre'])['Votos'].sum()
    # Ordenar los resultados de mayor a menor cantidad de votos y obtener los 3 primeros
    pres_top3 = pres_counts.sort_values(ascending=False)[:3]
    # Calcular los votos totales
    votos_totales = pres_df['Votos'].sum()
    votos_totalestp3 = pres_top3.sum()
    # Imprimir los resultados
    print('\nLos 3 candidatos con más votos para Presidente y Vicepresidente son:')
    for c, (partido, nombre) in enumerate(pres_top3.index):
        votos = pres_top3[c]
        print(f'{c+1}. {nombre} ({partido}): {votos} votos')
    print(f'\nVotos totales en el top 3 para Presidente y Vicepresidente: {votos_totalestp3} votos')
    print(f'Votos totales para Presidente y Vicepresidente: {votos_totales} votos')
    time.sleep(3)

    # Seleccionar sólo los candidatos a Presidente y Vicepresidente
    pres_df = candidatos_df[candidatos_df['Candidato'] == 'Presidente y Vicepresidente']
    # Agrupar por partido político y candidato para contar los votos
    pres_counts = pres_df.groupby(['Partido', 'Nombre'])['Votos'].sum()
    # Ordenar los resultados de mayor a menor cantidad de votos y obtener los 3 primeros
    pres_top3 = pres_counts.sort_values(ascending=False)[:3]
    # Calcular los porcentajes de votos
    total_votos = pres_top3.sum()
    porcentajes = (pres_top3 / total_votos) * 100
    # Convertir los índices y valores en listas
    candidatos = [f'{nombre} ({partido})' for partido, nombre in porcentajes.index]
    valores = porcentajes.values
    # Crear la gráfica de pastel de los porcentajes de votos
    plt.pie(valores, labels=candidatos, autopct='%1.1f%%')
    plt.title('Porcentaje de votos para los 3 candidatos con más votos para Presidente y Vicepresidente')
    # Mostrar la gráfica
    plt.show()

def tp3_al():
    # Cargar datos del archivo CSV en un DataFrame
    candidatos_df = pd.read_csv('candidatos.csv', encoding='Latin-1') #El latin se investigo y es por que el csv tiene una codificacion dicerente a UTF-8
    # Seleccionar sólo los candidatos a Alcalde
    alc_df = candidatos_df[candidatos_df['Candidato'] == 'Alcalde']
    # Agrupar por partido político y candidato para contar los votos
    alc_counts = alc_df.groupby(['Partido', 'Nombre'])['Votos'].sum()
    # Ordenar los resultados de mayor a menor cantidad de votos y obtener los 3 primeros
    alc_top3 = alc_counts.sort_values(ascending=False)[:3]
    # Calcular los votos totales
    votos_totales = alc_df['Votos'].sum()
    votos_totalestp3 = alc_top3.sum()
    # Imprimir los resultados
    print('\nLos 3 candidatos con más votos para Alcalde son:')
    for c, (partido, nombre) in enumerate(alc_top3.index):
        votos = alc_top3[c]
        print(f'{c+1}. {nombre} ({partido}): {votos} votos')
    print(f'\nVotos totales en el top 3 para Alcalde: {votos_totalestp3} votos')
    print(f'Votos totales para Alcalde: {votos_totales} votos')
    time.sleep(3)

    # Seleccionar sólo los candidatos a Alcalde
    alcalde_df = candidatos_df[candidatos_df['Candidato'] == 'Alcalde']
    # Agrupar por partido político y candidato para contar los votos
    alcalde_counts = alcalde_df.groupby(['Partido', 'Nombre'])['Votos'].sum()
    # Ordenar los resultados de mayor a menor cantidad de votos y obtener los 3 primeros
    alcalde_top3 = alcalde_counts.sort_values(ascending=False)[:3]
    # Calcular los porcentajes de votos
    total_votos = alcalde_top3.sum()
    porcentajes = (alcalde_top3 / total_votos) * 100
    # Convertir los índices y valores en listas
    candidatos = [f'{nombre} ({partido})' for partido, nombre in porcentajes.index]
    valores = porcentajes.values
    # Crear la gráfica de pastel de los porcentajes de votos
    plt.pie(valores, labels=candidatos, autopct='%1.1f%%')
    plt.title('Porcentaje de votos para los 3 candidatos con más votos para Alcalde')
    # Mostrar la gráfica
    plt.show()

def tp3_dp():
    # Cargar datos del archivo CSV en un DataFrame
    candidatos_df = pd.read_csv('candidatos.csv', encoding='Latin-1') #El latin se investigo y es por que el csv tiene una codificacion dicerente a UTF-8
    # Seleccionar sólo los candidatos a Diputado
    dp_df = candidatos_df[candidatos_df['Candidato'] == 'Diputado']
    # Agrupar por partido político y candidato para contar los votos
    dp_counts = dp_df.groupby(['Partido', 'Nombre'])['Votos'].sum()
    # Ordenar los resultados de mayor a menor cantidad de votos y obtener los 3 primeros
    dp_top3 = dp_counts.sort_values(ascending=False)[:3]
    # Calcular los votos totales
    votos_totales = dp_df['Votos'].sum()
    votos_totalestp3 = dp_top3.sum()
    # Imprimir los resultados
    print('\nLos 3 candidatos con más votos para Diputado son:')
    for c, (partido, nombre) in enumerate(dp_top3.index):
        votos = dp_top3[c]
        print(f'{c+1}. {nombre} ({partido}): {votos} votos')
    print(f'\nVotos totales en el top 3 para Alcalde: {votos_totalestp3} votos')
    print(f'Votos totales para Alcalde: {votos_totales} votos')
    time.sleep(3)

    # Seleccionar sólo los candidatos a Diputado
    diputado_df = candidatos_df[candidatos_df['Candidato'] == 'Diputado']
    # Agrupar por partido político y candidato para contar los votos
    diputado_counts = diputado_df.groupby(['Partido', 'Nombre'])['Votos'].sum()
    # Ordenar los resultados de mayor a menor cantidad de votos y obtener los 3 primeros
    diputado_top3 = diputado_counts.sort_values(ascending=False)[:3]
    # Calcular los porcentajes de votos
    total_votos = diputado_top3.sum()
    porcentajes = (diputado_top3 / total_votos) * 100
    # Convertir los índices y valores en listas
    candidatos = [f'{nombre} ({partido})' for partido, nombre in porcentajes.index]
    valores = porcentajes.values
    # Crear la gráfica de pastel de los porcentajes de votos
    plt.pie(valores, labels=candidatos, autopct='%1.1f%%')
    plt.title('Porcentaje de votos para los 3 candidatos con más votos para Diputado')
    # Mostrar la gráfica
    plt.show()

def administrador():
    # Definir la contraseña requerida para acceder como administrador
    contraseña_correcta = "contraseña123"
    while True:
        print('Bienvenido admin')
        print('Esta sección podrá mostrarle el conteo de votos en tiempo real')
        print('¿Qué desea realizar?')
        time.sleep(1)
        print('1. Contar votos de los top 3 candidatos a Presidente y Vicepresidente')
        time.sleep(1)
        print('2. Contar votos de los top 3 candidatos a Alcalde')
        time.sleep(1)
        print('3. Contar votos de los top 3 candidatos a Diputados')
        time.sleep(1)
        print('4. Salir')
        time.sleep(1)
        opcion = input("""Por favor, seleccione una opción (1-4): """)
        # Solicitar la contraseña al usuario
        if opcion in ['1', '2', '3']:
            contraseña = input("Ingrese la contraseña de administrador: ")

            # Verificar si la contraseña ingresada es correcta
            if contraseña == contraseña_correcta:
                if opcion == '1':
                    tp3_pr()
                elif opcion == '2':
                    tp3_al()
                elif opcion == '3':
                    tp3_dp()
            else:
                print("Contraseña incorrecta. Acceso denegado.")
                time.sleep(2)
        elif opcion == '4':
            print("Gracias por usar esta sección")
            return
        else:
            print('Error: opción inválida.')
            print('Ingrese una opción entre 1-4')
