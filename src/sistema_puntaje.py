import graphics.gamelib as gamelib
import sqlite3 as sql

NOMBRE_TABLA = "Puntajes"


class SistemaPuntaje:

    def __init__(self) -> None:
        self._sql_connect = sql.connect("Puntaje.db")
        self._my_cursor = self._sql_connect.cursor()
        self._my_cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {NOMBRE_TABLA} (Id INTEGER PRIMARY KEY AUTOINCREMENT, Jugador VARCHAR(10), Puntos INTEGER)"
        )

    def guardar_puntaje(self: object, puntaje: int) -> None:
        """..."""

        nombre_jugador = gamelib.input("Ingrese su nombre")

        self._my_cursor.execute(
            f"INSERT INTO {NOMBRE_TABLA} (Jugador, Puntos) VALUES(?, ?)",
            (nombre_jugador, puntaje),
        )
        self._sql_connect.commit()

    def obtener_puntajes_mas_altos(self: object) -> list:
        """..."""

        self._my_cursor.execute(
            f"SELECT Jugador, Puntos FROM {NOMBRE_TABLA} ORDER BY Puntos DESC LIMIT 10"
        )

        return self._my_cursor.fetchall()
