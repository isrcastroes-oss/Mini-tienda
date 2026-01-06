# -*- coding: utf-8 -*-
"""
Modulo archivos
Se encarga de la lectura y escritura de archivos JSON
y del manejo de contadores independientes para cada objeto
"""

import json
import os


def leer_json(ruta):
    """
    Lee un archivo JSON y devuelve su contenido
    como una lista de diccionarios
    """
    if not os.path.exists(ruta):
        return []

    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_json(ruta, datos):
    """
    Guarda una lista de diccionarios en un archivo JSON
    """
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def obtener_id(ruta_contador):
    """
    Obtiene un ID autoincremental desde un archivo contador
    """
    with open(ruta_contador, "r+") as archivo:
        contador = int(archivo.read())
        contador += 1
        archivo.seek(0)
        archivo.write(str(contador))
        archivo.truncate()
        return contador
