import time
from cell import Cell
from point import Point


class Maze:

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self._create_cells()

    def _create_cells(self):
        matrix = []

        for j in range(0, self.num_cols):
            row = []

            for i in range(0, self.num_rows):
                row.append(Cell(self.win,
                                Point(self.x1 + i *
                                      self.cell_size_x, self.y1 + self.cell_size_y * j),
                                Point(self.x1 + (i+1) *
                                      self.cell_size_x, self.y1 + self.cell_size_y + self.cell_size_y * j+1)))
            matrix.append(row)

        self.cells = matrix

        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                self._draw_cell(i, j)

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _draw_cell(self, i, j):

        cell = self.cells[i][j]
        cell.draw('black')

        self._animate()
