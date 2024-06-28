import random

pro=0
promedio=0
res=0
alumnos = {}



def registrar_alumno(): #funcion que permite agregar un alumno

  try:

    codigo = random.randint(100, 999) #le asigna un numero aleatorio 
    nombre = input("Ingrese el nombre del alumno: ")
    apellido= input("Ingrese el apellido del alumno: ")
    pimera = float(input("Ingrese la primera nota : "))
    segunda = float(input("Ingrese la segunda nota : "))
    tercera = float(input("Ingrese la tercera nota "))

    #se agrega a al diccionario automaticamente con su llave
    alumnos[codigo] = {

      'nombre': nombre,
      'apellido': apellido,
      'primera': primera,
      'segunda': segunda,
      'tercera': tercera,

    }
    
    print(f"alumno agregada exitosamente con el código {codigo}!")

  except ValueError:
    print("solo ingrese numeros en las notas")



def listar_alumnos():

  if alumnos:
    #se enpieza a nombrar todo lo que contiene
    for codigo, datos in alumnos.items():

      print(f"Código: {codigo}")
      print(f"Nombre: {datos['nombre']}")
      print(f"apellido: {datos["apellido"]}")
      print(f"primera: {datos['primera']}")
      print(f"segunda: {datos['seunda']}")
      print(f"tercera: {datos['tercera']}")
  else:
    print("No hay alumnos registrados aun")


def buscar_alumno():
  try:
    #segun el codigo buscara al alumno que le pertenesca
    codigo_buscar = int(input("Ingrese el codigo del alumno: "))
    if codigo_buscar in alumnos:

      datos = alumnos[codigo_buscar]

      print(f"Código: {codigo}")
      print(f"Nombre: {datos['nombre']}")
      print(f"apellido: {datos["apellido"]}")
      print(f"primera: {datos['primera']}")
      print(f"segunda: {datos['seunda']}")
      print(f"tercera: {datos['tercera']}")

    else:

      print("No hay alumnos con ese codigo")

  except ValueError:
    print("codigo desconocido ")

def promedio_notas ():
    if codigo_buscar in alumnos:

      datos = alumnos[codigo_buscar]

      print(f"Código: {codigo}")
      print(f"Nombre: {datos['nombre']}")
      print(f"apellido: {datos["apellido"]}")
      print(f"primera: {datos['primera']}")
      print(f"segunda: {datos['seunda']}")
      print(f"tercera: {datos['tercera']}")
        promedio=primera+segunda+tercera
        pro=pro+1
    res=promedio/pro
    print(F"el promedio de los alumnos es {res}")
    else:

      print("No hay alumnos ingresados aun")






def guardar_alumnos():

  try:

    with open("alumnos.txt", "w") as archivo:

      for codigo, datos in alumnos.items():
        archivo.write(f"Código: {codigo}\n")
        archivo.write(f"Nombre: {datos['nombre']}\n")
        archivo.write(f"apellido: {datos['apellido']}\n")
        archivo.write(f"primera: {datos['primera']}\n")
        archivo.write(f"segunda: {datos['segunda']}\n")
        archivo.write(f"tercera: {datos['tercera']}\n\n")

    print("Películas guardadas en alumnos.txt")

  except Exception as e:

    print(f"no se pudo guardar el archivo: {e}")


if __name__ == "__main__":

  menu()