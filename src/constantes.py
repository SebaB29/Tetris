# ARCHIVOS
ARCHIVO_PIEZAS = "resources\piezas.txt"

# VENTANA JUEGO
ANCHO_VENTANA = 500
ALTO_VENTANA = 500
MARGEN_X = 10
MARGEN_Y = 50

TITULO = {"TEXTO": "TETRIS", "COORD_X": ANCHO_VENTANA / 2, "COORD_Y": MARGEN_Y / 2}

TABLERO = {
    "FILAS": 18,
    "COLUMNAS": 9,
    "COLOR": "#465362",
    "COLOR_BORDE": "#707070",
    "GROSOR_BORDE": 5,
    "COORDENADAS": {
        "COORD_X1": MARGEN_X,
        "COORD_X2": ANCHO_VENTANA / 2,
        "COORD_Y1": MARGEN_Y,
        "COORD_Y2": ALTO_VENTANA - MARGEN_Y,
    },
    "ANCHO": ANCHO_VENTANA / 2 - MARGEN_X,
    "ALTO": ALTO_VENTANA - 2 * MARGEN_Y,
}

CELDA_TABLERO = {
    "ANCHO": (TABLERO["ANCHO"] - TABLERO["GROSOR_BORDE"] * 2) / TABLERO["COLUMNAS"],
    "ALTO": (TABLERO["ALTO"] - TABLERO["GROSOR_BORDE"] * 2) / TABLERO["FILAS"],
}

TABLERO_P_SIGUIENTE = {
    "FILAS": TABLERO["FILAS"] // 2,
    "COLUMNAS": TABLERO["COLUMNAS"] // 2,
    "GROSOR_BORDE": 5,
    "COORDENADAS": {
        "COORD_X1": MARGEN_X + ANCHO_VENTANA / 2,
        "COORD_X2": ANCHO_VENTANA - MARGEN_X,
        "COORD_Y1": MARGEN_Y,
        "COORD_Y2": ALTO_VENTANA / 2,
    },
    "ANCHO": ANCHO_VENTANA / 2 - 2 * MARGEN_X,
    "ALTO": ALTO_VENTANA / 2 - MARGEN_Y,
}

TITULO_TABLERO_P_SIGUIENTE = {
    "TEXTO": "PIEZA SIGUIENTE",
    "COORD_X": TABLERO_P_SIGUIENTE["COORDENADAS"]["COORD_X1"]
    + TABLERO_P_SIGUIENTE["ANCHO"] / 2,
    "COORD_Y": TABLERO_P_SIGUIENTE["COORDENADAS"]["COORD_Y1"] + 15,
}

BOTON_VOLVER_A_JUGAR = {
    "COLOR": "#000",
    "COLOR_BORDE": "#FFF",
    "COORDENADAS": {
        "COORD_X1": ANCHO_VENTANA // 4,
        "COORD_X2": ANCHO_VENTANA * 3 // 4,
        "COORD_Y1": 400,
        "COORD_Y2": 450,
    },
    "ANCHO": ANCHO_VENTANA * 3 // 4 - ANCHO_VENTANA // 4,
    "ALTO": 50,
}

TITULO_BOTON_VOLVER_A_JUGAR = {
    "TEXTO": "Volver a Empezar",
    "COORD_X": BOTON_VOLVER_A_JUGAR["COORDENADAS"]["COORD_X1"]
    + BOTON_VOLVER_A_JUGAR["ANCHO"] / 2,
    "COORD_Y": BOTON_VOLVER_A_JUGAR["COORDENADAS"]["COORD_Y1"]
    + BOTON_VOLVER_A_JUGAR["ALTO"] / 2,
    "SIZE": 15,
}

TECLAS = {
    "A": {
        "INSTRUCCION": "IZQUIERDA",
        "COORD_Y": ALTO_VENTANA / 2 + 30,
        "COORD_X": 4 / 6 * ANCHO_VENTANA - MARGEN_X,
    },
    "D": {
        "INSTRUCCION": "DERECHA",
        "COORD_Y": ALTO_VENTANA / 2 + 50,
        "COORD_X": 4 / 6 * ANCHO_VENTANA - MARGEN_X,
    },
    "W": {
        "INSTRUCCION": "ROTAR",
        "COORD_Y": ALTO_VENTANA / 2 + 70,
        "COORD_X": 4 / 6 * ANCHO_VENTANA - MARGEN_X,
    },
    "S": {
        "INSTRUCCION": "DESCENDER",
        "COORD_Y": ALTO_VENTANA / 2 + 90,
        "COORD_X": 4 / 6 * ANCHO_VENTANA - MARGEN_X,
    },
    "P": {
        "INSTRUCCION": "PAUSA",
        "COORD_Y": ALTO_VENTANA / 2 + 110,
        "COORD_X": 4 / 6 * ANCHO_VENTANA - MARGEN_X,
    },
}

TABLA_PUNTAJES = {
    "COLOR": "#000",
    "COLOR_BORDE": "#FFF",
    "GROSOR_BORDE": 5,
    "COORDENADAS": {
        "COORD_X1": MARGEN_X,
        "COORD_X2": ANCHO_VENTANA - 5,
        "COORD_Y1": MARGEN_Y,
        "COORD_Y2": ALTO_VENTANA - 10,
    },
}

TITULO_TABLA_PUNTAJES = {
    "TEXTO": "PUNTAJE",
    "COORD_X": ANCHO_VENTANA / 2,
    "COORD_Y": MARGEN_Y + 20,
}

# ELEMENTOS
PIEZA = {
    "SIMBOLO": "@",
    "COLOR": "#39FF14",
}

SUPERFICIE = {
    "SIMBOLO": "#",
    "COLOR": "#800080",
}

POSICION_LIBRE = ""

# DIRECCIÓN MOVIMIENTO
IZQUIERDA = -1
DERECHA = 1