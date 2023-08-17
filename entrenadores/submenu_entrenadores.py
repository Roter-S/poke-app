from entrenadores.opciones.ver_entrenadores import ver_listado_por_nombre_entrenador, ver_todos_los_entrenadores
from entrenadores.opciones.buscar_entrenadores import buscar_por_id, buscar_por_nombre

# Función para mostrar el submenú de opciones relacionadas con Entrenadores
def submenu_entrenadores(entrenadores):
    while True:
        print("\n--- Submenú de Opciones de Entrenadores ---")
        print("1. Ver todos los entrenadores")
        print("2. Ver listado por nombre")
        print("3. Buscar por ID")
        print("4. Buscar entrenador por nombre")
        print("5. Regresar al menú principal")
        opcion_entrenador = int(input("Seleccione una opción: "))

        if opcion_entrenador == 1:
            ver_todos_los_entrenadores(entrenadores)
        elif opcion_entrenador == 2:
            ver_listado_por_nombre_entrenador(entrenadores)
        elif opcion_entrenador == 3:
            buscar_por_id(entrenadores)
        elif opcion_entrenador == 4:
            buscar_por_nombre(entrenadores)
        elif opcion_entrenador == 5:
            break
        else:
            print("Opción inválida. Intente nuevamente.")
