from window import Window
from maze import Maze


def main():
    window = Window(800, 600)

    maze = Maze(5, 5, 30, 30, 20, 20, window)
    maze.solve()

    window.wait_for_close()


if __name__ == '__main__':
    main()
