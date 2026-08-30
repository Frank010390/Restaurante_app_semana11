class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int):
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

    def a_diccionario(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    def __str__(self) -> str:
        return f"Usuario: {self.usuario_id} | Producto: {self.producto_codigo} | Cantidad: {self.cantidad}"