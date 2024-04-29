from random import choice
from src.tablero import Tablero
from src.pieza import Pieza
import csv

FILAS_TABLERO = 18
COLUMNAS_TABLERO = 9
FILAS_TABLERO_P_SIGUIENTE = FILAS_TABLERO // 2
COLUMNAS_TABLERO_P_SIGUIENTE = COLUMNAS_TABLERO // 2

PIEZA = "@"
SUPERFICIE = "#"
IZQUIERDA, DERECHA = -1, 1


# ESTADO DEL JUEGO
def crear_juego(piezas):
    """..."""

    return {
        "TABLERO": Tablero(FILAS_TABLERO, COLUMNAS_TABLERO),
        "PIEZA_ACTUAL": Pieza(generar_pieza(piezas)),
        "CUADRO_PIEZA_SIG": Tablero(
            FILAS_TABLERO_P_SIGUIENTE, COLUMNAS_TABLERO_P_SIGUIENTE
        ),
        "PIEZA_SIGUIENTE": Pieza(generar_pieza(piezas)),
        "PUNTOS": 0,
    }


def avanzar_estado_juego(juego, piezas):
    """..."""

    juego["TABLERO"].actualizar(
        elemento=PIEZA, coordenadas_elemento=juego["PIEZA_ACTUAL"].get_coordenadas()
    )

    coordenadas_deseadas = juego["PIEZA_ACTUAL"].trasladarse()
    if juego["TABLERO"].son_coordenadas_validas(coordenadas_deseadas):
        juego["PIEZA_ACTUAL"].actualizar(coordenadas_deseadas)

    else:
        juego["TABLERO"].actualizar(
            elemento=PIEZA,
            coordenadas_elemento=juego["PIEZA_ACTUAL"].get_coordenadas(),
            nuevo_elemento=SUPERFICIE,
            eliminar_filas=True,
        )

        juego["PUNTOS"] += 1
        intercambiar_pieza_actual_por_siguiente(juego, piezas)

    juego["CUADRO_PIEZA_SIG"].actualizar(
        elemento=PIEZA,
        coordenadas_elemento=juego["PIEZA_SIGUIENTE"].get_coordenadas(),
    )


def intercambiar_pieza_actual_por_siguiente(juego, piezas):

    pieza_trasladada = juego["PIEZA_SIGUIENTE"].trasladarse(COLUMNAS_TABLERO // 2, 0)

    if juego["TABLERO"].son_coordenadas_validas(pieza_trasladada):
        juego["PIEZA_ACTUAL"] = Pieza(pieza_trasladada)
        juego["PIEZA_SIGUIENTE"] = Pieza(generar_pieza(piezas))

    else:
        juego["PIEZA_ACTUAL"] = None


def terminar_juego(pieza_actual):
    """..."""

    return pieza_actual == None


# ACCIONES PIEZA
def obtener_piezas():
    """..."""

    piezas = {}
    with open("resources\piezas.txt") as archivo:
        reader = csv.reader(archivo, delimiter=" ")
        for grupo_coordenadas in reader:
            pieza = grupo_coordenadas[-1]
            piezas[pieza] = []
            for coordenadas in grupo_coordenadas[:-2]:
                piezas[pieza].append(tuple(map(eval, coordenadas.split(";"))))

    return piezas


def generar_pieza(piezas):
    """..."""

    pieza = choice(list(piezas))
    # rotacion = randint(0, len(piezas[pieza]) - 1)

    return piezas[pieza][0]


# ACCIONES JUGADOR
def mover(juego, direccion):
    """..."""

    coordenadas_deseadas = juego["PIEZA_ACTUAL"].trasladarse(direccion, 0)
    if juego["TABLERO"].son_coordenadas_validas(coordenadas_deseadas):
        juego["PIEZA_ACTUAL"].actualizar(coordenadas_deseadas)


def descender_rapido(juego):
    """..."""

    pieza = juego["PIEZA_ACTUAL"].trasladarse()

    while juego["TABLERO"].son_coordenadas_validas(pieza):
        juego["PIEZA_ACTUAL"].actualizar(pieza)
        pieza = juego["PIEZA_ACTUAL"].trasladarse()

    juego["TABLERO"].actualizar(
        elemento=PIEZA, coordenadas_elemento=juego["PIEZA_ACTUAL"].get_coordenadas()
    )


def rotar_pieza(juego, piezas):
    """..."""

    coordenada_1 = juego["PIEZA_ACTUAL"].get_coordenadas()[0]
    pieza_en_origen = juego["PIEZA_ACTUAL"].trasladarse(
        -coordenada_1[0], -coordenada_1[1]
    )

    pieza_rotada = buscar_rotacion(piezas, pieza_en_origen)

    nueva_pieza = Pieza(pieza_rotada)
    pieza_trasladada = nueva_pieza.trasladarse(coordenada_1[0], coordenada_1[1])

    if juego["TABLERO"].son_coordenadas_validas(pieza_trasladada):
        juego["PIEZA_ACTUAL"] = nueva_pieza
        juego["PIEZA_ACTUAL"].actualizar(pieza_trasladada)


def buscar_rotacion(piezas, pieza_en_origen):
    """..."""

    for pieza in piezas:
        if pieza_en_origen in piezas[pieza]:
            i_coordenada = piezas[pieza].index(pieza_en_origen)
            return (
                piezas[pieza][i_coordenada + 1]
                if i_coordenada + 1 < len(piezas[pieza])
                else piezas[pieza][0]
            )


# PUNTAJE
def cargar_tabla_puntuaciones():
    """..."""

    with open("puntaje.csv") as archivo:
        tabla_puntuaciones = [
            jugador for jugador in list(csv.reader(archivo)) if jugador
        ]
        tabla_puntuaciones = sorted(
            tabla_puntuaciones, key=lambda jugador: int(jugador[1]), reverse=True
        )

    return tabla_puntuaciones[:10]


def guardar_puntaje(nombre_jugador, puntaje_final):
    """..."""

    with open("puntaje.csv", "a") as archivo:
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerow((nombre_jugador, puntaje_final))
