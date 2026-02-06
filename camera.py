class Camera:
    def __init__(self, cell_size=50):
        self.cell_size = cell_size
        self.x = 0.0
        self.y = 0.0
    
    def screen_to_cell(self, screen_x, screen_y):
        cell_x = (screen_x // self.cell_size) + self.x
        cell_y = (screen_y // self.cell_size) + self.y
        return cell_x, cell_y
    def cell_to_screen(self, cell_x, cell_y):
        screen_x = (cell_x - self.x) * self.cell_size
        screen_y = (cell_y - self.y) * self.cell_size
        return int(screen_x), int(screen_y)
    def zoom_in(self):
        if self.cell_size > 1:
            self.cell_size = int(self.cell_size / 1.5) 
    def zoom_out(self):
        self.cell_size = int(self.cell_size * 1.5)
    def move(self, x, y):
        self.x += x
        self.y += y