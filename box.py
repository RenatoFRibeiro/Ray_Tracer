import pygame
import sys

class Box:
    def __init__(self, file_name_specifications):
        self.file_name_specifications = file_name_specifications
        self.box_transf_index = None
        self.box_material_index = None

    def read_box_specifications(self):
        with open(self.file_name_specifications) as file:
            lines = file.readlines()
            box_material_flag = 0
            box_transf_flag = 0
            for line in lines:
                parts = line.strip().split()
                if 'Box' in parts:
                    box_transf_flag = 1
                    continue
                if box_transf_flag == 1 and '{' in parts:
                    box_material_flag = 1
                    continue
                if box_transf_flag == 1 and box_material_flag == 1:
                    self.box_transf_index = parts[0]
                    box_material_flag = 2
                    continue
                if box_transf_flag == 1 and box_material_flag == 2:
                    self.box_material_index = parts[0]
                    box_material_flag = 0
                    continue
                if box_transf_flag == 1 and '}' in parts:
                    box_transf_flag = 0
                    continue
            # No need to print here
        return self.box_transf_index, self.box_material_index
    
    def display_box(self):
        box_transf_index, box_material_index = self.read_box_specifications()
        print(box_transf_index, box_material_index)
