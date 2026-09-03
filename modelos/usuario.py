class Usuario:
    def __init__(self, identificacion, nombre, correo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def a_diccionario(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["identificacion"],
            datos["nombre"],
            datos["correo"]
        )