import pygame
import random

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snowflake Catching Game")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the number and size of snowflakes
NUM_SNOWFLAKES = 100
SNOWFLAKE_SIZE = 30

# Define the player size and speed
PLAYER_SIZE = 30
PLAYER_SPEED = 2

# Load the images and resize them
snowflake_image = pygame.image.load ('snowflake1.png')#.convert_alpha ()
snowflake_image = pygame.transform.scale (snowflake_image, (SNOWFLAKE_SIZE, SNOWFLAKE_SIZE))
player_image = pygame.image.load ('player.png')#.convert_alpha ()
player_image = pygame.transform.scale (player_image, (PLAYER_SIZE, PLAYER_SIZE))

# Create a list of snowflake objects with random positions and speeds
snowflakes = []
for i in range(NUM_SNOWFLAKES):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    speed = random.randint(1, 5)
    snowflakes.append([x, y, speed])

# Create a player object with initial position and direction
player = [400, 550, 0]

# Create a font object for rendering text
font = pygame.font.SysFont("Arial", 32)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check if the user presses the left or right arrow keys
        
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player[2] -= 0.005 # Set the player direction to left
        
    if keys[pygame.K_RIGHT]:
        player[2] += 0.005 # Set the player direction to right
        
    # Check if the user releases the left or right arrow keys
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player[2] = 0 # Stop the player movement
        
     # Clear screen
    screen.fill(BLACK)

    # Update and draw snowflakes
    for snowflake in snowflakes:
        # Move snowflake down by its speed
        snowflake[1] += 0.2#snowflake[2]
        # If snowflake reaches the bottom of the screen, reset its position and speed
        if snowflake[1] > 600:
            snowflake[0] = random.randint(0, 800)
            snowflake[1] = 0
            snowflake[2] = 0.2#random.randint(1, 5)
        # Draw snowflake as an image
        screen.blit (snowflake_image, (snowflake[0], snowflake[1]))

    # Update and draw player
    # Move player horizontally by its speed and direction
    player[0] += player[2]#PLAYER_SPEED * player[2]
    # Keep player within the screen boundaries
    if player[0] < PLAYER_SIZE / 2:
        player[0] = PLAYER_SIZE / 2
    if player[0] > 800 - PLAYER_SIZE / 2:
        player[0] = 800 - PLAYER_SIZE / 2
    # Draw player as an image
    screen.blit (player_image, (player[0] - PLAYER_SIZE / 2, player[1] - PLAYER_SIZE / 2))

    # Check for collisions between player and snowflakes
    for snowflake in snowflakes:
        # Calculate the distance between the center of the player and the center of the snowflake
        distance = ((player[0] - snowflake[0])**2 + (player[1] - snowflake[1])**2)**0.5
        # If the distance is less than the sum of their radii, they are colliding
        if distance < (PLAYER_SIZE / 2 + SNOWFLAKE_SIZE / 2):
            # Remove the snowflake from the list
            snowflakes.remove(snowflake)
            print(snowflakes)

    # Render and draw text for showing the number of remaining snowflakes and game over message
    text = font.render(f"Snowflakes left: {len(snowflakes)}", True, WHITE)
    screen.blit(text, (10, 10))
    if len(snowflakes) == 0:
        text = font.render("Game Over!", True, WHITE)
        screen.blit(text, (350, 250))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
