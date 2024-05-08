from src.constantes import TABLERO, TABLERO_P_SIGUIENTE, PIEZA, IZQUIERDA, DERECHA
from src.tablero import Tablero
from src.generador_piezas import GeneradorPieza
from src.sistema_puntaje import SistemaPuntaje
from graphics.tetris_gui import TetrisGUI
import graphics.gamelib as gamelib


class Tetris:
    """
    Clase cuya instancia se encarga de la logica del juego.
    """

    def __init__(self: object) -> None:
        """
        Parámetros:
            No recibe parámetros.

        Inicializa una instancia de Tetris, iniciando el tablero del juego,
        el tablero donde se muestra la pieza siguiente, el generador de piezas,
        las piezas (actual y siguiente), el sistema de puntuación y el grficador.


        Return:
            None
        """

        self._tablero = Tablero(TABLERO["FILAS"], TABLERO["COLUMNAS"])
        self._tablero_p_siguiente = Tablero(
            TABLERO_P_SIGUIENTE["FILAS"], TABLERO_P_SIGUIENTE["COLUMNAS"]
        )
        self._generador_pieza = GeneradorPieza()
        self._pieza_actual = self._generador_pieza.generar_pieza()
        self._pieza_siguiente = self._generador_pieza.generar_pieza()
        self._sistema_puntos = SistemaPuntaje()

        self._graficador = TetrisGUI()

    def transcurso_del_juego(self: object) -> None:
        """
        Parámetros:
            No recibe paráetros.

        Ejecuta el flujo del juego, procesando los eventos, actualizando el estado y
        graficando el estado de juego.

        Return:
            None
        """

        pieza_trasladada = self._pieza_actual.trasladarse(TABLERO["COLUMNAS"] // 2, 0)
        self._pieza_actual.actualizar(pieza_trasladada)

        while gamelib.loop(fps=5) and self._pieza_actual:
            self._procesar_eventos()
            self._avanzar_estado_juego()
            self._graficador.graficar_estado_juego(
                self._tablero, self._tablero_p_siguiente, self._sistema_puntos
            )

    def final_del_juego(self: object) -> bool:
        """
        Parámetros:
            No recibe parámetros.

        Ejecuta el final del juego, guardando el puntaje del jugador,
        mostrando el listado de puntos y un botón para volver a jugar.
        Devuelve True en caso de que se presione el botón.

        Return:
            bool
        """

        self._sistema_puntos.guardar_puntaje()
        self._graficador.graficar_final_del_juego(
            self._sistema_puntos.obtener_puntajes_mas_altos()
        )

        volver_a_jugar = False
        event = gamelib.wait(gamelib.EventType.ButtonPress)
        while event and not volver_a_jugar:
            volver_a_jugar = self._graficador.presiono_boton(event)
            if not volver_a_jugar:
                event = gamelib.wait(gamelib.EventType.ButtonPress)

        return volver_a_jugar

    def _avanzar_estado_juego(self: object) -> None:
        """
        Parámetros:
            No recibe parámetros.

        Actualiza el estado del juego, actualizando el tablero, el tablero
        de la pieza siguiente, la posición de la pieza y los puntos.

        Return:
            None
        """

        self._tablero.actualizar(
            elemento=PIEZA["SIMBOLO"],
            coordenadas_elemento=self._pieza_actual.obtener_coordenadas(),
        )

        coordenadas_deseadas = self._pieza_actual.trasladarse()
        if self._tablero.son_coordenadas_validas(coordenadas_deseadas):
            self._pieza_actual.actualizar(coordenadas_deseadas)

        else:
            filas_eliminadas = self._tablero.actualizar(
                elemento=PIEZA["SIMBOLO"],
                coordenadas_elemento=self._pieza_actual.obtener_coordenadas(),
                eliminar_elemento=True,
                eliminar_filas=True,
            )
            self._intercambiar_pieza_actual_por_siguiente()
            self._sistema_puntos.actualizar_puntaje(filas_eliminadas)

        self._tablero_p_siguiente.actualizar(
            elemento=PIEZA["SIMBOLO"],
            coordenadas_elemento=self._pieza_siguiente.obtener_coordenadas(),
        )

    def _intercambiar_pieza_actual_por_siguiente(self: object) -> None:
        """
        Parámetros:
            No recibe parámetros.

        Actualiza la pieza actual, cambiandola por la siguiente y genera
        una nueva pieza siguiente.

        Return:
            None
        """

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
        """
        Parámetros:
            No recibe parámetros.

        Procesa las acciones del jugador.

        Return:
            None
        """

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

    def _mover(self: object, direccion: int) -> None:
        """
        Parámetros:
            - direccion: int

        Le indica a la pieza que tiene que moverse en la dirección recibida.
        En caso de poder moverse, actualiza las coordenadas de la pieza.

        Return:
            None
        """

        coordenadas_deseadas = self._pieza_actual.trasladarse(direccion, 0)
        if self._tablero.son_coordenadas_validas(coordenadas_deseadas):
            self._pieza_actual.actualizar(coordenadas_deseadas)
