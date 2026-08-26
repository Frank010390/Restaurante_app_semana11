from typing import List, Optional, Tuple
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import (
    cargar_productos, guardar_productos,
    cargar_usuarios, guardar_usuarios,
    cargar_ventas, guardar_ventas
)


class Restaurante:
    def __init__(self):
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
        self._ventas: List[Venta] = []

    def iniciar(self) -> None:
        self._productos = cargar_productos()
        self._usuarios = cargar_usuarios()
        self._ventas = cargar_ventas()

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo):
            return False
        self._productos.append(producto)
        return guardar_productos(self._productos)

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        return next((p for p in self._productos if p.codigo == codigo), None)

    def listar_productos(self) -> List[Producto]:
        return list(self._productos)

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion):
            return False
        self._usuarios.append(usuario)
        return guardar_usuarios(self._usuarios)

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        return next((u for u in self._usuarios if u.identificacion == identificacion), None)

    def vender_producto(self, codigo_producto: str, id_usuario: str, cantidad: int) -> Tuple[bool, str]:
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            return False, "Usuario no registrado"
        producto = self.buscar_producto(codigo_producto)
        if not producto:
            return False, "Producto no encontrado"
        if cantidad <= 0:
            return False, "La cantidad debe ser mayor a cero"
        if producto.stock < cantidad:
            return False, f"Stock insuficiente. Disponible: {producto.stock}"

        venta = Venta(id_usuario, codigo_producto, cantidad)
        self._ventas.append(venta)
        producto.vender(cantidad)
        guardar_ventas(self._ventas)
        guardar_productos(self._productos)
        return True, "✅ Venta registrada correctamente"

    def consultar_ventas_por_usuario(self, id_usuario: str):
        return [
            (venta, self.buscar_producto(venta.producto_codigo))
            for venta in self._ventas if venta.usuario_id == id_usuario
        ]