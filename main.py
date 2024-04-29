from graphics.inter_grafica import *
from src.tetris import *

ESPERA_DESCENDER = 20


def main():
    # Inicializar el estado del juego
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    piezas = obtener_piezas()
    juego = crear_juego(piezas)

    timer_bajar = ESPERA_DESCENDER
    while gamelib.loop(fps=90) and not terminar_juego(juego["PIEZA_ACTUAL"]):
        for event in gamelib.get_events():
            if event.type == gamelib.EventType.KeyPress:
                tecla = event.key.upper()
                if tecla == "A":
                    mover(juego, IZQUIERDA)
                elif tecla == "D":
                    mover(juego, DERECHA)
                elif tecla == "W":
                    rotar_pieza(juego, piezas)
                elif tecla == "S":
                    descender_rapido(juego)
                elif tecla == "P":
                    gamelib.wait(gamelib.EventType.KeyPress)
                elif tecla == "ESCAPE":
                    exit()

        timer_bajar -= 1
        if timer_bajar == 0:
            timer_bajar = ESPERA_DESCENDER
            avanzar_estado_juego(juego, piezas)

        gamelib.draw_begin()
        graficar_titulo()
        graficar_tablero()
        graficar_teclas()
        graficar_elemento(juego["TABLERO"].get_tablero(), PIEZA)
        graficar_elemento(juego["TABLERO"].get_tablero(), SUPERFICIE)
        graficar_tablero_pieza_siguiente()
        graficar_pieza_siguiente(juego["CUADRO_PIEZA_SIG"].get_tablero(), PIEZA)
        gamelib.draw_end()

    nombre_jugador = gamelib.input("Ingrese su nombre")
    if nombre_jugador:
        guardar_puntaje(nombre_jugador.upper(), juego["PUNTOS"])
    tabla_puntuaciones = cargar_tabla_puntuaciones()

    gamelib.draw_begin()
    graficar_tabla_puntucaciones(tabla_puntuaciones)
    graficar_boton_volver_a_jugar()
    gamelib.draw_end()

    event = gamelib.wait(gamelib.EventType.ButtonPress)
    if event.x in range(
        int(ANCHO_BOTON[0]), int(ANCHO_BOTON[1]) + 1
    ) and event.y in range(ALTO_BOTON[0], ALTO_BOTON[1] + 1):
        main()


if __name__ == "__main__":
    gamelib.init(main)
