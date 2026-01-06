# -*- coding: utf-8 -*-
"""
Clase Empleado
Permite crear y gestionar empleados de la tienda
Cada empleado se guarda en data/empleados.json
y se le asigna un ID automático desde empleados_contador.txt
"""

from utils.archivos import leer_json, guardar_json, obtener_id
from utils.validaciones import validar_texto, validar_entero, validar_booleano

ARCHIVO_EMPLEADOS = "data/empleados.json"
CONTADOR_EMPLEADOS = "data/empleados_contador.txt"

def crear_empleado():
    """
    Crea un empleado nuevo con:
    - nombre
    - edad
    - activo (sí/no)
    Lo guarda en el archivo JSON de empleados
    """
    empleados = leer_json(ARCHIVO_EMPLEADOS)

    nuevo_empleado = {
        "id": obtener_id(CONTADOR_EMPLEADOS),
        "nombre": validar_texto("Nombre del empleado: "),
        "edad": validar_entero("Edad del empleado: "),
        "activo": validar_booleano("¿El empleado está activo?")
    }

    empleados.append(nuevo_empleado)
    guardar_json(ARCHIVO_EMPLEADOS, empleados)

    print(f"✅ Empleado '{nuevo_empleado['nombre']}' creado con ID {nuevo_empleado['id']}")

def listar_empleados():
    """
    Muestra todos los empleados registrados en la tienda
    """
    empleados = leer_json(ARCHIVO_EMPLEADOS)
    if not empleados:
        print("⚠️ No hay empleados registrados")
        return

    print("\n--- LISTA DE EMPLEADOS ---")
    for e in empleados:
        estado = "Activo" if e["activo"] else "Inactivo"
        print(f"ID: {e['id']} | Nombre: {e['nombre']} | Edad: {e['edad']} | {estado}")
    print("----------------------------\n")
