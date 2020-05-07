import xml.etree.ElementTree as ET
file = open("exporta_notas.csv", "a")
file.write('Curso,NIE,Apellidos,Nombre,Asignatura,Abrev,Cdo-Asig,Nota\n')

import os
#directorio='/Users/miguelbuenocobos/PycharmProjects/xmlparse1/venv/Exportacion_de_Calificaciones'
with os.scandir() as entries:
    for entry in entries:
        #si el archivo no es xml no lo parsees
        if not entry.name.endswith('.xml'):continue
        print(entry.name)
        # construyo la matriz de asignaturas
        tree = ET.parse(entry.name)
        root = tree.getroot()
        x_materia: str = ''
        matriz_asignaturas = []
        for item in root.findall('./CURSOS/CURSO/UNIDADES/UNIDAD/MATERIAS/MATERIA'):
            for child in item:
                if child.tag == 'X_MATERIAOMG': matriz_asignaturas.append(child.text)
                if child.tag == 'D_MATERIAC': matriz_asignaturas.append(child.text)
                if child.tag == 'T_ABREV':matriz_asignaturas.append(child.text)
                if child.tag == 'X_SISTCAL': matriz_asignaturas.append(child.text)

        # construyo la matriz de notas

        elroot = tree.getroot()
        x_nota: str = ''
        matriz_notas = []
        for item in elroot.findall('./SISTEMAS_CALIFICACION/SISTEMA_CALIFICACION/CALIFICACIONES/CALIFICACION'):
            for child in item:
                if child.tag == 'X_CALIFICA':
                    x_nota = child.text
                if child.tag == 'D_CALIFICA':
                    matriz_notas.append(x_nota)
                    matriz_notas.append(child.text)

        # vamos a buscar las notas de cada alumno

        mytree = ET.parse(entry.name)
        myroot = mytree.getroot()
        for alumno in myroot.findall('./CURSOS/CURSO/UNIDADES/UNIDAD/ALUMNOS/ALUMNO'):
            if alumno.find('T_APELLIDO2').text : nombre_completo = alumno.find('C_NUMESCOLAR').text+','+ alumno.find('T_APELLIDO1').text + ' ' + alumno.find('T_APELLIDO2').text + ', ' + alumno.find('T_NOMBRE_ALU').text
            else: nombre_completo = alumno.find('C_NUMESCOLAR').text+','+ alumno.find('T_APELLIDO1').text  + ', ' + alumno.find('T_NOMBRE_ALU').text
            for item in alumno:
                item.find('MATERIAS_ALUMNO')
                for materias in item.findall('MATERIA_ALUMNO'):
                    asig = matriz_asignaturas[matriz_asignaturas.index(materias.find('X_MATERIAOMG').text) + 1]+','+matriz_asignaturas[matriz_asignaturas.index(materias.find('X_MATERIAOMG').text) + 2]+','+matriz_asignaturas[matriz_asignaturas.index(materias.find('X_MATERIAOMG').text)]
                    if materias.find('X_CALIFICA').text:
                        notai = matriz_notas[matriz_notas.index(materias.find('X_CALIFICA').text) + 1]
                    else:
                        notai = ''
                    file.write(entry.name.rstrip('.xml')+ ',' +nombre_completo + ',' + asig + ',' + notai + '\n')
                    # print(nombre_completo,';',asig,';',notai)
file.close()
