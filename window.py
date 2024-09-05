from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.root = Tk()
        self.root.title = 'Maze solver'
        self.root.protocol('WM_DELETE_WINDOW', self.close)
        self.canvas = Canvas(height=self.height, width=self.width)
        self.canvas.pack()
        self.window_running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.window_running = True

        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False
