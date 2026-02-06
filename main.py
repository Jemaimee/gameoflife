import pygame
from datetime import datetime, timedelta
from map import Render
from cells import Game
from camera import Camera

game = Game()
camera = Camera()
render = Render(camera)


pygame.init()
clock = pygame.time.Clock()
running = True
paused = True
last_advance = datetime.now()
cooldown = 1

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            cell_coordinate = camera.screen_to_cell(*event.pos)
            if cell_coordinate not in game.alive_cells:
                game.add_cell(cell_coordinate)
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            cell_coordinate = camera.screen_to_cell(*event.pos)
            if cell_coordinate not in game.alive_cells:
                game.add_cell(cell_coordinate)
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                camera.y -= 1
            if keys[pygame.K_DOWN]:
                camera.y += 1
            if keys[pygame.K_LEFT]:
                camera.x -= 1
            if keys[pygame.K_RIGHT]:
                camera.x += 1
            if keys[pygame.K_SPACE]:
                if paused:
                    paused = False
                elif not paused:
                    paused = True
            if keys[pygame.K_e]:
                cooldown += 0.1
            if keys[pygame.K_a]:
                cooldown -= 0.1
    
    now = datetime.now()
    timedelta = now - last_advance
    if timedelta.total_seconds() > cooldown and not paused:
        game.get_next_state()
        last_advance = datetime.now()
        

    render.draw(game.alive_cells)
    clock.tick(120)

pygame.quit()