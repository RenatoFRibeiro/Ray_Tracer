import pygame
import sys
import tkinter as tk
from tkinter import filedialog
from image import SceneImage
from sphere import Sphere
from box import Box
from light import Light
from camera import Camera
from material import Material
from transformation import Transformation
from triangles import Triangles

pygame.init()

WIDTH, HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 40
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 300
FONT = pygame.font.Font(None, 36)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
file_path=''

resolution = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Window with Buttons")

def draw_button(text, x, y, width, height, color):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button_rect)
    text_surface = FONT.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

def open_file_dialog():
    global file_path
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected File:", file_path)
        return file_path

button_margin = 20
button_start_x = (WIDTH - 2 * BUTTON_WIDTH - 2 * button_margin) // 2
button_open_x = button_start_x + BUTTON_WIDTH + button_margin
button_y = HEIGHT - BUTTON_HEIGHT - 20

image_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True
scene = None
start_flag = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if open_button_rect.collidepoint(event.pos):
                start_flag = 0
                scene = open_file_dialog() 
                print("Open Button Clicked")
                pygame.display.set_mode((WIDTH, HEIGHT))
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

    open_button_rect = pygame.Rect(button_open_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
    start_button_rect = pygame.Rect(button_start_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
    inc_button_rect = pygame.Rect(10, button_y, 40, BUTTON_HEIGHT)
    dec_button_rect = pygame.Rect(60, button_y, 40, BUTTON_HEIGHT)

    draw_button("Open", *open_button_rect.topleft, BUTTON_WIDTH, BUTTON_HEIGHT, GRAY)
    draw_button("Start", *start_button_rect.topleft, BUTTON_WIDTH, BUTTON_HEIGHT, GRAY)
    draw_button("+", *inc_button_rect.topleft, 40, BUTTON_HEIGHT, GRAY)
    draw_button("-", *dec_button_rect.topleft, 40, BUTTON_HEIGHT, GRAY)

    resolution_text = FONT.render(f"Resolution: {resolution}", True, WHITE)
    resolution_rect = resolution_text.get_rect(midtop=(WIDTH // 2, 50))
    screen.blit(resolution_text, resolution_rect)

    if scene and start_flag == 1:
        pygame_image_display = SceneImage(file_path)
        pygame_sphere_display = Sphere(file_path)
        pygame_box_display = Box(file_path)
        pygame_light_display = Light(file_path)
        pygame_camera_display = Camera(file_path)
        pygame_material_by_index_display = Material(file_path, 1)
        pygame_transformation_by_index_display = Transformation(file_path, 1)
        pygame_triangles_by_index_display = Triangles(file_path, 1)

        pygame_image_display.display_image()
        pygame_sphere_display.display_sphere()
        pygame_box_display.display_box()
        pygame_light_display.display_light()
        pygame_camera_display.display_camera()
        pygame_material_by_index_display.display_material()
        pygame_transformation_by_index_display.display_transformation()
        pygame_triangles_by_index_display.display_triangles()
        break
    pygame.display.flip()

pygame.quit()
sys.exit()
