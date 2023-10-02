import pygame
import sys

class Sphere:
    def __init__(self, file_name_specifications):
        self.file_name_specifications = file_name_specifications
        self.sphere_transf_index = None
        self.sphere_material_index = None

    def read_sphere_specifications(self):
        with open(self.file_name_specifications) as file:
            lines = file.readlines()
            sphere_material_flag = 0
            sphere_transf_flag = 0
            for line in lines:
                parts = line.strip().split()
                if 'Sphere' in parts:
                    sphere_transf_flag = 1
                    continue
                if sphere_transf_flag == 1 and '{' in parts:
                    sphere_material_flag = 1
                    continue
                if sphere_transf_flag == 1 and sphere_material_flag == 1:
                    self.sphere_transf_index = parts[0]
                    sphere_material_flag = 2
                    continue
                if sphere_transf_flag == 1 and sphere_material_flag == 2:
                    self.sphere_material_index = parts[0]
                    sphere_material_flag = 0
                    continue
                if sphere_transf_flag == 1 and '}' in parts:
                    sphere_transf_flag = 0
                    continue
        return self.sphere_transf_index, self.sphere_material_index
    
    def display_sphere(self):
        sphere_transf_index, sphere_material_index = self.read_sphere_specifications()
        print(sphere_transf_index, sphere_material_index)
