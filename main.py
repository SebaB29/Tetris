import graphics.gamelib as gamelib
from src.tetris import Tetris


def main():
    tetris = Tetris()
    tetris.transcurso_del_juego()
    volver_a_jugar = tetris.final_del_juego()
    if volver_a_jugar:
        main()


if __name__ == "__main__":
    gamelib.init(main)
