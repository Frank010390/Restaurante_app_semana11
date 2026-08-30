import json
import os
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    def __init__(self, carpeta_datos: str = "datos"):
        self.carpeta_datos = carpeta_datos
        if not os.path.exists(self.carpeta_datos):
            os.makedirs(self.carpeta_datos)

    # ─────────────── PRODUCTOS ───────────────
    def guardar_productos(self, productos: list) -> bool:
        ruta = os.path.join(self.carpeta_datos, "productos.json")
        try:
            datos = [p.a_diccionario() for p in productos]
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print("❌ Sin permisos para escribir productos.json")
            return False
        except Exception as e:
            print(f"❌ Error al guardar productos: {e}")
            return False

    def cargar_productos(self) -> list:
        ruta = os.path.join(self.carpeta_datos, "productos.json")
        productos = []
        if not os.path.exists(ruta):
            print("ℹ️ Sin archivo productos.json → iniciando vacío")
            return productos
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                try:
                    datos = json.load(f)
                except json.JSONDecodeError:
                    print("⚠️ productos.json corrupto → iniciando vacío")
                    return productos
            for item in datos:
                try:
                    p = Producto(
                        id_producto=item["id_producto"],
                        nombre=item["nombre"],
                        precio=item["precio"],
                        categoria=item["categoria"],
                        stock=item.get("stock", 0),
                        disponible=item.get("disponible", True)
                    )
                    productos.append(p)
                except KeyError as falta:
                    print(f"⚠️ Producto sin campo {falta} → omitido")
                except ValueError as e:
                    print(f"⚠️ Datos inválidos en producto: {e} → omitido")
        except FileNotFoundError:
            print("ℹ️ Sin archivo productos.json")
        except PermissionError:
            print("❌ Sin permisos para leer productos.json")
        return productos

    # ─────────────── USUARIOS ───────────────
    def guardar_usuarios(self, usuarios: list) -> bool:
        ruta = os.path.join(self.carpeta_datos, "usuarios.json")
        try:
            datos = [u.a_diccionario() for u in usuarios]
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print("❌ Sin permisos para escribir usuarios.json")
            return False
        except Exception as e:
            print(f"❌ Error al guardar usuarios: {e}")
            return False

    def cargar_usuarios(self) -> list:
        ruta = os.path.join(self.carpeta_datos, "usuarios.json")
        usuarios = []
        if not os.path.exists(ruta):
            print("ℹ️ Sin archivo usuarios.json → iniciando vacío")
            return usuarios
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                try:
                    datos = json.load(f)
                except json.JSONDecodeError:
                    print("⚠️ usuarios.json corrupto → iniciando vacío")
                    return usuarios
            for item in datos:
                try:
                    u = Usuario(
                        identificacion=item["identificacion"],
                        nombre=item["nombre"],
                        correo=item["correo"]
                    )
                    usuarios.append(u)
                except KeyError as falta:
                    print(f"⚠️ Usuario sin campo {falta} → omitido")
            return usuarios
        except FileNotFoundError:
            print("ℹ️ Sin archivo usuarios.json")
        except PermissionError:
            print("❌ Sin permisos para leer usuarios.json")
        return usuarios

    # ─────────────── VENTAS ───────────────
    def guardar_ventas(self, ventas: list) -> bool:
        ruta = os.path.join(self.carpeta_datos, "ventas.json")
        try:
            datos = [v.a_diccionario() for v in ventas]
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print("❌ Sin permisos para escribir ventas.json")
            return False
        except Exception as e:
            print(f"❌ Error al guardar ventas: {e}")
            return False

    def cargar_ventas(self) -> list:
        ruta = os.path.join(self.carpeta_datos, "ventas.json")
        ventas = []
        if not os.path.exists(ruta):
            print("ℹ️ Sin archivo ventas.json → iniciando vacío")
            return ventas
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                try:
                    datos = json.load(f)
                except json.JSONDecodeError:
                    print("⚠️ ventas.json corrupto → iniciando vacío")
                    return ventas
            for item in datos:
                try:
                    v = Venta(
                        usuario_id=item["usuario_id"],
                        producto_codigo=item["producto_codigo"],
                        cantidad=item["cantidad"]
                    )
                    ventas.append(v)
                except KeyError as falta:
                    print(f"⚠️ Venta sin campo {falta} → omitida")
            return ventas
        except FileNotFoundError:
            print("ℹ️ Sin archivo ventas.json")
        except PermissionError:
            print("❌ Sin permisos para leer ventas.json")
        return ventas