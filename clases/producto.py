# -*- coding: utf-8 -*-
"""
Clase Producto
Permite crear y gestionar productos de la tienda
Cada producto se guarda en data/productos.json
y se le asigna un ID automático desde productos_contador.txt
"""

from utils.archivos import leer_json, guardar_json, obtener_id
from utils.validaciones import validar_texto, validar_float, validar_booleano

ARCHIVO_PRODUCTOS = "data/productos.json"
CONTADOR_PRODUCTOS = "data/productos_contador.txt"

def crear_producto():
    """
    Crea un producto nuevo con:
    - nombre
    - precio
    - activo (sí/no)
    Lo guarda en el archivo JSON de productos
    """
    productos = leer_json(ARCHIVO_PRODUCTOS)

    nuevo_producto = {
        "id": obtener_id(CONTADOR_PRODUCTOS),
        "nombre": validar_texto("Nombre del producto: "),
        "precio": validar_float("Precio del producto: "),
        "activo": validar_booleano("¿El producto está activo?")
    }

    productos.append(nuevo_producto)
    guardar_json(ARCHIVO_PRODUCTOS, productos)

    print(f"✅ Producto '{nuevo_producto['nombre']}' creado con ID {nuevo_producto['id']}")

def listar_productos():
    """
    Muestra todos los productos registrados en la tienda
    """
    productos = leer_json(ARCHIVO_PRODUCTOS)
    if not productos:
        print("⚠️ No hay productos registrados")
        return

    print("\n--- LISTA DE PRODUCTOS ---")
    for p in productos:
        estado = "Activo" if p["activo"] else "Inactivo"
        print(f"ID: {p['id']} | Nombre: {p['nombre']} | Precio: ${p['precio']} | {estado}")
    print("----------------------------\n")
