from random import choice
from src.tablero import Tablero
from src.generador_piezas import GeneradorPieza
from src.pieza import Pieza
import csv

FILAS_TABLERO = 18
COLUMNAS_TABLERO = 9
FILAS_TABLERO_P_SIGUIENTE = FILAS_TABLERO // 2
COLUMNAS_TABLERO_P_SIGUIENTE = COLUMNAS_TABLERO // 2

PIEZA = "@"
SUPERFICIE = "#"
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

    def avanzar_estado_juego(self: object):
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
                nuevo_elemento=SUPERFICIE,
                eliminar_filas=True,
            )

            self.puntos += 1
            self._intercambiar_pieza_actual_por_siguiente()

        self.tablero_p_siguiente.actualizar(
            elemento=PIEZA,
            coordenadas_elemento=self.pieza_siguiente.get_coordenadas(),
        )

    def _intercambiar_pieza_actual_por_siguiente(self: object):
        """..."""

        pieza_trasladada = self.pieza_siguiente.trasladarse(COLUMNAS_TABLERO // 2, 0)

        if self.tablero.son_coordenadas_validas(pieza_trasladada):
            self.pieza_actual = self.generador_pieza.generar_pieza(pieza_trasladada)
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

        pieza = self.pieza_actual.trasladarse()

        while self.tablero.son_coordenadas_validas(pieza):
            self.pieza_actual.actualizar(pieza)
            pieza = self.pieza_actual.trasladarse()

        self.tablero.actualizar(
            elemento=PIEZA, coordenadas_elemento=self.pieza_actual.get_coordenadas()
        )

    def rotar_pieza(self: object):
        """..."""

        coordenada_1 = self.pieza_actual.get_coordenadas()[0]
        pieza_en_origen = self.pieza_actual.trasladarse(
            -coordenada_1[0], -coordenada_1[1]
        )

        pieza_rotada = self.buscar_rotacion(pieza_en_origen)

        nueva_pieza = Pieza(pieza_rotada)
        pieza_trasladada = nueva_pieza.trasladarse(coordenada_1[0], coordenada_1[1])

        if self.tablero.son_coordenadas_validas(pieza_trasladada):
            self.pieza_actual = nueva_pieza
            self.pieza_actual.actualizar(pieza_trasladada)

    def buscar_rotacion(self: object, pieza_en_origen):
        """..."""

        piezas = self.generador_pieza.get_piezas()
        for pieza in piezas:
            if pieza_en_origen in piezas[pieza]:
                i_coordenada = piezas[pieza].index(pieza_en_origen)
                return (
                    piezas[pieza][i_coordenada + 1]
                    if i_coordenada + 1 < len(piezas[pieza])
                    else piezas[pieza][0]
                )

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
