# -*- coding: utf-8 -*-
"""
Módulo validaciones
Funciones para validar la entrada del usuario
"""

def validar_entero(mensaje):
    """
    Solicita al usuario un número entero
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Ingrese un número entero válido")

def validar_float(mensaje):
    """
    Solicita al usuario un número decimal
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Ingrese un número válido")

def validar_texto(mensaje):
    """
    Solicita al usuario un texto no vacío
    """
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("❌ El texto no puede estar vacío")

def validar_booleano(mensaje):
    """
    Solicita al usuario un valor sí/no (s/n)
    Devuelve True si es 's', False si es 'n'
    """
    while True:
        valor = input(mensaje + " (s/n): ").lower()
        if valor in ["s", "n"]:
            return valor == "s"
        print("❌ Ingrese 's' o 'n'")
