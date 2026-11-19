import pygame
import sys

#1, Start pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame .time.Clock()

ball_x = 400
ball_y = 300
ball_speed = 5
ball_radius = 25

rect_x = 400
rect_y = 300
rect_width = 100
rect_height = 200
wall_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

running = True
while running == True:
    #Check for quitting 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #get keys currently being pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT]:
        ball_x += ball_speed
    if keys[pygame.K_UP]:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN]:
        ball_y += ball_speed

    #stopping the ball at walls (we'll do this later)
    if ball_x < ball_radius:
        ball_x = ball_radius
    elif ball_x > WIDTH - ball_radius:
        ball_x = WIDTH - ball_radius

    if ball_y < ball_radius:
        ball_y = ball_radius
    elif ball_y > HEIGHT - ball_radius:
        ball_y = HEIGHT - ball_radius

    if (ball_x + ball_radius > wall_rect.left and ball_x - ball_radius < wall_rect.right and ball_y + ball_radius > wall_rect.top and ball_y - ball_radius < wall_rect.bottom):
        #collision dectected, move th eball back to its previous position
        if keys[pygame.K_LEFT]:
            ball_x = wall_rect.right - ball_radius
        if keys[pygame.K_RIGHT]:
            ball_x = wall_rect.right + ball_radius
        if keys[pygame.K_UP]:
            ball_y = wall_rect.right + ball_radius
        if keys[pygame.K_DOWN]:
            ball_y = wall_rect.right - ball_radius

        

    #clear the screen
    screen.fill((20, 20, 50))

    # draw the ball at its new position
    pygame.draw.circle(screen,(255, 0, 0), (ball_x, ball_y), ball_radius)

    #update the display (60 FPS)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.quit()