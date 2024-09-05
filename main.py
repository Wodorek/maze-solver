from window import Window
from point import Point
from line import Line
from cell import Cell


def main():
    window = Window(800, 600)

    p1 = Point(5, 5)
    p2 = Point(105, 105)
    p3 = Point(405, 5)
    p4 = Point(505, 105)
    cell = Cell(window, p1, p2)
    cell.draw('black')
    cell2 = Cell(window, p3, p4)
    cell2.draw('red')

    cell.draw_move(cell2, True)

    window.wait_for_close()


if __name__ == '__main__':
    main()
