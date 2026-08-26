class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int):
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad
        if cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser mayor a cero")

    def convertir_a_diccionario(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    @classmethod
    def reconstruir_desde_diccionario(cls, datos: dict):
        return cls(
            usuario_id=datos["usuario_id"],
            producto_codigo=datos["producto_codigo"],
            cantidad=datos["cantidad"]
        )