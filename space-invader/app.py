import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader (Vertical Enemy Movement)")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Player settings
player_width = 100
player_height = 10
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 7

# Enemy settings
enemy_radius = 20
enemy_x = random.randint(50, WIDTH - 50)
enemy_y = 50
enemy_speed = 4

# Game variables
score = 0
lives = 3
WINNING_SCORE = 10
running = True

# Game loop
while running:
    screen.fill(BLACK)  # Clear screen
    pygame.time.delay(20)  # Frame rate control

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Enemy movement (falls downwards)
    enemy_y += enemy_speed

    # Check if enemy reaches the player
    if enemy_y >= HEIGHT - 50:
        if player_x < enemy_x < player_x + player_width:
            score += 1  # Player catches the enemy, increase score
        else:
            lives -= 1  # Player misses, lose a life
        enemy_x = random.randint(50, WIDTH - 50)  # Reset enemy position
        enemy_y = 50

    # **Winning Condition**
    if score >= WINNING_SCORE:
        screen.fill(BLACK)
        win_text = font.render("You Win! Press Q to Quit", True, YELLOW)
        screen.blit(win_text, (WIDTH // 2 - 150, HEIGHT // 2))
        pygame.display.update()

        # Wait for player to quit
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    waiting = False
                    running = False

    # **Game Over Condition**
    if lives <= 0:
        screen.fill(BLACK)
        game_over_text = font.render("Game Over! Press Q to Quit", True, YELLOW)
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
        pygame.display.update()

        # Wait for player to quit
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    waiting = False
                    running = False

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Draw enemy
    pygame.draw.circle(screen, RED, (enemy_x, enemy_y), enemy_radius)

    # Display Score and Lives
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))

    pygame.display.update()  # Update screen

pygame.quit()