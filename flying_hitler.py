import pygame
import sys
import random

pygame.init()

# Window size (adjust as needed)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Flappy Hitler vs. Stalin')
clock = pygame.time.Clock()

# Load images - PNGs with transparent background recommended!
background_img = pygame.transform.scale(pygame.image.load("C:\\Users\\hp\\Downloads\\ww2.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
bird_img = pygame.transform.scale(pygame.image.load("C:\\Users\\hp\\Downloads\\adolf hitler.png").convert_alpha(), (50,50))
pipe_img = pygame.transform.scale(pygame.image.load("C:\\Users\\hp\\Downloads\\joseph stalin.png").convert_alpha(), (70,80))

# Bird variables
bird_x = 170
bird_y = WINDOW_HEIGHT // 2
bird_movement = 0
gravity = 0.5
flap_power = -8

# Pipe variables
pipe_speed = 3.5
pipe_gap = 200
pipe_frequency = 1500  # ms between pipe generations
pipes = []

last_pipe_time = pygame.time.get_ticks() - pipe_frequency

def create_pipe_pair():
    y_pos = random.randint(100, WINDOW_HEIGHT-100-pipe_gap)
    top_rect = pipe_img.get_rect(midbottom=(WINDOW_WIDTH+40, y_pos))
    bot_rect = pipe_img.get_rect(midtop=(WINDOW_WIDTH+40, y_pos+pipe_gap))
    return (top_rect, bot_rect)

def move_pipes(pipes):
    # Move all pipe rects leftwards and remove off-screen pipes
    updated = []
    for top_rect, bot_rect in pipes:
        top_rect.x -= pipe_speed
        bot_rect.x -= pipe_speed
        if top_rect.right > 0:
            updated.append((top_rect, bot_rect))
    return updated

def draw_pipes(pipes):
    # Draw Stalin's face for pipes, flipped at top
    for top_rect, bot_rect in pipes:
        window.blit(pygame.transform.flip(pipe_img, False, True), top_rect)  # top pipe flipped
        window.blit(pipe_img, bot_rect)                                     # bottom pipe normal

def check_collision(bird_rect, pipes):
    if bird_rect.top <= 0 or bird_rect.bottom >= WINDOW_HEIGHT:
        return True
    for top_rect, bot_rect in pipes:
        if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bot_rect):
            return True
    return False

# Main loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_movement = flap_power

    # Bird physics
    bird_movement += gravity
    bird_y += bird_movement

    # Bird rect
    bird_rect = bird_img.get_rect(center=(bird_x, bird_y))

    # Create new pipes at set intervals
    now = pygame.time.get_ticks()
    if now - last_pipe_time > pipe_frequency:
        pipes.append(create_pipe_pair())
        last_pipe_time = now

    pipes = move_pipes(pipes)

    # Screen drawing
    window.blit(background_img, (0,0))
    draw_pipes(pipes)
    window.blit(bird_img, bird_rect)

    if check_collision(bird_rect, pipes):
        print('Game Over!')
        running = False

    pygame.display.update()

pygame.quit()
sys.exit()
