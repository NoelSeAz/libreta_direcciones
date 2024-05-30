from libreta_direcciones import LibretaDirecciones
from contacto import Contacto
import pandas as pd
from tabulate import tabulate

def mostrar_menu(count):
    """Muestra el menú principal con la cantidad de contactos actuales."""
    menu = [
        ["1", "Añadir contacto"],
        ["2", "Buscar contacto"],
        ["3", "Modificar contacto"],
        ["4", "Eliminar contacto"],
        ["5", "Salir"]
    ]
    print("Libreta de Direcciones\n")
    print(tabulate(menu, headers=["Libreta Direcciones   Total: " + count], tablefmt="grid"))

def mostrar_submenu_busqueda():
    """Muestra el submenú para seleccionar el criterio de búsqueda."""
    submenu = [
        ["1", "Nombre"],
        ["2", "Apellido"],
        ["3", "Teléfono"],
        ["4", "Mostrar todos los contactos"],
        ["", "Cualquier otra letra Volver al menú principal"]
    ]
    print("\nBuscar por:\n")
    print(tabulate(submenu, headers=["Buscar Contacto"], tablefmt="grid"))

def mostrar_submenu_modificacion():
    """Muestra el submenú para seleccionar el campo a modificar."""
    submenu = [
        ["1", "Nombre"],
        ["2", "Apellido"],
        ["3", "Teléfono"],
        ["4", "Dirección"],
        ["5", "Empleo"],
        ["", "Cualquier otra letra Volver al menú principal"]
    ]
    print("\nModificar campo:\n")
    print(tabulate(submenu, headers=["Modificar Contacto"], tablefmt="grid"))

def main():
    """Función principal que ejecuta el menú y las opciones seleccionadas por el usuario."""
    libreta = LibretaDirecciones()

    while True:
        count = str(libreta.contar_contactos())
        mostrar_menu(count)
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Añadir un nuevo contacto
            nombre = input("\nNombre: ")
            apellido = input("Apellido: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            empleo = input("Empleo: ")
            nuevo_contacto = Contacto(nombre, apellido, telefono, direccion, empleo)
            libreta.agregar_contacto(nuevo_contacto)
            print("\nContacto añadido.\n")

        elif opcion == '2':
            # Buscar un contacto
            mostrar_submenu_busqueda()
            criterio_opcion = input("\nSelecciona un criterio de búsqueda: ")
            if criterio_opcion == '1':
                criterio = "nombre"
            elif criterio_opcion == '2':
                criterio = "apellido"
            elif criterio_opcion == '3':
                criterio = "telefono"
            elif criterio_opcion == '4':
                resultados = libreta.obtener_todos_contactos()
                if not resultados.empty:
                    print("\n" + tabulate(resultados, headers='keys', tablefmt='grid', showindex=False) + "\n")
                else:
                    print("\nNo se encontraron resultados.\n")
                continue
            else:
                print("\nVolviendo al menú principal...\n")
                continue
            valor = input(f"\nIntroduce el {criterio}: ")
            resultados = libreta.buscar_contacto(criterio, valor)
            if not resultados.empty:
                print("\n" + tabulate(resultados, headers='keys', tablefmt='grid', showindex=False) + "\n")
            else:
                print("\nNo se encontraron resultados.\n")

        elif opcion == '3':
            # Modificar un contacto existente
            contacto_id = int(input("\nID del contacto a modificar: "))
            mostrar_submenu_modificacion()
            campo_opcion = input("\nSelecciona un campo a modificar: \n")
            if campo_opcion == '1':
                campo = "nombre"
            elif campo_opcion == '2':
                campo = "apellido"
            elif campo_opcion == '3':
                campo = "telefono"
            elif campo_opcion == '4':
                campo = "direccion"
            elif campo_opcion == '5':
                campo = "empleo"
            else:
                print("\nVolviendo al menú principal...\n")
                continue
            nuevo_valor = input(f"\nIntroduce el nuevo {campo}: ")
            libreta.modificar_contacto(contacto_id, {campo: nuevo_valor})
            print("\nContacto modificado.\n")

        elif opcion == '4':
            # Eliminar un contacto por ID
            contacto_id = int(input("\nID del contacto a eliminar: "))
            libreta.eliminar_contacto(contacto_id)
            print("\nContacto eliminado.\n")

        elif opcion == '5':
            # Salir del programa
            break

        else:
            print("\nOpción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()
