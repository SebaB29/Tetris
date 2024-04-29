class Pieza:

    def __init__(self: object, coordenadas: tuple) -> None:
        """..."""

        self.coordenadas = coordenadas

    def get_coordenadas(self: object) -> tuple:
        """..."""

        return self.coordenadas

    def actualizar(self: object, nuevas_coordenadas: tuple) -> None:
        """..."""

        self.coordenadas = nuevas_coordenadas

    def trasladarse(
        self: object, desplazamiento_x: int = 0, desplazamiento_y: int = 1
    ) -> tuple:
        """..."""

        return tuple(
            (coordenada_x + desplazamiento_x, coordenada_y + desplazamiento_y)
            for coordenada_x, coordenada_y in self.coordenadas
        )
