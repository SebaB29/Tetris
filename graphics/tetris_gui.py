import graphics.gamelib as gamelib
from src.tablero import Tablero
from src.sistema_puntaje import SistemaPuntaje
from src.constantes import *


class TetrisGUI:

    def __init__(self: object) -> None:
        """..."""

        gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    def graficar_estado_juego(
        self: object,
        tablero: Tablero,
        tablero_p_siguiente: Tablero,
        sistema_puntaje: SistemaPuntaje,
    ) -> None:
        """..."""

        gamelib.draw_begin()
        self._graficar_titulo()
        self._graficar_tablero()
        self._graficar_tablero_pieza_siguiente()
        self._graficar_titulo_tablero_pieza_siguiente()
        self._graficar_elemento(tablero, PIEZA["SIMBOLO"], PIEZA["COLOR"])
        self._graficar_elemento(tablero, SUPERFICIE["SIMBOLO"], SUPERFICIE["COLOR"])
        self._graficar_pieza_siguiente(tablero_p_siguiente, PIEZA["SIMBOLO"])
        self._graficar_teclas()
        self._graficar_puntos_actuales(sistema_puntaje.obtener_puntos())
        gamelib.draw_end()

    def graficar_final_del_juego(self: object, tabla_puntuaciones: list) -> None:
        """..."""

        gamelib.draw_begin()
        self._graficar_tabla_puntuaciones()
        self._graficar_titulo_tabla_puntuaciones()
        self._graficar_puntajes(tabla_puntuaciones)
        self._graficar_boton_volver_a_jugar()
        gamelib.draw_end()

    def _graficar_titulo(self: object) -> None:
        """..."""

        gamelib.draw_text(TITULO["TEXTO"], TITULO["COORD_X"], TITULO["COORD_Y"])

    def _graficar_tablero(self: object) -> None:
        """..."""

        gamelib.draw_rectangle(
            TABLERO["COORDENADAS"]["COORD_X1"],
            TABLERO["COORDENADAS"]["COORD_Y1"],
            TABLERO["COORDENADAS"]["COORD_X2"],
            TABLERO["COORDENADAS"]["COORD_Y2"],
            fill=TABLERO["COLOR"],
            outline=TABLERO["COLOR_BORDE"],
            width=TABLERO["GROSOR_BORDE"],
        )

    def _graficar_tablero_pieza_siguiente(self: object) -> None:
        """..."""

        gamelib.draw_rectangle(
            TABLERO_P_SIGUIENTE["COORDENADAS"]["COORD_X1"],
            TABLERO_P_SIGUIENTE["COORDENADAS"]["COORD_Y1"],
            TABLERO_P_SIGUIENTE["COORDENADAS"]["COORD_X2"],
            TABLERO_P_SIGUIENTE["COORDENADAS"]["COORD_Y2"],
            fill=TABLERO["COLOR"],
            outline=TABLERO["COLOR_BORDE"],
            width=TABLERO["GROSOR_BORDE"],
        )

    def _graficar_titulo_tablero_pieza_siguiente(self: object) -> None:
        """..."""
        gamelib.draw_text(
            TITULO_TABLERO_P_SIGUIENTE["TEXTO"],
            TITULO_TABLERO_P_SIGUIENTE["COORD_X"],
            TITULO_TABLERO_P_SIGUIENTE["COORD_Y"],
        )

    def _graficar_teclas(self: object) -> None:
        """..."""

        for tecla in TECLAS:
            gamelib.draw_text(
                tecla + ": " + TECLAS[tecla]["INSTRUCCION"],
                TECLAS[tecla]["COORD_X"],
                TECLAS[tecla]["COORD_Y"],
                anchor="w",
            )

    def _graficar_elemento(
        self: object, tablero: Tablero, elemento: str, color: str
    ) -> None:
        """
        Recibe: las coordenadas de un elemento (list[tuples]) y su color (str)

        Dibuja en la pantalla el elemento
        """

        coordenadas_pixels = self._convertir_coordenadas_a_pixels(
            tablero.obtener_coordenadas_elemento(elemento)
        )
        for coordenada_pixels_x, coordenada_pixels_y in coordenadas_pixels:
            gamelib.draw_rectangle(
                coordenada_pixels_x,
                coordenada_pixels_y,
                coordenada_pixels_x + CELDA_TABLERO["ANCHO"],
                coordenada_pixels_y + CELDA_TABLERO["ALTO"],
                fill=color,
            )

    def _graficar_pieza_siguiente(
        self: object, tablero_p_siguiente: Tablero, elemento: str
    ) -> None:
        """..."""

        coordenadas_pixels = self._convertir_coordenadas_a_pixels(
            tablero_p_siguiente.obtener_coordenadas_elemento(elemento)
        )
        for coordenada_pixels_x, coordenada_pixels_y in coordenadas_pixels:
            coordenada_pixels_x += (
                TABLERO_P_SIGUIENTE["COORDENADAS"]["COORD_X1"]
                + TABLERO_P_SIGUIENTE["ANCHO"] / 4
            )
            coordenada_pixels_y += (
                TABLERO_P_SIGUIENTE["COORDENADAS"]["COORD_Y1"]
                + TABLERO_P_SIGUIENTE["ALTO"] / 6
            )
            gamelib.draw_rectangle(
                coordenada_pixels_x,
                coordenada_pixels_y,
                coordenada_pixels_x + CELDA_TABLERO["ANCHO"],
                coordenada_pixels_y + CELDA_TABLERO["ALTO"],
                fill=PIEZA["COLOR"],
            )

    def _graficar_tabla_puntuaciones(self: object) -> None:
        """..."""

        gamelib.draw_rectangle(
            TABLA_PUNTAJES["COORDENADAS"]["COORD_X1"],
            TABLA_PUNTAJES["COORDENADAS"]["COORD_Y1"],
            TABLA_PUNTAJES["COORDENADAS"]["COORD_X2"],
            TABLA_PUNTAJES["COORDENADAS"]["COORD_Y2"],
            fill=TABLA_PUNTAJES["COLOR"],
            outline=TABLA_PUNTAJES["COLOR_BORDE"],
            width=TABLA_PUNTAJES["GROSOR_BORDE"],
        )

    def _graficar_titulo_tabla_puntuaciones(self: object) -> None:
        """..."""

        gamelib.draw_text(
            TITULO_TABLA_PUNTAJES["TEXTO"],
            TITULO_TABLA_PUNTAJES["COORD_X"],
            TITULO_TABLA_PUNTAJES["COORD_Y"],
        )

    def _graficar_puntos_actuales(self: object, puntos: int) -> None:
        """..."""

        gamelib.draw_text(
            PUNTAJE["TITULO"]["TEXTO"],
            PUNTAJE["TITULO"]["COORD_X"],
            PUNTAJE["TITULO"]["COORD_Y"],
            bold=True,
        )
        gamelib.draw_text(
            puntos,
            PUNTAJE["PUNTOS"]["COORD_X"],
            PUNTAJE["PUNTOS"]["COORD_Y"],
            fill=PUNTAJE["COLOR"],
            bold=True,
        )

    def _graficar_puntajes(self: object, tabla_puntuaciones: list) -> None:
        """..."""

        coordenada_y = MARGEN_Y + 60
        for jugador, puntos in tabla_puntuaciones:
            gamelib.draw_text(jugador, ANCHO_VENTANA / 2 - 40, coordenada_y)
            gamelib.draw_text(puntos, ANCHO_VENTANA / 2 + 40, coordenada_y, anchor="w")
            coordenada_y += 30

    def _graficar_boton_volver_a_jugar(self: object) -> None:
        """..."""

        gamelib.draw_rectangle(
            BOTON_VOLVER_A_JUGAR["COORDENADAS"]["COORD_X1"],
            BOTON_VOLVER_A_JUGAR["COORDENADAS"]["COORD_Y1"],
            BOTON_VOLVER_A_JUGAR["COORDENADAS"]["COORD_X2"],
            BOTON_VOLVER_A_JUGAR["COORDENADAS"]["COORD_Y2"],
            fill=BOTON_VOLVER_A_JUGAR["COLOR"],
            outline=BOTON_VOLVER_A_JUGAR["COLOR_BORDE"],
        )
        gamelib.draw_text(
            TITULO_BOTON_VOLVER_A_JUGAR["TEXTO"],
            TITULO_BOTON_VOLVER_A_JUGAR["COORD_X"],
            TITULO_BOTON_VOLVER_A_JUGAR["COORD_Y"],
            size=TITULO_BOTON_VOLVER_A_JUGAR["SIZE"],
        )

    def _convertir_coordenadas_a_pixels(self: object, coordenadas_pieza: list) -> list:
        """..."""

        return [
            (
                TABLERO["COORDENADAS"]["COORD_X1"]
                + TABLERO["GROSOR_BORDE"]
                + coordenada_x * CELDA_TABLERO["ANCHO"],
                TABLERO["COORDENADAS"]["COORD_Y1"]
                + TABLERO["GROSOR_BORDE"]
                + coordenada_y * CELDA_TABLERO["ALTO"],
            )
            for coordenada_x, coordenada_y in coordenadas_pieza
        ]

    def presiono_boton(self: object, event: gamelib.EventType.ButtonPress) -> bool:
        return (
            event
            and event.x
            in range(
                BOTON_VOLVER_A_JUGAR["COORDENADAS"]["COORD_X1"],
                BOTON_VOLVER_A_JUGAR["COORDENADAS"]["COORD_X2"],
            )
            and event.y
            in range(
                BOTON_VOLVER_A_JUGAR["COORDENADAS"]["COORD_Y1"],
                BOTON_VOLVER_A_JUGAR["COORDENADAS"]["COORD_Y2"],
            )
        )
