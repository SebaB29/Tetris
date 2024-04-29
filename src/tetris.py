from random import choice
from src.tablero import Tablero
from src.pieza import Pieza
import csv

PIEZA = "@"
SUPERFICIE = "#"
POSICION_LIBRE = ""
IZQUIERDA, DERECHA = -1, 1


# ESTADO DEL JUEGO
def crear_juego(filas_tablero, columnas_tablero, piezas):
    """..."""

    return {
        "TABLERO": Tablero(),
        "PIEZA_ACTUAL": Pieza(generar_pieza(piezas)),
        "CUADRO_PIEZA_SIG": crear_tablero(filas_tablero // 2, columnas_tablero),
        "PIEZA_SIGUIENTE": generar_pieza(piezas),
        "PUNTOS": 0,
    }


def iniciar_juego(juego):
    """..."""

    juego["TABLERO"].actualizar(
        elemento=PIEZA, coordenadas_elemento=juego["PIEZA_ACTUAL"].get_coordenadas()
    )

    colocar_elemento(juego["CUADRO_PIEZA_SIG"], juego["PIEZA_SIGUIENTE"], PIEZA)


def avanzar_estado_juego(juego, piezas):
    """..."""

    juego["TABLERO"].actualizar(
        elemento=PIEZA, coordenadas_elemento=juego["PIEZA_ACTUAL"].get_coordenadas()
    )

    coordenadas_deseadas = juego["PIEZA_ACTUAL"].trasladarse()
    if juego["TABLERO"].revisar_coordenadas_pieza(coordenadas_deseadas):
        juego["PIEZA_ACTUAL"].actualizar(coordenadas_deseadas)

    else:
        juego["TABLERO"].actualizar(
            elemento=PIEZA,
            coordenadas_elemento=juego["PIEZA_ACTUAL"].get_coordenadas(),
            nuevo_elemento=SUPERFICIE,
            eliminar_filas=True,
        )

        juego["PUNTOS"] += 1
        juego["PIEZA_SIGUIENTE"] = trasladar_pieza(
            juego["PIEZA_SIGUIENTE"], len(juego["TABLERO"].get_tablero()[0]) // 2, 0
        )

        if juego["TABLERO"].revisar_coordenadas_pieza(juego["PIEZA_SIGUIENTE"]):

            borrar_elemento(juego["CUADRO_PIEZA_SIG"], PIEZA)
            juego["PIEZA_ACTUAL"], juego["PIEZA_SIGUIENTE"] = Pieza(
                juego["PIEZA_SIGUIENTE"]
            ), generar_pieza(piezas)
            colocar_elemento(juego["CUADRO_PIEZA_SIG"], juego["PIEZA_SIGUIENTE"], PIEZA)
        else:
            juego["PIEZA_ACTUAL"] = None


def terminar_juego(pieza_actual):
    """..."""

    return pieza_actual == None


# ACCIONES TABLERO
def crear_tablero(filas, columnas):
    """..."""

    return [[POSICION_LIBRE for columna in range(columnas)] for fila in range(filas)]


def colocar_elemento(tablero, coordenadas_elemento, elemento):
    """..."""

    for coordenada_x, coordenada_y in coordenadas_elemento:
        tablero[coordenada_y][coordenada_x] = elemento


def borrar_elemento(tablero, elemento):
    """..."""

    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna] == elemento:
                tablero[fila][columna] = POSICION_LIBRE


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


def trasladar_pieza(coordenadas_pieza, desplazamiento_x, desplazamiento_y):
    """..."""

    return tuple(
        (coordenada_x + desplazamiento_x, coordenada_y + desplazamiento_y)
        for coordenada_x, coordenada_y in coordenadas_pieza
    )


# ACCIONES JUGADOR
def mover(juego, direccion):
    """..."""

    coordenadas_deseadas = juego["PIEZA_ACTUAL"].trasladarse(direccion, 0)
    if juego["TABLERO"].revisar_coordenadas_pieza(coordenadas_deseadas):
        juego["PIEZA_ACTUAL"].actualizar(coordenadas_deseadas)


def descender_rapido(juego):
    """..."""

    pieza = juego["PIEZA_ACTUAL"].trasladarse()

    while juego["TABLERO"].revisar_coordenadas_pieza(pieza):
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

    if juego["TABLERO"].revisar_coordenadas_pieza(pieza_trasladada):
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
