POSICION_LIBRE = ""


class Tablero:

    def __init__(self: object, filas: int, columnas: int) -> None:
        self.tablero = [
            [POSICION_LIBRE for columna in range(columnas)] for fila in range(filas)
        ]

    def actualizar(
        self: object,
        elemento: str,
        coordenadas_elemento: tuple,
        nuevo_elemento: str = None,
        eliminar_filas: bool = False,
    ) -> None:

        self._borrar_elemento(elemento)
        if nuevo_elemento:
            self._colocar_elemento(coordenadas_elemento, nuevo_elemento)
        else:
            self._colocar_elemento(coordenadas_elemento, elemento)

        if eliminar_filas:
            self._eliminar_filas()

    def get_tablero(self) -> list:
        return self.tablero

    def son_coordenadas_validas(self: object, pieza: tuple) -> bool:
        """..."""

        for coordenada in pieza:
            if not self._coordenada_es_valida(coordenada):
                return False

        return True

    def _coordenada_es_valida(self: object, coordenada: tuple) -> bool:
        """..."""

        return (
            (0 <= coordenada[0] < len(self.tablero[0]))
            and (0 <= coordenada[1] < len(self.tablero))
            and self.tablero[coordenada[1]][coordenada[0]] != "#"  # MODIFICAR
        )

    def _colocar_elemento(
        self: object, coordenadas_elemento: tuple, elemento: str
    ) -> None:
        """..."""

        for coordenada_x, coordenada_y in coordenadas_elemento:
            self.tablero[coordenada_y][coordenada_x] = elemento

    def _borrar_elemento(self: object, elemento: str) -> None:
        """..."""

        for fila in range(len(self.tablero)):
            for columna in range(len(self.tablero[fila])):
                if self.tablero[fila][columna] == elemento:
                    self.tablero[fila][columna] = POSICION_LIBRE

    def _eliminar_filas(self: object):
        """..."""

        nuevo_tablero = []

        for fila in self.tablero:
            if not POSICION_LIBRE in fila:
                nuevo_tablero.insert(
                    0, [POSICION_LIBRE for columna in range(len(fila))]
                )
            else:
                nuevo_tablero.append(fila)

        self.tablero = nuevo_tablero
