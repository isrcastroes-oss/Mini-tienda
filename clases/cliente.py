# -*- coding: utf-8 -*-
"""
Clase Cliente
Permite crear y gestionar clientes de la tienda
Cada cliente se guarda en data/clientes.json
y se le asigna un ID automático desde clientes_contador.txt
"""

from utils.archivos import leer_json, guardar_json, obtener_id
from utils.validaciones import validar_texto, validar_entero, validar_booleano

ARCHIVO_CLIENTES = "data/clientes.json"
CONTADOR_CLIENTES = "data/clientes_contador.txt"

def crear_cliente():
    """
    Crea un cliente nuevo con:
    - nombre
    - edad
    - activo (sí/no)
    Lo guarda en el archivo JSON de clientes
    """
    clientes = leer_json(ARCHIVO_CLIENTES)

    nuevo_cliente = {
        "id": obtener_id(CONTADOR_CLIENTES),
        "nombre": validar_texto("Nombre del cliente: "),
        "edad": validar_entero("Edad del cliente: "),
        "activo": validar_booleano("¿El cliente está activo?")
    }

    clientes.append(nuevo_cliente)
    guardar_json(ARCHIVO_CLIENTES, clientes)

    print(f"✅ Cliente '{nuevo_cliente['nombre']}' creado con ID {nuevo_cliente['id']}")

def listar_clientes():
    """
    Muestra todos los clientes registrados en la tienda
    """
    clientes = leer_json(ARCHIVO_CLIENTES)
    if not clientes:
        print("⚠️ No hay clientes registrados")
        return

    print("\n--- LISTA DE CLIENTES ---")
    for c in clientes:
        estado = "Activo" if c["activo"] else "Inactivo"
        print(f"ID: {c['id']} | Nombre: {c['nombre']} | Edad: {c['edad']} | {estado}")
    print("----------------------------\n")
