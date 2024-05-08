import graphics.gamelib as gamelib
import sqlite3 as sql

NOMBRE_TABLA = "Puntajes"


class SistemaPuntaje:

    def __init__(self: object) -> None:
        """..."""

        self._sql_connect = sql.connect("Puntaje.db")
        self._my_cursor = self._sql_connect.cursor()
        self._my_cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {NOMBRE_TABLA} (Id INTEGER PRIMARY KEY AUTOINCREMENT, Jugador VARCHAR(10), Puntos INTEGER)"
        )
        self._puntos = 0

    def actualizar_puntaje(self: object, filas_eliminadas: int) -> None:
        """..."""

        self._puntos += 1
        if filas_eliminadas:
            self._puntos *= filas_eliminadas

    def _pedir_nombre_jugador(self: object) -> str:
        """..."""

        nombre_jugador = None
        while not nombre_jugador or len(nombre_jugador) > 5:
            nombre_jugador = gamelib.input("Ingrese su nombre (Max. 5)")

        return nombre_jugador

    def guardar_puntaje(self: object) -> None:
        """..."""

        nombre_jugador = self._pedir_nombre_jugador()

        self._my_cursor.execute(
            f"INSERT INTO {NOMBRE_TABLA} (Jugador, Puntos) VALUES(?, ?)",
            (nombre_jugador, self._puntos),
        )
        self._sql_connect.commit()

    def obtener_puntajes_mas_altos(self: object) -> list:
        """..."""

        self._my_cursor.execute(
            f"SELECT Jugador, Puntos FROM {NOMBRE_TABLA} ORDER BY Puntos DESC LIMIT 10"
        )

        return self._my_cursor.fetchall()
