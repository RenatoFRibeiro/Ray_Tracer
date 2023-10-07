from image import SceneImage
from sphere import Sphere
from box import Box
from light import Light
from camera import Camera
from material import Material
from transformation import Transformation
from triangles import Triangles

file_path='COSIG_RayTracer/src/scene.txt'

class Parser:
    def __init__(self, file_name_specifications):
        self.triangle_counter = -1
        self.file_name_specifications = file_name_specifications
        self.pygame_image_display = SceneImage(file_path)
        self.pygame_sphere_display = Sphere(file_path)
        self.pygame_box_display = Box(file_path)
        self.pygame_light_display = Light(file_path)
        self.pygame_camera_display = Camera(file_path)

    def parseScene(self):
        with open(self.file_name_specifications) as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split()
                if 'Image' in parts:
                    self.pygame_image_display.display_image()
                    continue
                elif 'Light' in parts:
                    self.pygame_light_display.display_light()
                    continue
                elif 'Camera' in parts:
                    self.pygame_camera_display.display_camera()
                    #self.
                    continue
                elif 'Box' in parts:
                    self.pygame_box_display.display_box()
                    continue
                elif 'Sphere' in parts:
                    self.pygame_sphere_display.display_sphere()
                    continue
                elif 'Triangles' in parts:
                    self.triangle_counter += 1
                    self.pygame_triangles_by_index_display = Triangles(file_path, self.triangle_counter)
                    self.pygame_triangles_by_index_display.display_triangles()
                    continue
def main():
    parser = Parser(file_path)
    parser.parseScene()

if __name__ == "__main__":
    main()
