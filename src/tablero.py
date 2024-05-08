from src.constantes import POSICION_LIBRE, SUPERFICIE


class Tablero:
    """
    Clase cuya instancia se encarga de mantener el estado del tablero.
    """

    def __init__(self: object, filas: int, columnas: int) -> None:
        """
        Parámetros:
            - filas: int
            - columnas: int

        Inicializa una instancia de Tablero, iniciando self._tablero
        de alto (filas) y ancho (columnas) donde todas sus posiciones tiene POSICION_LIBRE.

        Return:
            None
        """

        self._tablero = [
            [POSICION_LIBRE for i in range(columnas)] for j in range(filas)
        ]

    def actualizar(
        self: object,
        elemento: str,
        coordenadas_elemento: tuple,
        eliminar_elemento: bool = False,
        eliminar_filas: bool = False,
    ) -> int:
        """
        Parámetros:
            - elemento: str
            - coordenadas_elemento: tuple
            - eliminar_elemento: bool
            - eliminar_filas: bool

        Actualiza el estado del talero, actualizando la posición del elemento recibido,
        eliminandolo en caso de que el parámetro eliminar_elemento sea True (por defecto es False) y
        eliminando filas en caso de que el parámetro eliminar_filas sea True (por defecto es False).
        Luego devuelve la cantidad de filas eliminadas.

        Return:
            - filas_eliminadas: int
        """

        # Borra el elemento reemplazandolo por POSICION_LIBRE
        self._borrar_elemento(elemento)

        if eliminar_elemento:
            # Eliminia el elemento reemplazandolo por SUPERFICIE
            self._colocar_elemento(SUPERFICIE["SIMBOLO"], coordenadas_elemento)
        else:
            self._colocar_elemento(elemento, coordenadas_elemento)

        filas_eliminadas = 0
        if eliminar_filas:
            filas_eliminadas = self._eliminar_filas()

        return filas_eliminadas

    def obtener_coordenadas_elemento(self: object, elemento: str) -> tuple:
        """
        Parámetros:
            - elemento: str

        Devuelve las coordenadas del elemento recibido.

        Return:
            - coordenadas_elemento: tuple
        """

        return (
            (columna, fila)
            for fila in range(len(self._tablero))
            for columna in range(len(self._tablero[0]))
            if self._tablero[fila][columna] == elemento
        )

    def son_coordenadas_validas(self: object, coordenadas: tuple) -> bool:
        """
        Parámetros:
            - coordenadas: tuple

        Comprueba que el conjunto de coordenadas se encuentren en posición valida
        y devuelve True si todas están en posición valida, False en caso contrario.

        Return:
            bool
        """

        for coordenada in coordenadas:
            if not self._coordenada_es_valida(coordenada):
                return False

        return True

    def _coordenada_es_valida(self: object, coordenada: tuple) -> bool:
        """
        Parámetros:
            - coordenada: tuple

        Devuelve True en caso de que la coordenada se encuentre en una posición
        valida y False en caso contrario. Para estar en condición valida tiene que
        estar en los rangos del tablero y no haber SUPERFICIE en esa coordenada.

        Return:
            bool
        """

        return (
            (0 <= coordenada[0] < len(self._tablero[0]))
            and (0 <= coordenada[1] < len(self._tablero))
            and self._tablero[coordenada[1]][coordenada[0]] != SUPERFICIE["SIMBOLO"]
        )

    def _colocar_elemento(
        self: object, elemento: str, coordenadas_elemento: tuple
    ) -> None:
        """
        Parámetros:
            - elemento: str
            - coordenadas_elemento: tuple

        Coloca el elemento recibido por parámetro en el tablero
        ubicandolo de las coordenadas recibidas.

        Return:
            None
        """

        for coordenada_x, coordenada_y in coordenadas_elemento:
            self._tablero[coordenada_y][coordenada_x] = elemento

    def _borrar_elemento(self: object, elemento: str) -> None:
        """
        Parámetros:
            - elemento: str

        Elimina del tablero el elemento recibido por parámetro.

        Return:
            None
        """

        for fila in range(len(self._tablero)):
            for columna in range(len(self._tablero[fila])):
                if self._tablero[fila][columna] == elemento:
                    self._tablero[fila][columna] = POSICION_LIBRE

    def _eliminar_filas(self: object) -> int:
        """
        Parámetros:
            No recibe parámetros.

        Crea un nuevo tablero manteniendo el estado del anterior,
        pero eliminando las filas que no tengan POSICION_LIBRE.
        Devuelve la cantidad de filas eliminadas.

        Return:
            - filas_eliminadas: int
        """

        nuevo_tablero = []
        filas_eliminadas = 0

        for fila in self._tablero:
            if not POSICION_LIBRE in fila:
                nuevo_tablero.insert(0, [POSICION_LIBRE for i in range(len(fila))])
                filas_eliminadas += 1
            else:
                nuevo_tablero.append(fila)

        self._tablero = nuevo_tablero
        return filas_eliminadas
