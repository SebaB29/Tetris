from graphics.tetris_gui import *
from src.tetris import *
import graphics.gamelib as gamelib

ESPERA_DESCENDER = 20


def main():
    # Inicializar el estado del juego
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    juego = Tetris()
    juegoGUI = TetrisGUI()

    timer_bajar = ESPERA_DESCENDER
    while gamelib.loop(fps=90) and not juego.terminar_juego():
        for event in gamelib.get_events():
            if event.type == gamelib.EventType.KeyPress:
                tecla = event.key.upper()
                if tecla == "A":
                    juego.mover(IZQUIERDA)
                elif tecla == "D":
                    juego.mover(DERECHA)
                elif tecla == "W":
                    juego.rotar_pieza()
                elif tecla == "S":
                    juego.descender_rapido()
                elif tecla == "P":
                    gamelib.wait(gamelib.EventType.KeyPress)
                elif tecla == "ESCAPE":
                    exit()

        timer_bajar -= 1
        if timer_bajar == 0:
            timer_bajar = ESPERA_DESCENDER
            juego.avanzar_estado_juego()

        juegoGUI.graficar_estado_juego(
            juego.get_tablero(), juego.get_tablero_p_siguiente()
        )

    nombre_jugador = gamelib.input("Ingrese su nombre")
    if nombre_jugador:
        juego.guardar_puntaje(nombre_jugador.upper())
    tabla_puntuaciones = juego.cargar_tabla_puntuaciones()

    juegoGUI.graficar_final_del_juego(tabla_puntuaciones)

    event = gamelib.wait(gamelib.EventType.ButtonPress)
    if event.x in range(
        int(ANCHO_BOTON[0]), int(ANCHO_BOTON[1]) + 1
    ) and event.y in range(ALTO_BOTON[0], ALTO_BOTON[1] + 1):
        main()


if __name__ == "__main__":
    gamelib.init(main)
