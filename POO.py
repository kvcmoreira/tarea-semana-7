class Vector:
    def __init__(self, a, b, c):
        """Constructor que inicializa las componentes del vector."""
        self.a = a
        self.b = b
        self.c = c
        print(f"Vector ({self.a}, {self.b}, {self.c}) creado.")

    def __del__(self):
        """Destructor que imprime un mensaje cuando el objeto es eliminado."""
        print(f"Vector ({self.a}, {self.b}, {self.c}) eliminado.")

    def magnitud(self):
        """Método para calcular la magnitud del vector."""
        return (self.a ** 2 + self.b ** 2 + self.c ** 2) ** 0.5


# Crear y eliminar un objeto de la clase Vector
vector = Vector(1, 2, 3)
print(f"Magnitud del vector: {vector.magnitud():.2f}")
del vector
