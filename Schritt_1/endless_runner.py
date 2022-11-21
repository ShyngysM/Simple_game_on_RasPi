import pygame as pg 
import random

pg.init()

#game constants
white = (255, 255, 255)
black = (0, 0, 0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
WIDTH = 450
HEIGHT = 600

#game variables
score = 0
player_x = 200
player_y = 450
x_change = 0
obstacle_speed = 2
obstacle_x = 0
obstacle_y = -20
active = False

screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption('Endless Runner')
background = black
fps = 60
font = pg.font.Font('freesansbold.ttf', 16)
timer = pg.time.Clock()

running = True
# Start game
while running:
    timer.tick(fps)
    screen.fill(background)
    score_text = font.render(f'Score: {score}', True, white, black)
    screen.blit(score_text, (10, 10))
    player = pg.draw.rect(screen, white, [player_x, player_y, 30, 30])
    obstacle0 = pg.draw.rect(screen, red, [obstacle_x, obstacle_y,  20, 20])

# Events -> Press buttons
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

# Change from here!
        if event.type == pg.KEYDOWN and active:
            if event.key == pg.K_RIGHT:
                x_change = 2
            if event.key == pg.K_LEFT:
                x_change = -2
        elif event.type == pg.KEYDOWN and not active:
            if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                player_x = 200 
                score = 0
                obstacle_speed = 3
                active = True
# Change till here!

# Create and handle obstacles
    if active:
        obstacle_y += obstacle_speed
        if obstacle_y > HEIGHT:
            obstacle_y = random.randint(-400, -250)
            score += 1
            obstacle_x = random.randint(0, WIDTH - 20)
            if score % 5 == 0 :
                obstacle_speed += 4
        if player.colliderect(obstacle0):
            active = False
            x_change = 0

# Player movement 
    if 0 <= player_x <= WIDTH - 30:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - 30:
        player_x = WIDTH - 30

    pg.display.flip()
pg.quit()
