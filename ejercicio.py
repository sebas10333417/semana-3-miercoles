students = {}

continuar = True

while continuar:
    
    list_tex = int(input ("""
    1. Agregar estudiantes
    2. Buscar estudiante por ID
    3. Actualizar informacion de estudiante 
    4. Eliminar estudiante
    5. Calcular el promedio de notas
    6. Listar estudiantes con notas inferiores a un umbral (ejemplo 3.0)\n
    ingrese la opcion deseada \n
    """))
    if list_tex == 1:
        id = int(input("Por favor ingresa el ID del estudiante -> \n"))
        user = input("Agrega el nombre del estudiante -> \n ")
        user2 = input("Agrega el apellido del estudiante -> \n ")
        old = input("Agrega la edad del estudiante -> \n ")
        note = float(input("Agrega la Nota del estudiante -> \n "))

        students[id] = {
            "Nombre" : user,
            "Apellido" : user2,
            "Edad" : old,
            "Nota" : note
        }
    
        for i, n in students.items():
            print(i, n)
                
    elif list_tex == 2:
        consult = int(input("Igresa el ID que deseas consultar -> :"))
        if consult != id:
            print("El ID no se encuentra registrado:")
        else:
            list_students = students.get(consult)
            
            print("Los datos almacenados en el ID son: \n")
            print(f"{consult} {list_students}")
    
    elif list_tex == 3:
        update = input("Quieres actualizar la edad del estudiante? \n si/no ")
        if update == "si":
            cam_id = int(input("Ingrese el ID del estudiante que desea actualizar la edad: \n "))
            new_age = int(input("Ingrese la edad actualizada"))
            students[cam_id] ["Edad"] = new_age
            date = students.get(cam_id)
            print(cam_id,date)
            

