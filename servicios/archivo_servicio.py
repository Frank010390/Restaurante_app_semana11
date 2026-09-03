import json
import os

class ArchivoServicio:
    def __init__(self, carpeta_datos="datos"):
        self.carpeta = carpeta_datos
        os.makedirs(carpeta_datos, exist_ok=True)

    def guardar_json(self, nombre_archivo, lista_objetos):
        ruta = os.path.join(self.carpeta, nombre_archivo)
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump([obj.a_diccionario() for obj in lista_objetos], archivo, ensure_ascii=False, indent=2)

    def cargar_json(self, nombre_archivo, clase):
        ruta = os.path.join(self.carpeta, nombre_archivo)
        if not os.path.exists(ruta):
            return []
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [clase.desde_diccionario(item) for item in datos]