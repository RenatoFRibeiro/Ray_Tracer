import pygame
import sys
import tkinter as tk
from tkinter import filedialog
from image import SceneImage
from sphere import Sphere
from box import Box

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 40
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 300  # The size of the image display window
FONT = pygame.font.Font(None, 36)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
file_path=''
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

# Function to open a file dialog
def open_file_dialog():
    global file_path  # Declare that we want to use the global variable
    root = tk.Tk()
    root.withdraw()  # Hide the tkinter root window
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected File:", file_path)
        return file_path # Load the selected file

# Calculate button positions responsively
button_margin = 20
button_start_x = (WIDTH - 2 * BUTTON_WIDTH - 2 * button_margin) // 2
button_open_x = button_start_x + BUTTON_WIDTH + button_margin
button_y = HEIGHT - BUTTON_HEIGHT - 20

# Create a Pygame surface for displaying the scene
image_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

# Main game loop
running = True
scene = None  # Variable to store the loaded image
start_flag = 0 # Variable to render the image only on start
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if open_button_rect.collidepoint(event.pos):
                start_flag = 0
                scene = open_file_dialog() 
                print("Open Button Clicked")
                pygame.display.set_mode((WIDTH, HEIGHT))  # Set focus back on the Pygame window
            elif start_button_rect.collidepoint(event.pos):
                start_flag = 1
                print("Start Button Clicked")
            elif inc_button_rect.collidepoint(event.pos):
                resolution += 10
                print("Increase Button Clicked")
            elif dec_button_rect.collidepoint(event.pos):
                resolution -= 10
                print("Decrease Button Clicked")

    screen.fill((0, 50, 0))

    # Draw buttons
    open_button_rect = pygame.Rect(button_open_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
    start_button_rect = pygame.Rect(button_start_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
    inc_button_rect = pygame.Rect(10, button_y, 40, BUTTON_HEIGHT)
    dec_button_rect = pygame.Rect(60, button_y, 40, BUTTON_HEIGHT)

    draw_button("Open", *open_button_rect.topleft, BUTTON_WIDTH, BUTTON_HEIGHT, GRAY)
    draw_button("Start", *start_button_rect.topleft, BUTTON_WIDTH, BUTTON_HEIGHT, GRAY)
    draw_button("+", *inc_button_rect.topleft, 40, BUTTON_HEIGHT, GRAY)
    draw_button("-", *dec_button_rect.topleft, 40, BUTTON_HEIGHT, GRAY)

    # Draw the resolution value
    resolution_text = FONT.render(f"Resolution: {resolution}", True, WHITE)
    resolution_rect = resolution_text.get_rect(midtop=(WIDTH // 2, 50))
    screen.blit(resolution_text, resolution_rect)

    if scene and start_flag == 1:
        # Create an instance of the PygameImageDisplay class
        pygame_image_display = SceneImage(file_path)
        pygame_sphere_display = Sphere(file_path)
        pygame_box_display = Box(file_path)
        # Display the image
        pygame_image_display.display_image()
        pygame_sphere_display.display_sphere()
        pygame_box_display.display_box()

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
