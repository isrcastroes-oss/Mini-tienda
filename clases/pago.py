# -*- coding: utf-8 -*-
"""
Clase Pago
Permite registrar pagos de ventas, si quieres separar pagos de la venta.
Cada pago se guarda en data/pagos.json
y se le asigna un ID automático desde pagos_contador.txt
"""

from utils.archivos import leer_json, guardar_json, obtener_id
from utils.validaciones import validar_entero, validar_booleano
from clases.venta import listar_ventas

ARCHIVO_PAGOS = "data/pagos.json"
CONTADOR_PAGOS = "data/pagos_contador.txt"

def registrar_pago():
    """
    Registra un pago de una venta existente:
    - Selecciona ID de venta
    - Ingresa si se pagó completo o parcial
    """
    pagos = leer_json(ARCHIVO_PAGOS)
    ventas = leer_json("data/ventas.json")

    if not ventas:
        print("⚠️ No hay ventas registradas para pagar")
        return

    print("\n--- VENTAS DISPONIBLES ---")
    listar_ventas()
    id_venta = validar_entero("Ingrese ID de la venta a pagar: ")

    venta = next((v for v in ventas if v["id"] == id_venta), None)
    if not venta:
        print("❌ Venta no encontrada")
        return

    pagado_completo = validar_booleano("¿Se pagó completo? (sí/no): ")

    monto = venta["total"] if pagado_completo else validar_entero("Ingrese monto a pagar: ")

    nuevo_pago = {
        "id": obtener_id(CONTADOR_PAGOS),
        "venta_id": id_venta,
        "monto": monto,
        "pagado_completo": pagado_completo
    }

    pagos.append(nuevo_pago)
    guardar_json(ARCHIVO_PAGOS, pagos)

    print(f"✅ Pago registrado. Monto: ${monto}")

def listar_pagos():
    """
    Muestra todos los pagos registrados
    """
    pagos = leer_json(ARCHIVO_PAGOS)
    ventas = leer_json("data/ventas.json")

    if not pagos:
        print("⚠️ No hay pagos registrados")
        return

    print("\n--- LISTA DE PAGOS ---")
    for p in pagos:
        venta = next((v for v in ventas if v["id"] == p["venta_id"]), None)
        print(f"Pago ID: {p['id']}")
        print(f" Venta ID: {p['venta_id']}")
        print(f" Monto: ${p['monto']}")
        print(f" Pagado completo: {'Sí' if p['pagado_completo'] else 'No'}")
        if venta:
            print(f" Total venta: ${venta['total']}")
        print("----------------------------")
    print()
