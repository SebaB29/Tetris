from src.constantes import *
from src.tablero import Tablero
from src.sistema_puntaje import SistemaPuntaje
import graphics.gamelib as gamelib


class TetrisGUI:
    """
    Clase cuya instancia se encarga de graficar todos los componentes del juego.
    """

    def __init__(self: object) -> None:
        """
        Parámetros:
            No recibe parámetros.

        Inicializa una instancia de TetrisGUI, creando la ventana del juego.

        Return:
            None
        """

        gamelib.resize(VENTANA["ANCHO"], VENTANA["ALTO"])
        gamelib.title(VENTANA["TITULO"])

    def graficar_estado_juego(
        self: object,
        tablero: Tablero,
        tablero_p_siguiente: Tablero,
        sistema_puntaje: SistemaPuntaje,
    ) -> None:
        """
        Parámetros:
            - tablero: Tablero
            - tablero_p_siguiente: Tablero
            - sistema_puntaje: SistemaPuntaje

            Muestra el estado actual del juego.

        Return:
            None
        """

        gamelib.draw_begin()
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
        """
        Parámetros:
            - tabla_puntuaciones: list

        Muestra el final del juego.

        Return:
            None
        """

        gamelib.draw_begin()
        self._graficar_tabla_puntuaciones()
        self._graficar_titulo_tabla_puntuaciones()
        self._graficar_puntajes(tabla_puntuaciones)
        self._graficar_boton_volver_a_jugar()
        gamelib.draw_end()

    def presiono_boton(self: object, event: gamelib.EventType.ButtonPress) -> bool:
        """
        Parámetros:
            - event: gamelib.EventType.ButtonPress

        Devuelve True si las coordenadas de event se enecuetran
        dentro de los rangos de BOTON_VOLVER_A_JUGAR.

        Return:
            bool
        """

        return event.x in range(
            BOTON_VOLVER_A_JUGAR["COORDENADAS"]["COORD_X1"],
            BOTON_VOLVER_A_JUGAR["COORDENADAS"]["COORD_X2"],
        ) and event.y in range(
            BOTON_VOLVER_A_JUGAR["COORDENADAS"]["COORD_Y1"],
            BOTON_VOLVER_A_JUGAR["COORDENADAS"]["COORD_Y2"],
        )

    def _graficar_tablero(self: object) -> None:
        """
        Parámetros:
            No recibe parámetros.

        Muetra el tablero de juego.

        Return:
            None
        """

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
        """
        Parámetros:
            No recibe parámetros.

        Muestra el tablero de la pieza siguiente.

        Return:
            None
        """

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
        """
        Parámetros:
            No recibe parámetros.

        Muestra el título del tablero pieza siguiente

        Return:
            None
        """

        gamelib.draw_text(
            TITULO_TABLERO_P_SIGUIENTE["TEXTO"],
            TITULO_TABLERO_P_SIGUIENTE["COORD_X"],
            TITULO_TABLERO_P_SIGUIENTE["COORD_Y"],
        )

    def _graficar_elemento(
        self: object, tablero: Tablero, elemento: str, color_elemento: str
    ) -> None:
        """
        Parámetros:
            - tablero: Tablero
            - elemento: str
            - color_elemento: str

        Muestra el elemento recibido.

        Return:
            None
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
                fill=color_elemento,
            )

    def _graficar_pieza_siguiente(
        self: object, tablero_p_siguiente: Tablero, elemento: str
    ) -> None:
        """
        Parámetros:
            - tablero_p_siguiente: Tablero
            - elemento: str

        Muestra la pieza siguiente.

        Return:
            None
        """

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

    def _graficar_teclas(self: object) -> None:
        """
        Parámetros:
            No recibe parámetros.

        Muestra las teclas y acciones disponibles.

        Return:
            None
        """

        for tecla in TECLAS:
            gamelib.draw_text(
                tecla + ": " + TECLAS[tecla]["INSTRUCCION"],
                TECLAS[tecla]["COORD_X"],
                TECLAS[tecla]["COORD_Y"],
                anchor="w",
            )

    def _graficar_puntos_actuales(self: object, puntos_actuales: int) -> None:
        """
        Parámetros:
            - puntos_actuales: int

        Muestra los puntos actuales.

        Return:
            None
        """

        gamelib.draw_text(
            PUNTAJE["TITULO"]["TEXTO"],
            PUNTAJE["TITULO"]["COORD_X"],
            PUNTAJE["TITULO"]["COORD_Y"],
            bold=True,
        )
        gamelib.draw_text(
            puntos_actuales,
            PUNTAJE["PUNTOS"]["COORD_X"],
            PUNTAJE["PUNTOS"]["COORD_Y"],
            fill=PUNTAJE["COLOR"],
            bold=True,
            anchor="e",
        )

    def _graficar_tabla_puntuaciones(self: object) -> None:
        """
        Parámetros:
            No recibe parámetros.

        Muestra una tabla para luego mostrar los puntajes.

        Return:
            None
        """

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
        """
        Parámetros:
            No recibe parámetros.

        Muestra el título de la tabla de puntuaciones.

        Return:
            None
        """

        gamelib.draw_text(
            TITULO_TABLA_PUNTAJES["TEXTO"],
            TITULO_TABLA_PUNTAJES["COORD_X"],
            TITULO_TABLA_PUNTAJES["COORD_Y"],
        )

    def _graficar_puntajes(self: object, tabla_puntuaciones: list) -> None:
        """
        Parámetros:
            - tabla_puntuaciones: list

        Muestra los puntajes de tabla puntuaciones.

        Return:
            None
        """

        coordenada_y = VENTANA["MARGEN_Y"] + 60
        for jugador, puntos in tabla_puntuaciones:
            gamelib.draw_text(jugador, VENTANA["ANCHO"] / 2 - 40, coordenada_y)
            gamelib.draw_text(
                puntos, VENTANA["ANCHO"] / 2 + 40, coordenada_y, anchor="w"
            )
            coordenada_y += 30

    def _graficar_boton_volver_a_jugar(self: object) -> None:
        """
        Parámetros:
            No recibe parámetros.

        Muestra el boton con la opción de volver a jugar.

        Return:
            None
        """

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

    def _convertir_coordenadas_a_pixels(
        self: object, coordenadas_pieza: tuple
    ) -> tuple:
        """
        Parámetros:
            coordenadas_pieza: tuple

        Convierte las coordenadas recibidas a pixels.

        Return:
            - coordenadas_en_pixels: tuple
        """

        return (
            (
                TABLERO["COORDENADAS"]["COORD_X1"]
                + TABLERO["GROSOR_BORDE"]
                + coordenada_x * CELDA_TABLERO["ANCHO"],
                TABLERO["COORDENADAS"]["COORD_Y1"]
                + TABLERO["GROSOR_BORDE"]
                + coordenada_y * CELDA_TABLERO["ALTO"],
            )
            for coordenada_x, coordenada_y in coordenadas_pieza
        )
