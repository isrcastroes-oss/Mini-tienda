
# -*- coding: utf-8 -*-
"""
Archivo principal del sistema Mini Tienda.
Muestra el menú y llama a las funciones de cada módulo.
"""

from clases.producto import crear_producto, listar_productos
from clases.cliente import crear_cliente, listar_clientes
from clases.empleado import crear_empleado, listar_empleados
from clases.venta import registrar_venta, listar_ventas
from clases.pago import registrar_pago, listar_pagos

# Colores ANSI para la consola
RESET = "\033[0m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
CYAN = "\033[36m"

def mostrar_menu():
    """
    Muestra el menú principal del sistema
    """
    print(AZUL + "\n=== MINI TIENDA EN CONSOLA ===" + RESET)
    print(AMARILLO + """
1. Crear producto
2. Listar productos
3. Crear cliente
4. Listar clientes
5. Crear empleado
6. Listar empleados
7. Registrar venta
8. Listar ventas
9. Registrar pago
10. Listar pagos
11. Salir
""" + RESET)

def main():
    """
    Función principal que controla el flujo del programa
    """
    while True:
        mostrar_menu()
        opcion = input(CYAN + "Opción: " + RESET).strip()

        if opcion == "1":
            crear_producto()

        elif opcion == "2":
            listar_productos()

        elif opcion == "3":
            crear_cliente()

        elif opcion == "4":
            listar_clientes()

        elif opcion == "5":
            crear_empleado()

        elif opcion == "6":
            listar_empleados()

        elif opcion == "7":
            registrar_venta()

        elif opcion == "8":
            listar_ventas()

        elif opcion == "9":
            registrar_pago()

        elif opcion == "10":
            listar_pagos()

        elif opcion == "11":
            print(VERDE + "\n¡Gracias por usar la Mini Tienda!" + RESET)
            break

        else:
            print(ROJO + "❌ Opción inválida, intente de nuevo" + RESET)

if __name__ == "__main__":
    main()
