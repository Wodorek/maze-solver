from line import Line
from point import Point
import math


class Cell:
    def __init__(self, window, p1, p2):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True

        self._x1, self._y1 = min(p1.x, p2.x), min(p1.y, p2.y)
        self._x2, self._y2 = max(p1.x, p2.x), max(p1.y, p2.y)

        self._win = window

    def draw(self, fill_color):
        if self.has_left_wall:
            Line(Point(self._x1, self._y1), Point(self._x1, self._y2)).draw(
                self._win.canvas, fill_color)
        if self.has_bottom_wall:
            Line(Point(self._x1, self._y2), Point(self._x2, self._y2)).draw(
                self._win.canvas, fill_color)
        if self.has_top_wall:
            Line(Point(self._x1, self._y1), Point(self._x2, self._y1)).draw(
                self._win.canvas, fill_color)
        if self.has_right_wall:
            Line(Point(self._x2, self._y1), Point(self._x2, self._y2)).draw(
                self._win.canvas, fill_color)
