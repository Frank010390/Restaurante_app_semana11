import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import json
from typing import List

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

RUTA_PRODUCTOS = Path("datos/productos.json")
RUTA_USUARIOS = Path("datos/usuarios.json")
RUTA_VENTAS = Path("datos/ventas.json")


def _leer_archivo(ruta):
    if not ruta.exists():
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
            if not contenido:
                return []
            return json.loads(contenido)
    except:
        return []


def _escribir_archivo(ruta, objetos):
    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        diccionarios = [obj.convertir_a_diccionario() for obj in objetos]
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(diccionarios, archivo, indent=2, ensure_ascii=False)
        return True
    except:
        return False


def cargar_productos():
    datos = _leer_archivo(RUTA_PRODUCTOS)
    return [Producto.reconstruir_desde_diccionario(item) for item in datos]

def guardar_productos(productos):
    return _escribir_archivo(RUTA_PRODUCTOS, productos)

def cargar_usuarios():
    datos = _leer_archivo(RUTA_USUARIOS)
    return [Usuario.reconstruir_desde_diccionario(item) for item in datos]

def guardar_usuarios(usuarios):
    return _escribir_archivo(RUTA_USUARIOS, usuarios)

def cargar_ventas():
    datos = _leer_archivo(RUTA_VENTAS)
    return [Venta.reconstruir_desde_diccionario(item) for item in datos]

def guardar_ventas(ventas):
    return _escribir_archivo(RUTA_VENTAS, ventas)