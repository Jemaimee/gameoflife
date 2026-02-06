import pygame



class Render():

    def __init__(self, camera):
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 1000
        self.SQUARE_SIZE = 50
        self.camera = camera

        pygame.init()
        self.screen = pygame.display.set_mode((1000, 1000))

    def draw_grid(self):
        
        for x in range(self.SCREEN_WIDTH // self.SQUARE_SIZE):
            pygame.draw.line(self.screen, "#747474", start_pos=((x * self.SQUARE_SIZE), 0), end_pos=((x * self.SQUARE_SIZE), self.SCREEN_HEIGHT))
        
        for y in range(self.SCREEN_HEIGHT // self.SQUARE_SIZE):
            pygame.draw.line(self.screen, "#747474", start_pos=(0, (y * self.SQUARE_SIZE)), end_pos=(self.SCREEN_WIDTH, (y * self.SQUARE_SIZE)))

    def draw_cells(self, alive_cells):
        for cell in alive_cells:
            screen_coordinate = self.camera.cell_to_screen(*cell)
            pygame.draw.rect(self.screen, "#C7C7C7", ((screen_coordinate), (self.SQUARE_SIZE, self.SQUARE_SIZE)))

    def draw(self, alive_cells):
        self.screen.fill("#121212")
        self.draw_cells(alive_cells)
        self.draw_grid()
        pygame.display.flip()