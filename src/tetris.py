from src.tablero import Tablero
from src.generador_piezas import GeneradorPieza
import csv

FILAS_TABLERO = 18
COLUMNAS_TABLERO = 9
FILAS_TABLERO_P_SIGUIENTE = FILAS_TABLERO // 2
COLUMNAS_TABLERO_P_SIGUIENTE = COLUMNAS_TABLERO // 2

PIEZA = "@"
IZQUIERDA, DERECHA = -1, 1


class Tetris:

    def __init__(self: object) -> None:
        """..."""

        self.tablero = Tablero(FILAS_TABLERO, COLUMNAS_TABLERO)
        self.tablero_p_siguiente = Tablero(
            FILAS_TABLERO_P_SIGUIENTE, COLUMNAS_TABLERO_P_SIGUIENTE
        )
        self.generador_pieza = GeneradorPieza()
        self.pieza_actual = self.generador_pieza.generar_pieza()
        self.pieza_siguiente = self.generador_pieza.generar_pieza()
        self.puntos = 0

    def get_tablero(self: object) -> list:
        """..."""

        return self.tablero.get_tablero()

    def get_tablero_p_siguiente(self: object) -> list:
        """..."""

        return self.tablero_p_siguiente.get_tablero()

    def avanzar_estado_juego(self: object) -> None:
        """..."""

        self.tablero.actualizar(
            elemento=PIEZA, coordenadas_elemento=self.pieza_actual.get_coordenadas()
        )

        coordenadas_deseadas = self.pieza_actual.trasladarse()
        if self.tablero.son_coordenadas_validas(coordenadas_deseadas):
            self.pieza_actual.actualizar(coordenadas_deseadas)

        else:
            self.tablero.actualizar(
                elemento=PIEZA,
                coordenadas_elemento=self.pieza_actual.get_coordenadas(),
                eliminar_elemento=True,
                eliminar_filas=True,
            )
            self._intercambiar_pieza_actual_por_siguiente()
            self.puntos += 1

        self.tablero_p_siguiente.actualizar(
            elemento=PIEZA,
            coordenadas_elemento=self.pieza_siguiente.get_coordenadas(),
        )

    def _intercambiar_pieza_actual_por_siguiente(self: object) -> None:
        """..."""

        pieza_trasladada = self.pieza_siguiente.trasladarse(COLUMNAS_TABLERO // 2, 0)

        if self.tablero.son_coordenadas_validas(pieza_trasladada):
            self.pieza_siguiente.actualizar(pieza_trasladada)
            self.pieza_actual = self.pieza_siguiente
            self.pieza_siguiente = self.generador_pieza.generar_pieza()

        else:
            self.pieza_actual = None

    def terminar_juego(self: object):
        """..."""

        return self.pieza_actual == None

    # ACCIONES JUGADOR
    def mover(self: object, direccion):
        """..."""

        coordenadas_deseadas = self.pieza_actual.trasladarse(direccion, 0)
        if self.tablero.son_coordenadas_validas(coordenadas_deseadas):
            self.pieza_actual.actualizar(coordenadas_deseadas)

    def descender_rapido(self: object):
        """..."""

        self.pieza_actual.descender_rapido(self.tablero)

    def rotar_pieza(self: object):
        """..."""

        self.pieza_actual.rotar(self.tablero)

    # PUNTAJE
    def cargar_tabla_puntuaciones(self: object):
        """..."""

        with open("puntaje.csv") as archivo:
            tabla_puntuaciones = [
                jugador for jugador in list(csv.reader(archivo)) if jugador
            ]
            tabla_puntuaciones = sorted(
                tabla_puntuaciones, key=lambda jugador: int(jugador[1]), reverse=True
            )

        return tabla_puntuaciones[:10]

    def guardar_puntaje(self: object, nombre_jugador):
        """..."""

        with open("puntaje.csv", "a") as archivo:
            archivo_csv = csv.writer(archivo)
            archivo_csv.writerow((nombre_jugador, self.puntos))
