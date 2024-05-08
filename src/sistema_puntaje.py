import graphics.gamelib as gamelib
import sqlite3 as sql

NOMBRE_TABLA = "Puntajes"


class SistemaPuntaje:
    """
    Clase cuya instancia se encarga de controlar la logica del Sistema de Puntuación
    y preservar los puntajes.
    """

    def __init__(self: object) -> None:
        """
        Parámetros:
            No recibe parámetros.

        Inicializa una instancia de SistemaPuntaje iniciando los puntos en 0,
        creando una conección a una Base de Datos y creando,
        en caso de que no exista, la tabla donde se almacenan los puntajes.

        Return:
            None
        """

        self._sql_connect = sql.connect("Puntaje.db")
        self._my_cursor = self._sql_connect.cursor()
        self._my_cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {NOMBRE_TABLA} (Id INTEGER PRIMARY KEY AUTOINCREMENT, Jugador VARCHAR(10), Puntos INTEGER)"
        )
        self._puntos = 0

    def obtener_puntos(self: object) -> int:
        """
        Parámetros:
            No recibe parámetros.

        Devuelve los puntos actuales.

        Return:
            - puntos: int
        """

        return self._puntos

    def actualizar_puntaje(self: object, filas_eliminadas: int) -> None:
        """
        Parámetros:
            - filas_eliminadas: int

        Actualiza el puntaje actual sumandole 1 y multiplicandolo por
        filas eliminadas, en caso de que las haya.

        Return:
            None
        """

        self._puntos += 1
        if filas_eliminadas:
            self._puntos *= filas_eliminadas

    def guardar_puntaje(self: object) -> None:
        """
        Parámetros:
            No recibe parámetros.

        Guarda el puntaje de nombre_jugador en la Base de Datos.

        Return:
            None
        """

        nombre_jugador = self._pedir_nombre_jugador()

        self._my_cursor.execute(
            f"INSERT INTO {NOMBRE_TABLA} (Jugador, Puntos) VALUES(?, ?)",
            (nombre_jugador, self._puntos),
        )
        self._sql_connect.commit()

    def obtener_puntajes_mas_altos(self: object) -> list:
        """
        Parámetros:
            No recibe parámetros.

        Selecciona los 10 puntajes más altos y los devuelve.

        Return:
            - puntajes_mas_altos: list
        """

        self._my_cursor.execute(
            f"SELECT Jugador, Puntos FROM {NOMBRE_TABLA} ORDER BY Puntos DESC LIMIT 10"
        )

        return self._my_cursor.fetchall()

    def _pedir_nombre_jugador(self: object) -> str:
        """
        Parámetros:
            No recibe parámetros.

        Pide al jugador que ingrese su nombre (máximo 5 caracteres),
        es necesario que ingrese un nombre para continuar. Luego lo devuelve.

        Return:
            - nombre_jugador: str
        """

        nombre_jugador = None
        while not nombre_jugador or len(nombre_jugador) > 5:
            nombre_jugador = gamelib.input("Ingrese su nombre (Max. 5)")

        return nombre_jugador
