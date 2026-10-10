#Ejercicio 1: Aplicación ToDo en línea de comandos


tasks = [
    {
        "id": 1,
        "title": "Learn Python Functions",
        "priority": "High",
        "status": "Pending"
    },
    {
        "id": 2,
        "title": "Build CLI App",
        "priority": "Medium",
        "status": "In Progress"
    }
]


def add_task(title, priority="Medium", **details):
    new_id = max([task["id"] for task in tasks], default=0) + 1

    new_task = {
        "id": new_id,
        "title": title,
        "priority": priority,
        "status": "Pending"
    }

    new_task.update(details)
    tasks.append(new_task)

    print("Tarea agregada correctamente:", new_task)


def view_tasks(*task_ids):
    if not task_ids:
        for task in tasks:
            print(task)
    else:
        for task_id in task_ids:
            found = False

            for task in tasks:
                if task["id"] == task_id:
                    print(task)
                    found = True

            if not found:
                print(f"No existe la tarea con ID {task_id}")


def update_task(task_id, **updates):
    for task in tasks:
        if task["id"] == task_id:
            task.update(updates)
            print("Tarea actualizada:", task)
            return

    print("No se encontró la tarea.")


def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Tarea eliminada correctamente.")
            return

    print("No se encontró la tarea.")


# Menú interactivo
while True:
    print("LISTA DE TAREAS")
    print("1.Agregar tarea")
    print("2.Ver tareas")
    print("3.Actualizar tarea")
    print("4.Eliminar tarea")
    print("5.Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        titulo = input("Título de la tarea: ")
        prioridad = input("Prioridad (High, Medium, Low): ")
        add_task(titulo, priority=prioridad or "Medium")

    elif opcion == "2":
        ids = input("IDs separados por comas (Enter para ver todas): ")

        if ids.strip():
            try:
                task_ids = [
                    int(task_id.strip())
                    for task_id in ids.split(",")
                ]
                view_tasks(*task_ids)
            except ValueError:
                print("Ingresa únicamente números separados por comas.")
        else:
            view_tasks()

    elif opcion == "3":
        try:
            task_id = int(input("ID de la tarea: "))
            nuevo_titulo = input("Nuevo título: ")
            nuevo_estado = input("Nuevo estado: ")

            cambios = {}

            if nuevo_titulo:
                cambios["title"] = nuevo_titulo

            if nuevo_estado:
                cambios["status"] = nuevo_estado

            update_task(task_id, **cambios)

        except ValueError:
            print("El ID debe ser un número.")

    elif opcion == "4":
        try:
            task_id = int(input("ID de la tarea que deseas eliminar: "))
            delete_task(task_id)
        except ValueError:
            print("El ID debe ser un número.")

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
