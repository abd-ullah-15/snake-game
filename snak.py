import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
BLOCK_SIZE = 20
SPEED = 10

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def game_loop():
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0

    snake = []
    length = 1

    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, BLOCK_SIZE

        x += dx
        y += dy

        # Boundary check
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            running = False

        snake.append([x, y])
        if len(snake) > length:
            del snake[0]

        # Self collision
        for block in snake[:-1]:
            if block == [x, y]:
                running = False

        # Food
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        if x == food_x and y == food_y:
            length += 1
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

        draw_snake(snake)
        pygame.display.update()
        clock.tick(SPEED)

    pygame.quit()

game_loop()