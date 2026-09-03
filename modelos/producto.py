class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["precio"],
            datos["stock"]
        )