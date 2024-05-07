from src.constantes import ARCHIVO_PIEZAS
from src.pieza import Pieza
from random import choice
import csv


class GeneradorPieza:

    def __init__(self: object) -> None:
        """..."""
        self.piezas = {}
        self._cargar_piezas()

    def generar_pieza(self: object, coordenadas: tuple = None) -> Pieza:
        """..."""

        if not coordenadas:
            pieza_aleatoria = choice(list(self.piezas))
            coordenadas = self.piezas[pieza_aleatoria][0]

        return Pieza(coordenadas, self.piezas[pieza_aleatoria])

    def _cargar_piezas(self: object) -> None:
        """..."""

        with open(ARCHIVO_PIEZAS) as archivo:
            reader = csv.reader(archivo, delimiter=" ")

            for grupo_coordenadas in reader:
                pieza = grupo_coordenadas[-1]
                self.piezas[pieza] = []
                for coordenadas in grupo_coordenadas[:-2]:
                    self.piezas[pieza].append(tuple(map(eval, coordenadas.split(";"))))
