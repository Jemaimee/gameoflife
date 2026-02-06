import pygame



class Render():

    def __init__(self, camera):
        self.screen_width = 1000
        self.screen_height = 1000
        self.camera = camera

        pygame.init()
        self.screen = pygame.display.set_mode((1000, 1000))

    def draw_grid(self):
        
        for x in range(self.screen_width // self.camera.cell_size):
            pygame.draw.line(self.screen, "#747474", start_pos=((x * self.camera.cell_size), 0), end_pos=((x * self.camera.cell_size), self.screen_height))
        
        for y in range(self.screen_height // self.camera.cell_size):
            pygame.draw.line(self.screen, "#747474", start_pos=(0, (y * self.camera.cell_size)), end_pos=(self.screen_width, (y * self.camera.cell_size)))

    def draw_cells(self, alive_cells):
        for cell in alive_cells:
            screen_coordinate = self.camera.cell_to_screen(*cell)
            pygame.draw.rect(self.screen, "#C7C7C7", ((screen_coordinate), (self.camera.cell_size, self.camera.cell_size)))

    def draw(self, alive_cells):
        self.screen.fill("#121212")
        self.draw_cells(alive_cells)
        self.draw_grid()
        pygame.display.flip()