# NotasSenecaaCSV
Programa en python que genera un csv con las  notas de cada alumno en una fila por nota a partir de todos los xml que encuentre en el mismo directorio.

Los xml que sabe parsear son los que genera séneca en exportación de datos/datos de la evaluación,  uno por unidad del centro y todos comprimidos en un zip.

Para ejecutarlo extraer todos los xml en la misma carpeta que el programa y trs ejecutarlo tendremos un csv llamado exporta_notas.csv con esta info:
 
  Curso,NIE,Apellidos,Nombre,Asignatura,Abrev,Cdo-Asig,Nota
  
una fila por asignatura de la matricula del centro.  
