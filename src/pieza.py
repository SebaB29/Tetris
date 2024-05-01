from src.tablero import Tablero

COORDENADA_X = 0
COORDENADA_Y = 1


class Pieza:

    def __init__(
        self: object, coordenadas: tuple, rotaciones: tuple, rotacion: int = 0
    ) -> None:
        """..."""

        self.coordenadas = coordenadas
        self.rotacion_actual = rotacion
        self.rotaciones = rotaciones

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

    def descender_rapido(self: object, tablero: Tablero) -> None:
        """..."""

        nueva_coordenada = self.trasladarse()

        while tablero.son_coordenadas_validas(nueva_coordenada):
            self.actualizar(nueva_coordenada)
            nueva_coordenada = self.trasladarse()

    def rotar(self: object, tablero: Tablero) -> None:
        """..."""

        self.rotacion_actual = (
            self.rotacion_actual + 1
            if self.rotacion_actual + 1 < len(self.rotaciones)
            else 0
        )

        aux = self.coordenadas
        coordenada_1 = self.coordenadas[0]
        self.coordenadas = self.rotaciones[self.rotacion_actual]
        pieza_trasladada = self.trasladarse(
            coordenada_1[COORDENADA_X], coordenada_1[COORDENADA_Y]
        )

        self.coordenadas = (
            pieza_trasladada
            if tablero.son_coordenadas_validas(pieza_trasladada)
            else aux
        )
