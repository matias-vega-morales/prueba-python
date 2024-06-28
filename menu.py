import codigos 

while True:

    print("*******Menú de gestion*******")
    print("1) agregar alumno")
    print("2) ver todos los alumnos ")
    print("3) buscar al alumno")
    print("4) promedio de notas")
    print("4) selir y guardar")
    print("*****************************")
    
    try:

      opcion = int(input("Seleccione una opción: "))
      if opcion == 1:

        registrar_alumno()

      elif opcion == 2:

        listar_alumnos()

      elif opcion == 3:

        buscar_alumno()

      elif opcion == 4:
        promedio_notas()
        
      elif opcion == 5:

        guardar_alumnos()

        print("guardando...")
        print("bye")
        break

      else:

        print("solo existen estas opciones 1-2-3-4-5")
    except ValueError:
      print("Ingrese solo numeros validos pls ")

