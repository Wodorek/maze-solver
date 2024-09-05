from line import Line
from point import Point


class Cell:
    def __init__(self, p1, p2, window=None):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True

        self._x1, self._y1 = min(p1.x, p2.x), min(p1.y, p2.y)
        self._x2, self._y2 = max(p1.x, p2.x), max(p1.y, p2.y)

        self._win = window

    def draw(self, fill_color):
        left_color = fill_color if self.has_left_wall else 'white'
        right_color = fill_color if self.has_right_wall else 'white'
        top_color = fill_color if self.has_top_wall else 'white'
        bottom_color = fill_color if self.has_bottom_wall else 'white'

        if not self._win:
            return

# left wall
        Line(Point(self._x1, self._y1), Point(self._x1, self._y2)).draw(
            self._win.canvas, left_color)
# bottom wall
        Line(Point(self._x1, self._y2), Point(self._x2, self._y2)).draw(
            self._win.canvas, bottom_color)
# top wall
        Line(Point(self._x1, self._y1), Point(self._x2, self._y1)).draw(
            self._win.canvas, top_color)
# right wall
        Line(Point(self._x2, self._y1), Point(self._x2, self._y2)).draw(
            self._win.canvas, right_color)

    def draw_move(self, target, undo=False):

        color = 'grey' if undo else 'red'

        self_center_x = (self._x1 + self._x2) / 2
        self_center_y = (self._y1 + self._y2) / 2

        target_center_x = (target._x1 + target._x2) / 2
        target_center_y = (target._y1 + target._y2) / 2

        Line(Point(self_center_x, self_center_y), Point(
            target_center_x, target_center_y)).draw(self._win.canvas, color)
