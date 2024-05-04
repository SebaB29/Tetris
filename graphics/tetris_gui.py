import graphics.gamelib as gamelib

ANCHO_VENTANA, ALTO_VENTANA = (500, 500)
MARGEN_X, MARGEN_Y = (10, 40)
FILAS, COLUMNAS = (18, 9)
ANCHO_TABLERO, ALTO_TABLERO = (
    ANCHO_VENTANA / 2 - MARGEN_X,
    ALTO_VENTANA - MARGEN_Y * 2,
)
ANCHO_CELDA, ALTO_CELDA = (ANCHO_TABLERO / COLUMNAS, ALTO_TABLERO / FILAS)
ANCHO_BOTON, ALTO_BOTON = ((ANCHO_VENTANA * 1 / 4, ANCHO_VENTANA * 3 / 4), (400, 450))
TECLAS_A_MOSTRAR = {
    "A : IZQUIERDA": (3 / 4 * ANCHO_VENTANA - MARGEN_X, ALTO_VENTANA / 2 + 20),
    "D : DERECHA": (3 / 4 * ANCHO_VENTANA - MARGEN_X, ALTO_VENTANA / 2 + 40),
    "W : ROTAR": (3 / 4 * ANCHO_VENTANA - MARGEN_X, ALTO_VENTANA / 2 + 60),
    "S : DESCENDER": (3 / 4 * ANCHO_VENTANA - MARGEN_X, ALTO_VENTANA / 2 + 80),
    "P : PAUSA": (3 / 4 * ANCHO_VENTANA - MARGEN_X, ALTO_VENTANA / 2 + 100),
}

PIEZA = "@"
SUPERFICIE = "#"


class TetrisGUI:

    def __init__(self: object) -> None:
        pass

    def graficar_estado_juego(self: object, tablero: tuple, tablero_p_siguiente: tuple):
        """..."""

        gamelib.draw_begin()
        self.graficar_titulo()
        self.graficar_tablero()
        self.graficar_teclas()
        self.graficar_elemento(tablero, PIEZA)
        self.graficar_elemento(tablero, SUPERFICIE)
        self.graficar_tablero_pieza_siguiente()
        self.graficar_pieza_siguiente(tablero_p_siguiente, PIEZA)
        gamelib.draw_end()

    def graficar_final_del_juego(self: object, tabla_puntuaciones: list):
        """..."""

        gamelib.draw_begin()
        self.graficar_tabla_puntuaciones(tabla_puntuaciones)
        self.graficar_boton_volver_a_jugar()
        gamelib.draw_end()

    def graficar_titulo(self: object):
        """..."""

        gamelib.draw_text("TETRIS", ANCHO_VENTANA / 2, MARGEN_Y / 2)

    def graficar_tablero(self: object):
        """..."""

        gamelib.draw_rectangle(
            MARGEN_X,
            MARGEN_Y,
            ANCHO_VENTANA / 2,
            ALTO_VENTANA - MARGEN_Y,
            fill="#000",
            outline="#02F",
            width=2,
        )

    def graficar_teclas(self: object):
        """..."""

        for tecla in TECLAS_A_MOSTRAR:
            gamelib.draw_text(
                tecla,
                TECLAS_A_MOSTRAR[tecla][0] - 50,
                TECLAS_A_MOSTRAR[tecla][1],
                anchor="w",
            )

    def graficar_elemento(self: object, tablero, elemento):
        """
        Recibe: las coordenadas de un elemento (list[tuples]) y su color (str)

        Dibuja en la pantalla el elemento
        """

        coordenadas_pixels = self.convertir_coordenadas_a_pixels(tablero, elemento)
        for coordenada_pixels_y, coordenada_pixels_x in coordenadas_pixels:
            gamelib.draw_rectangle(
                coordenada_pixels_x,
                coordenada_pixels_y,
                coordenada_pixels_x + ANCHO_CELDA,
                coordenada_pixels_y + ALTO_CELDA,
                fill="#0F0",
            )

    def graficar_tablero_pieza_siguiente(self: object):
        """..."""

        gamelib.draw_rectangle(
            MARGEN_X + ANCHO_VENTANA / 2,
            MARGEN_Y,
            ANCHO_VENTANA - MARGEN_X,
            ALTO_VENTANA / 2,
            fill="#000000",
            outline="#0020FF",
            width=2,
        )
        gamelib.draw_text(
            "PIEZA SIGUIENTE", 3 / 4 * ANCHO_VENTANA - MARGEN_X, MARGEN_Y + 15
        )

    def graficar_pieza_siguiente(self: object, cuadro_pieza_siguiente, elemento):
        """..."""

        coordenadas_pixels = self.convertir_coordenadas_a_pixels(
            cuadro_pieza_siguiente, elemento
        )
        for coordenada_pixels_y, coordenada_pixels_x in coordenadas_pixels:
            coordenada_pixels_x = coordenada_pixels_x + 3 / 4 * ANCHO_VENTANA - MARGEN_X
            coordenada_pixels_y = coordenada_pixels_y + MARGEN_Y * 2
            gamelib.draw_rectangle(
                coordenada_pixels_x,
                coordenada_pixels_y,
                coordenada_pixels_x + ANCHO_CELDA,
                coordenada_pixels_y + ALTO_CELDA,
                fill="#0F0",
            )

    def graficar_tabla_puntuaciones(self: object, tabla_puntuaciones):
        """..."""

        gamelib.draw_rectangle(
            MARGEN_X,
            MARGEN_Y,
            ANCHO_VENTANA - 5,
            ALTO_VENTANA - 10,
            outline="#FFF",
            fill="#000",
            width=5,
        )
        gamelib.draw_text("PUNTAJES", ANCHO_VENTANA / 2, MARGEN_Y + 20)

        coordenada_y = MARGEN_Y + 60
        for jugador, puntos in tabla_puntuaciones:
            gamelib.draw_text(jugador, ANCHO_VENTANA / 2 - 40, coordenada_y)
            gamelib.draw_text(puntos, ANCHO_VENTANA / 2 + 40, coordenada_y, anchor="w")
            coordenada_y += 30

    def graficar_boton_volver_a_jugar(self: object):
        """..."""

        gamelib.draw_rectangle(
            ANCHO_BOTON[0],
            ALTO_BOTON[0],
            ANCHO_BOTON[1],
            ALTO_BOTON[1],
            fill="#000",
            outline="#FFF",
        )
        gamelib.draw_text(
            "Volver a empezar", sum(ANCHO_BOTON) / 2, sum(ALTO_BOTON) / 2, size=15
        )

    def convertir_coordenadas_a_pixels(self: object, tablero, elemento):
        """..."""

        return [
            (MARGEN_Y + fila * ALTO_CELDA, MARGEN_X + columna * ANCHO_CELDA)
            for fila in range(len(tablero))
            for columna in range(len(tablero[fila]))
            if tablero[fila][columna] == elemento
        ]