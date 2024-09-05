import time
import random
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
        win=None,
        seed=None
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
        if seed:
            self.seed = random.seed(seed)

        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        matrix = []

        for j in range(0, self.num_cols):
            row = []

            for i in range(0, self.num_rows):
                row.append(Cell(
                    Point(self.x1 + i *
                          self.cell_size_x, self.y1 + self.cell_size_y * j),
                    Point(self.x1 + (i+1) *
                          self.cell_size_x, self.y1 + self.cell_size_y + self.cell_size_y * j+1), self.win))
            matrix.append(row)

        self.cells = matrix

        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()

    def _animate(self):
        if not self.win:
            return
        self.win.redraw()
        time.sleep(0.01)

    def _draw_cell(self, i, j):

        cell = self.cells[i][j]
        cell.draw('black')

        self._animate()

    def _break_entrance_and_exit(self):
        ent = self.cells[0][0]
        ext = self.cells[-1][-1]

        ent.has_left_wall = False
        ext.has_right_wall = False

        self._draw_cell(0, 0)
        self._draw_cell(-1, -1)

    def _unvisited_neighbors(self, i, j):
        neigbors = []

        # left
        if j-1 >= 0:
            cell = self.cells[i][j-1]
            if not cell.visited:
                neigbors.append(('left', i, j-1))

        # top
        if i-1 >= 0:
            cell = self.cells[i-1][j]
            if not cell.visited:
                neigbors.append(('top', i-1, j))

        # right
        if j+1 < self.num_cols:
            cell = self.cells[i][j+1]
            if not cell.visited:
                neigbors.append(('right', i, j+1))
        # bottom
        if i+1 < self.num_rows:
            cell = self.cells[i+1][j]
            if not cell.visited:
                neigbors.append(('bot', i+1, j))

        return neigbors

    def _break_walls_r(self, i, j):

        cell = self.cells[i][j]
        cell.visited = True

        while True:
            neighbors = self._unvisited_neighbors(i, j)
            if len(neighbors) == 0:
                self._draw_cell(i, j)
                return

            select = random.randrange(0, len(neighbors))
            print('nn', neighbors)
            move_dir, x, y = neighbors[select]
            moving_to = self.cells[x][y]

            if move_dir == 'left':
                cell.has_left_wall = False
                moving_to.has_right_wall = False

            if move_dir == 'top':
                cell.has_top_wall = False
                moving_to.has_bottom_wall = False

            if move_dir == 'right':
                cell.has_right_wall = False
                moving_to.has_left_wall = False

            if move_dir == 'bot':
                cell.has_bottom_wall = False
                moving_to.has_top_wall = False

            self._break_walls_r(x, y)

    def _reset_cells_visited(self):

        for row in self.cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0, self.cells[-1][-1])

    def _solve_r(self, i, j, end):
        self._animate()

        curr_cell = self.cells[i][j]
        curr_cell.visited = True

        if self.cells[i][j] == end:
            return True

        neighbors = self._unvisited_neighbors(i, j)

        for neighbor in neighbors:
            move_dir, x, y = neighbor

            moving_to = self.cells[x][y]

            if move_dir == 'left':
                if not curr_cell.has_left_wall and not moving_to.has_right_wall:
                    curr_cell.draw_move(moving_to)
                    s = self._solve_r(x, y, end)
                    if s:
                        return True
                    if not s:
                        curr_cell.draw_move(moving_to, True)

            if move_dir == 'right':
                if not curr_cell.has_right_wall and not moving_to.has_left_wall:
                    curr_cell.draw_move(moving_to)
                    s = self._solve_r(x, y, end)
                    if s:
                        return True
                    if not s:
                        curr_cell.draw_move(moving_to, True)

            if move_dir == 'top':
                if not curr_cell.has_top_wall and not moving_to.has_bottom_wall:
                    curr_cell.draw_move(moving_to)
                    s = self._solve_r(x, y, end)
                    if s:
                        return True
                    if not s:
                        curr_cell.draw_move(moving_to, True)

            if move_dir == 'bot':
                if not curr_cell.has_bottom_wall and not moving_to.has_top_wall:
                    curr_cell.draw_move(moving_to)
                    s = self._solve_r(x, y, end)
                    if s:
                        return True
                    if not s:
                        curr_cell.draw_move(moving_to, True)
