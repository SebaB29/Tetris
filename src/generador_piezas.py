from src.pieza import Pieza
from random import choice
import csv

ARCHIVO_PIEZAS = "resources\piezas.txt"


class GeneradorPieza:

    def __init__(self: object) -> None:
        """..."""
        self.piezas = {}
        self.cargar_piezas()

    def get_piezas(self: object):
        """..."""

        return self.piezas

    def cargar_piezas(self: object) -> None:
        """..."""

        with open(ARCHIVO_PIEZAS) as archivo:
            reader = csv.reader(archivo, delimiter=" ")

            for grupo_coordenadas in reader:
                pieza = grupo_coordenadas[-1]
                self.piezas[pieza] = []
                for coordenadas in grupo_coordenadas[:-2]:
                    self.piezas[pieza].append(tuple(map(eval, coordenadas.split(";"))))

    def generar_pieza(self: object, coordenadas: tuple = None) -> Pieza:
        """..."""

        if not coordenadas:
            pieza_aleatoria = choice(list(self.piezas))
            # rotacion = randint(0, len(piezas[pieza]) - 1)
            coordenadas = self.piezas[pieza_aleatoria][0]

        return Pieza(coordenadas)
