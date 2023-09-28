import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 40
FONT = pygame.font.Font(None, 36)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Initial resolution value
resolution = 800

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Window with Buttons")

# Function to draw buttons
def draw_button(text, x, y, width, height, color):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button_rect)
    text_surface = FONT.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if open_button_rect.collidepoint(event.pos):
                print("Open Button Clicked")
            elif start_button_rect.collidepoint(event.pos):
                print("Start Button Clicked")
            elif inc_button_rect.collidepoint(event.pos):
                resolution += 10
            elif dec_button_rect.collidepoint(event.pos):
                resolution -= 10

    screen.fill((0, 0, 0))

    # Draw buttons
    open_button_rect = pygame.Rect(50, 200, BUTTON_WIDTH, BUTTON_HEIGHT)
    start_button_rect = pygame.Rect(175, 200, BUTTON_WIDTH, BUTTON_HEIGHT)
    inc_button_rect = pygame.Rect(300, 200, 40, BUTTON_HEIGHT)
    dec_button_rect = pygame.Rect(350, 200, 40, BUTTON_HEIGHT)

    draw_button("Open", *open_button_rect.topleft, BUTTON_WIDTH, BUTTON_HEIGHT, GRAY)
    draw_button("Start", *start_button_rect.topleft, BUTTON_WIDTH, BUTTON_HEIGHT, GRAY)
    draw_button("➕", *inc_button_rect.topleft, 40, BUTTON_HEIGHT, GRAY)
    draw_button("➖", *dec_button_rect.topleft, 40, BUTTON_HEIGHT, GRAY)

    # Draw the resolution value
    resolution_text = FONT.render(f"Resolution: {resolution}", True, WHITE)
    resolution_rect = resolution_text.get_rect(midtop=(WIDTH // 2, 50))
    screen.blit(resolution_text, resolution_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
