# ARCHIVOS
ARCHIVO_PIEZAS = "resources\piezas.txt"

VENTANA = {
    "TITULO": "TETRIS",
    "ANCHO": 500,
    "ALTO": 500,
    "MARGEN_X": 10,
    "MARGEN_Y": 50,
}

TABLERO = {
    "FILAS": 18,
    "COLUMNAS": 9,
    "COLOR": "#000000",
    "COLOR_BORDE": "#007FFF",
    "GROSOR_BORDE": 5,
    "COORDENADAS": {
        "COORD_X1": VENTANA["MARGEN_X"],
        "COORD_X2": VENTANA["ANCHO"] / 2,
        "COORD_Y1": VENTANA["MARGEN_Y"],
        "COORD_Y2": VENTANA["ALTO"] - VENTANA["MARGEN_Y"],
    },
    "ANCHO": VENTANA["ANCHO"] / 2 - VENTANA["MARGEN_X"],
    "ALTO": VENTANA["ALTO"] - 2 * VENTANA["MARGEN_Y"],
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
        "COORD_X1": VENTANA["MARGEN_X"] + VENTANA["ANCHO"] / 2,
        "COORD_X2": VENTANA["ANCHO"] - VENTANA["MARGEN_X"],
        "COORD_Y1": VENTANA["MARGEN_Y"],
        "COORD_Y2": VENTANA["ALTO"] / 2,
    },
    "ANCHO": VENTANA["ANCHO"] / 2 - 2 * VENTANA["MARGEN_X"],
    "ALTO": VENTANA["ALTO"] / 2 - VENTANA["MARGEN_Y"],
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
        "COORD_X1": VENTANA["ANCHO"] // 4,
        "COORD_X2": VENTANA["ANCHO"] * 3 // 4,
        "COORD_Y1": 400,
        "COORD_Y2": 450,
    },
    "ANCHO": VENTANA["ANCHO"] * 3 // 4 - VENTANA["ANCHO"] // 4,
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
        "COORD_Y": TABLERO_P_SIGUIENTE["COORDENADAS"]["COORD_Y2"] + 15,
        "COORD_X": 4 / 6 * VENTANA["ANCHO"] - VENTANA["MARGEN_X"],
    },
    "D": {
        "INSTRUCCION": "DERECHA",
        "COORD_Y": TABLERO_P_SIGUIENTE["COORDENADAS"]["COORD_Y2"] + 35,
        "COORD_X": 4 / 6 * VENTANA["ANCHO"] - VENTANA["MARGEN_X"],
    },
    "W": {
        "INSTRUCCION": "ROTAR",
        "COORD_Y": TABLERO_P_SIGUIENTE["COORDENADAS"]["COORD_Y2"] + 55,
        "COORD_X": 4 / 6 * VENTANA["ANCHO"] - VENTANA["MARGEN_X"],
    },
    "S": {
        "INSTRUCCION": "DESCENDER",
        "COORD_Y": TABLERO_P_SIGUIENTE["COORDENADAS"]["COORD_Y2"] + 75,
        "COORD_X": 4 / 6 * VENTANA["ANCHO"] - VENTANA["MARGEN_X"],
    },
    "P": {
        "INSTRUCCION": "PAUSA",
        "COORD_Y": TABLERO_P_SIGUIENTE["COORDENADAS"]["COORD_Y2"] + 95,
        "COORD_X": 4 / 6 * VENTANA["ANCHO"] - VENTANA["MARGEN_X"],
    },
}

PUNTAJE = {
    "TITULO": {
        "TEXTO": "PUNTOS",
        "COORD_X": TABLERO["COORDENADAS"]["COORD_X2"] + VENTANA["MARGEN_X"] * 8,
        "COORD_Y": TECLAS["P"]["COORD_Y"] + VENTANA["MARGEN_Y"],
    },
    "PUNTOS": {
        "COORD_X": TABLERO["COORDENADAS"]["COORD_X2"] + VENTANA["MARGEN_X"] * 19,
        "COORD_Y": TECLAS["P"]["COORD_Y"] + VENTANA["MARGEN_Y"],
    },
    "COLOR": "#FFD700",
}

TABLA_PUNTAJES = {
    "COLOR": "#000",
    "COLOR_BORDE": "#FFF",
    "GROSOR_BORDE": 5,
    "COORDENADAS": {
        "COORD_X1": VENTANA["MARGEN_X"],
        "COORD_X2": VENTANA["ANCHO"] - 5,
        "COORD_Y1": VENTANA["MARGEN_Y"],
        "COORD_Y2": VENTANA["ALTO"] - 10,
    },
}

TITULO_TABLA_PUNTAJES = {
    "TEXTO": "PUNTAJE",
    "COORD_X": VENTANA["ANCHO"] / 2,
    "COORD_Y": VENTANA["MARGEN_Y"] + 20,
}

# ELEMENTOS
PIEZA = {
    "SIMBOLO": "@",
    "COLOR": "#39FF14",
}

SUPERFICIE = {
    "SIMBOLO": "#",
    "COLOR": "#9400D3",
}

POSICION_LIBRE = ""

# DIRECCIÓN MOVIMIENTO
IZQUIERDA = -1
DERECHA = 1
