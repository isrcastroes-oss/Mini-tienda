# -*- coding: utf-8 -*-
"""
Clase Venta
Permite registrar y listar ventas de la tienda
Cada venta se guarda en data/ventas.json
y se le asigna un ID automático desde ventas_contador.txt
"""

from utils.archivos import leer_json, guardar_json, obtener_id
from utils.validaciones import validar_entero
from clases.producto import listar_productos
from clases.cliente import listar_clientes
from clases.empleado import listar_empleados

ARCHIVO_VENTAS = "data/ventas.json"
CONTADOR_VENTAS = "data/ventas_contador.txt"

def registrar_venta():
    """
    Registra una venta:
    - Selecciona un cliente por ID
    - Selecciona un empleado por ID
    - Selecciona un producto por ID
    - Ingresa cantidad
    - Calcula total automáticamente
    """
    clientes = leer_json("data/clientes.json")
    empleados = leer_json("data/empleados.json")
    productos = leer_json("data/productos.json")
    ventas = leer_json(ARCHIVO_VENTAS)

    if not clientes or not empleados or not productos:
        print("⚠️ Debe existir al menos un cliente, empleado y producto para registrar la venta.")
        return

    print("\n--- CLIENTES DISPONIBLES ---")
    listar_clientes()
    id_cliente = validar_entero("Ingrese ID del cliente: ")
    if not any(c["id"] == id_cliente for c in clientes):
        print("❌ Cliente no encontrado")
        return

    print("\n--- EMPLEADOS DISPONIBLES ---")
    listar_empleados()
    id_empleado = validar_entero("Ingrese ID del empleado: ")
    if not any(e["id"] == id_empleado for e in empleados):
        print("❌ Empleado no encontrado")
        return

    print("\n--- PRODUCTOS DISPONIBLES ---")
    listar_productos()
    id_producto = validar_entero("Ingrese ID del producto: ")
    if not any(p["id"] == id_producto for p in productos):
        print("❌ Producto no encontrado")
        return

    cantidad = validar_entero("Cantidad a vender: ")
    producto = next(p for p in productos if p["id"] == id_producto)
    total = producto["precio"] * cantidad

    nueva_venta = {
        "id": obtener_id(CONTADOR_VENTAS),
        "cliente_id": id_cliente,
        "empleado_id": id_empleado,
        "producto_id": id_producto,
        "cantidad": cantidad,
        "total": total
    }

    ventas.append(nueva_venta)
    guardar_json(ARCHIVO_VENTAS, ventas)

    print(f"✅ Venta registrada. Total a pagar: ${total}")

def listar_ventas():
    """
    Muestra todas las ventas registradas con:
    - Nombre del cliente
    - Nombre del empleado
    - Nombre del producto
    - Cantidad y total
    """
    clientes = leer_json("data/clientes.json")
    empleados = leer_json("data/empleados.json")
    productos = leer_json("data/productos.json")
    ventas = leer_json(ARCHIVO_VENTAS)

    if not ventas:
        print("⚠️ No hay ventas registradas")
        return

    print("\n--- LISTA DE VENTAS ---")
    for v in ventas:
        cliente = next((c["nombre"] for c in clientes if c["id"] == v["cliente_id"]), "Desconocido")
        empleado = next((e["nombre"] for e in empleados if e["id"] == v["empleado_id"]), "Desconocido")
        producto = next((p["nombre"] for p in productos if p["id"] == v["producto_id"]), "Desconocido")
        print(f"Venta ID: {v['id']}")
        print(f" Cliente: {cliente}")
        print(f" Empleado: {empleado}")
        print(f" Producto: {producto}")
        print(f" Cantidad: {v['cantidad']}")
        print(f" Total: ${v['total']}")
        print("----------------------------")
    print()
