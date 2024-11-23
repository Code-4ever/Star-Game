import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Stars")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player properties
player_width = 50
player_height = 50
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 8

# Falling objects properties
star_width = 30
star_height = 30
star_speed = 5
stars = []

# Score
score = 0

# Font
font = pygame.font.Font(None, 36)

# Function to create a new star
def create_star():
    x = random.randint(0, SCREEN_WIDTH - star_width)
    y = random.randint(-100, -40)
    return {"x": x, "y": y}

# Add initial stars
for _ in range(5):
    stars.append(create_star())

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # Update stars
    for star in stars:
        star["y"] += star_speed
        # Check if a star hits the ground
        if star["y"] > SCREEN_HEIGHT:
            star["y"] = random.randint(-100, -40)
            star["x"] = random.randint(0, SCREEN_WIDTH - star_width)

        # Check collision with player
        if (player_x < star["x"] + star_width and
            player_x + player_width > star["x"] and
            player_y < star["y"] + star_height and
            player_y + player_height > star["y"]):
            score += 1
            star["y"] = random.randint(-100, -40)
            star["x"] = random.randint(0, SCREEN_WIDTH - star_width)

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Draw stars
    for star in stars:
        pygame.draw.rect(screen, RED, (star["x"], star["y"], star_width, star_height))

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
