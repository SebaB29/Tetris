from src.constantes import ARCHIVO_PIEZAS
from src.pieza import Pieza
from random import choice
import csv


class GeneradorPieza:
    """
    Clase cuya instancia se encarga de cargar las piezas disponibles en el juego,
    guardarselas y generar objetos Pieza a partir de las piezas guardadas.
    """

    def __init__(self: object) -> None:
        """
        Parámetros:
            No recibe parámetros.

        Inicializa una instancia de GeneradorPieza, creando el atributo self._piezas
        y ejecutando la función self._cargar_piezas()

        Return:
            None
        """

        self._piezas = {}
        self._cargar_piezas()

    def generar_pieza(self: object, coordenadas: tuple = None) -> Pieza:
        """
        Parámetros:
            - coordenadas: tuple

        Devuelve un objeto Pieza, generado a partir de las coordenadas recibidas por parámetro
        o en caso no recibir coordenadas (por defecto None), elige unas de self._piezas de forma aleatoria.

        Return:
            - nueva_pieza: Pieza(coordenadas, rotaciones_disponibles)
        """

        if not coordenadas:
            pieza_aleatoria = choice(list(self._piezas))
            coordenadas = self._piezas[pieza_aleatoria][0]

        return Pieza(coordenadas, self._piezas[pieza_aleatoria])

    def _cargar_piezas(self: object) -> None:
        """
        Parámetros:
            No recibe parámetros.

        Carga desde ARCHIVO_PIEZAS todas las piezas disponibles en el juego
        y las guarda en el atributo self._piezas.

        Return:
            None
        """

        with open(ARCHIVO_PIEZAS) as archivo:
            reader = csv.reader(archivo, delimiter=" ")

            for grupo_coordenadas in reader:
                pieza = grupo_coordenadas[-1]
                self._piezas[pieza] = []
                for coordenadas in grupo_coordenadas[:-2]:
                    self._piezas[pieza].append(tuple(map(eval, coordenadas.split(";"))))
