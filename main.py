# -*- coding: utf-8 -*-
"""
Archivo principal del sistema Mini Tienda.
Menú principal con submenús por categoría.
"""

from clases.producto import crear_producto, listar_productos
from clases.cliente import crear_cliente, listar_clientes
from clases.empleado import crear_empleado, listar_empleados
from clases.venta import registrar_venta, listar_ventas
from clases.pago import registrar_pago, listar_pagos

# Colores ANSI
RESET = "\033[0m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
CYAN = "\033[36m"


def menu_principal():
    print(AZUL + "\n=== MINI TIENDA ===" + RESET)
    print(AMARILLO + """
1. Productos
2. Clientes
3. Empleados
4. Ventas
5. Pagos
6. Salir
""" + RESET)


def menu_productos():
    print(CYAN + """
--- PRODUCTOS ---
1. Crear producto
2. Listar productos
3. Volver
""" + RESET)


def menu_clientes():
    print(CYAN + """
--- CLIENTES ---
1. Crear cliente
2. Listar clientes
3. Volver
""" + RESET)


def menu_empleados():
    print(CYAN + """
--- EMPLEADOS ---
1. Crear empleado
2. Listar empleados
3. Volver
""" + RESET)


def menu_ventas():
    print(CYAN + """
--- VENTAS ---
1. Registrar venta
2. Listar ventas
3. Volver
""" + RESET)


def menu_pagos():
    print(CYAN + """
--- PAGOS ---
1. Registrar pago
2. Listar pagos
3. Volver
""" + RESET)


def main():
    while True:
        menu_principal()
        opcion = input("Opción: ").strip()

        # PRODUCTOS
        if opcion == "1":
            while True:
                menu_productos()
                op = input("Opción: ").strip()

                if op == "1":
                    crear_producto()
                elif op == "2":
                    listar_productos()
                elif op == "3":
                    break
                else:
                    print(ROJO + "Opción inválida" + RESET)

        # CLIENTES
        elif opcion == "2":
            while True:
                menu_clientes()
                op = input("Opción: ").strip()

                if op == "1":
                    crear_cliente()
                elif op == "2":
                    listar_clientes()
                elif op == "3":
                    break
                else:
                    print(ROJO + "Opción inválida" + RESET)

        # EMPLEADOS
        elif opcion == "3":
            while True:
                menu_empleados()
                op = input("Opción: ").strip()

                if op == "1":
                    crear_empleado()
                elif op == "2":
                    listar_empleados()
                elif op == "3":
                    break
                else:
                    print(ROJO + "Opción inválida" + RESET)

        # VENTAS
        elif opcion == "4":
            while True:
                menu_ventas()
                op = input("Opción: ").strip()

                if op == "1":
                    registrar_venta()
                elif op == "2":
                    listar_ventas()
                elif op == "3":
                    break
                else:
                    print(ROJO + "Opción inválida" + RESET)

        # PAGOS
        elif opcion == "5":
            while True:
                menu_pagos()
                op = input("Opción: ").strip()

                if op == "1":
                    registrar_pago()
                elif op == "2":
                    listar_pagos()
                elif op == "3":
                    break
                else:
                    print(ROJO + "Opción inválida" + RESET)

        # SALIR
        elif opcion == "6":
            print(VERDE + "\n¡Gracias por usar la Mini Tienda!" + RESET)
            break

        else:
            print(ROJO + "❌ Opción inválida" + RESET)


if __name__ == "__main__":
    main()
