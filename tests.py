import unittest

from maze import Maze
from window import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):

        num_cols = 12
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def tests_maze_has_ent_and_ext(self):
        maze = Maze(0, 0, 10, 10, 10, 10)

        ent = maze.cells[0][0]
        ext = maze.cells[-1][-1]

        self.assertEqual(ent.has_left_wall, False)
        self.assertEqual(ext.has_right_wall, False)


if __name__ == "__main__":
    unittest.main()
