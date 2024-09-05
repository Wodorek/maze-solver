from window import Window
from point import Point
from line import Line


def main():
    window = Window(800, 600)

    p1 = Point(200, 300)
    p2 = Point(300, 400)
    p3 = Point(500, 500)

    window.draw_line(Line(p1, p2), 'black')
    window.draw_line(Line(p2, p3), 'red')

    window.wait_for_close()


if __name__ == '__main__':
    main()
