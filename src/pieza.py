from src.tablero import Tablero

COORDENADA_X = 0
COORDENADA_Y = 1


class Pieza:
    """
    Clase cuya instancia se encarga de mantener las características de las piezas y
    ejecutar sus acciones.
    """

    def __init__(
        self: object, coordenadas: tuple, rotaciones: tuple, rotacion: int = 0
    ) -> None:
        """
        Parámetros:
            - coordenadas: tuple
            - rotaciones: tuple
            - rotacion: int

        Inicializa una instancia de Pieza, con sus respectivas coordenadas, rotaciones disponibles
        y su rotación actual, por defecto la rotación actual es 0.

        Return:
            None
        """

        self._coordenadas = coordenadas
        self._rotacion_actual = rotacion
        self._rotaciones = rotaciones

    def obtener_coordenadas(self: object) -> tuple:
        """
        Parámetros:
            No recibe parámetros.

        Devuelve las coordenadas del objecto Pieza.

        Return:
            - coordenadas: tuple
        """

        return self._coordenadas

    def actualizar(self: object, nuevas_coordenadas: tuple) -> None:
        """
        Parámetros:
            - nuevas_coordenadas: tuple

        Actaliza las coordenadas del objeto Pieza, cambiandolas por nuevas_coordenadas.

        Return:
            None
        """

        self._coordenadas = nuevas_coordenadas

    def trasladarse(
        self: object, desplazamiento_x: int = 0, desplazamiento_y: int = 1
    ) -> tuple:
        """
        Parámetros:
            - desplazamiento_x: int
            - desplazamiento_y: int

        Traslada las coordenadas del objeto Pieza utilizando los desplazamientos recibidos por parámetro
        y devuelve las coordenadas trasladadas, por defecto los desplazamientos son:
        desplazamiento_x = 0   desplazamiento_y = 1

        Return:
            - coordenadas_trasladadas: tuple
        """

        return tuple(
            (coordenada_x + desplazamiento_x, coordenada_y + desplazamiento_y)
            for coordenada_x, coordenada_y in self._coordenadas
        )

    def descender_rapido(self: object, tablero: Tablero) -> None:
        """
        Parámetros:
            - tablero: Tablero

        Desciende las coordenadas del objeto Pieza hasta que el tablero diga
        que no se puede descender más.

        Return:
            None
        """

        nueva_coordenada = self.trasladarse()

        while tablero.son_coordenadas_validas(nueva_coordenada):
            self.actualizar(nueva_coordenada)
            nueva_coordenada = self.trasladarse()

    def rotar(self: object, tablero: Tablero) -> None:
        """
        Parámetros:
            - tablero: Tablero

        Busca la siguiente rotación de la pieza en self._rotaciones y
        en caso de poder colocarse en el tablero, actualiza self._rotacion_actual,
        en caso contrario, se mantiene igual.

        Return:
            None
        """

        self._rotacion_actual = (
            self._rotacion_actual + 1
            if self._rotacion_actual + 1 < len(self._rotaciones)
            else 0
        )

        aux = self._coordenadas
        coordenada_1 = self._coordenadas[0]
        self._coordenadas = self._rotaciones[self._rotacion_actual]
        pieza_trasladada = self.trasladarse(
            coordenada_1[COORDENADA_X], coordenada_1[COORDENADA_Y]
        )

        self._coordenadas = (
            pieza_trasladada
            if tablero.son_coordenadas_validas(pieza_trasladada)
            else aux
        )
