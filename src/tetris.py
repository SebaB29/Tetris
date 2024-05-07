import graphics.gamelib as gamelib
from src.tablero import Tablero
from src.generador_piezas import GeneradorPieza
from graphics.tetris_gui import TetrisGUI
from src.sistema_puntaje import SistemaPuntaje
from src.constantes import *


class Tetris:

    def __init__(self: object) -> None:
        """..."""

        self._tablero = Tablero(TABLERO["FILAS"], TABLERO["COLUMNAS"])
        self._tablero_p_siguiente = Tablero(
            TABLERO_P_SIGUIENTE["FILAS"], TABLERO_P_SIGUIENTE["COLUMNAS"]
        )
        self._generador_pieza = GeneradorPieza()
        self._pieza_actual = self._generador_pieza.generar_pieza()
        self._pieza_siguiente = self._generador_pieza.generar_pieza()
        self._puntos = 0

        self._graficador = TetrisGUI()
        self._sistema_puntos = SistemaPuntaje()

    def transcurso_del_juego(self: object) -> None:
        """..."""

        while gamelib.loop(fps=5) and self._pieza_actual:
            self._procesar_eventos()
            self._avanzar_estado_juego()
            self._graficador.graficar_estado_juego(
                self._tablero, self._tablero_p_siguiente
            )

    def final_del_juego(self: object) -> bool:
        """..."""

        self._sistema_puntos.guardar_puntaje(self._puntos)
        self._graficador.graficar_final_del_juego(
            self._sistema_puntos.obtener_puntajes_mas_altos()
        )

        return self._graficador.presiono_boton(
            gamelib.wait(gamelib.EventType.ButtonPress)
        )

    def _avanzar_estado_juego(self: object) -> None:
        """..."""

        self._tablero.actualizar(
            elemento=PIEZA["SIMBOLO"],
            coordenadas_elemento=self._pieza_actual.get_coordenadas(),
        )

        coordenadas_deseadas = self._pieza_actual.trasladarse()
        if self._tablero.son_coordenadas_validas(coordenadas_deseadas):
            self._pieza_actual.actualizar(coordenadas_deseadas)

        else:
            self._tablero.actualizar(
                elemento=PIEZA["SIMBOLO"],
                coordenadas_elemento=self._pieza_actual.get_coordenadas(),
                eliminar_elemento=True,
                eliminar_filas=True,
            )
            self._intercambiar_pieza_actual_por_siguiente()
            self._puntos += 1

        self._tablero_p_siguiente.actualizar(
            elemento=PIEZA["SIMBOLO"],
            coordenadas_elemento=self._pieza_siguiente.get_coordenadas(),
        )

    def _intercambiar_pieza_actual_por_siguiente(self: object) -> None:
        """..."""

        pieza_trasladada = self._pieza_siguiente.trasladarse(
            TABLERO["COLUMNAS"] // 2, 0
        )

        if self._tablero.son_coordenadas_validas(pieza_trasladada):
            self._pieza_siguiente.actualizar(pieza_trasladada)
            self._pieza_actual = self._pieza_siguiente
            self._pieza_siguiente = self._generador_pieza.generar_pieza()

        else:
            self._pieza_actual = None

    def _procesar_eventos(self: object) -> None:
        """..."""

        for event in gamelib.get_events():
            if event and event.type == gamelib.EventType.KeyPress:
                tecla = event.key.upper()
                if tecla == "A":
                    self._mover(IZQUIERDA)
                elif tecla == "D":
                    self._mover(DERECHA)
                elif tecla == "W":
                    self._pieza_actual.rotar(self._tablero)
                elif tecla == "S":
                    self._pieza_actual.descender_rapido(self._tablero)
                elif tecla == "P":
                    gamelib.wait(gamelib.EventType.KeyPress)
                elif tecla == "ESCAPE":
                    exit()

    def _mover(self: object, direccion) -> None:
        """..."""

        coordenadas_deseadas = self._pieza_actual.trasladarse(direccion, 0)
        if self._tablero.son_coordenadas_validas(coordenadas_deseadas):
            self._pieza_actual.actualizar(coordenadas_deseadas)
