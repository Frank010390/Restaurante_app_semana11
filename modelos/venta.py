class Venta:
    def __init__(self, id_venta, identificacion_usuario, codigo_producto, cantidad, fecha=None):
        self.id_venta = id_venta
        self.identificacion_usuario = identificacion_usuario
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.fecha = fecha

    def a_diccionario(self):
        return {
            "id_venta": self.id_venta,
            "identificacion_usuario": self.identificacion_usuario,
            "codigo_producto": self.codigo_producto,
            "cantidad": self.cantidad,
            "fecha": self.fecha
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["id_venta"],
            datos["identificacion_usuario"],
            datos["codigo_producto"],
            datos["cantidad"],
            datos.get("fecha")
        )