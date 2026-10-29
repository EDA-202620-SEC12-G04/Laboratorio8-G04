"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones
 *
 * Dario Correal
 """

import sys
import App.logic as logic

"""
La vista se encarga de la interacción con el usuario
Presenta el menú de opciones y por cada selección
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
#  -------------------------------------------------------------
# Funciones para la carga de datos
#  -------------------------------------------------------------

def new_logic():
    """
    Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

#  -------------------------------------------------------------
# Funciones para la correcta impresión de los datos
#  -------------------------------------------------------------

def print_menu():
    """
    Menu de usuario
    """
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de crimenes")
    print("3- Consultar crimenes en un rango de fechas")
    print("4- Consultar crimenes por codigo y fecha")
    print("5- Consultar crimenes por Reporting Area")
    print("0- Salir")
    print("*******************************************")

# main del ejercicio
def main():
    """
    Menú principal
    """
    # bandera para controlar el ciclo del menu
    working = True
    control = None
    crimefile = 'Boston Crimes//crime-utf8.csv'

    # ciclo del menu
    while working:
        print_menu()
        inputs = input("Seleccione una opción para continuar\n").strip()
        if not inputs or not inputs[0].isdigit():
            print("Opción no válida")
            continue
            
        option = int(inputs[0])
        if option == 1:
            print("\nInicializando....")
            # cont es el controlador que se usará de acá en adelante
            control = new_logic()
        elif option == 2:
            if control is None:
                print("\nDebe inicializar el analizador primero.")
                continue
            print("\nCargando información de crimenes ....")
            logic.load_data(control, crimefile)
            print('Crimenes cargados: ' + str(logic.crimes_size(control)))
            print('Altura del arbol: ' + str(logic.index_height(control)))
            print('Elementos en el arbol: ' + str(logic.index_size(control)))
            print('Menor Llave: ' + str(logic.min_key(control)))
            print('Mayor Llave: ' + str(logic.max_key(control)))

        elif option == 3:
            if control is None:
                print("\nDebe inicializar el analizador primero.")
                continue
            print("\nBuscando crimenes en un rango de fechas: ")
            initialDate = input("Fecha Inicial (YYYY-MM-DD): ")
            finalDate = input("Fecha Final (YYYY-MM-DD): ")
            try:
                total = logic.get_crimes_by_range(control, initialDate, finalDate)
            except ValueError:
                print("\nLas fechas deben tener el formato YYYY-MM-DD.")
                continue
            print("\nTotal de crimenes en el rango de fechas: " + str(total))

        elif option == 4:
            if control is None:
                print("\nDebe inicializar el analizador primero.")
                continue
            print("\nBuscando crimenes x grupo de ofensa en una fecha: ")
            initialDate = input("Fecha (YYYY-MM-DD): ")
            offensecode = input("Ofensa: ")
            try:
                numoffenses = logic.get_crimes_by_range_code(
                    control, initialDate, offensecode)
            except ValueError:
                print("\nLa fecha debe tener el formato YYYY-MM-DD.")
                continue
            print("\nTotal de ofensas tipo: " + offensecode + " en esa fecha:  " +
                str(numoffenses))
        elif option == 5:
            if control is None:
                print("\nDebe inicializar el analizador primero.")
                continue
            print("\nBuscando crimenes en un rango de areas: ")
            initialArea = input("Area inicial: ")
            finalArea = input("Area final: ")
            try:
                area = logic.get_crimes_by_range_area(
                    control, initialArea, finalArea)
            except ValueError:
                print("\nLas areas deben ser números enteros.")
                continue
            print("\nTotal de crimenes en el rango de areas: " + str(area))
        else:
            sys.exit(0)
    sys.exit(0)
