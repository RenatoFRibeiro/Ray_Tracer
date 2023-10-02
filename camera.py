import pygame
import sys

class Camera:
    def __init__(self, file_name_specifications):
        self.file_name_specifications = file_name_specifications
        self.box_transf_index = None
        self.box_distance = None
        self.box_fov = None

    def read_camera_specifications(self):
        with open(self.file_name_specifications) as file:
            lines = file.readlines()
            box_flag = 0
            box_distance_flag = 0
            box_fov_flag = 0
            box_transf_flag = 0
            for line in lines:
                parts = line.strip().split()
                if 'Box' in parts:
                    box_flag = 1
                    continue
                if box_flag == 1 and '{' in parts:
                    box_transf_flag = 1
                    continue
                if box_transf_flag == 1 and box_flag == 1:
                    self.box_transf_index = parts[0]
                    box_distance_flag = 1
                    continue
                if box_transf_flag == 1 and box_distance_flag == 1 and box_flag == 1:
                    self.box_distance = parts[0]
                    box_fov_flag = 1
                    continue
                if box_transf_flag == 1 and box_distance_flag == 1 and box_flag == 1 and box_fov_flag == 1:
                    self.box_fov = parts[0]
                    box_fov_flag = 0
                    box_distance_flag = 0
                    box_tranf_flag = 0
                    continue
            # No need to print here
        return self.box_transf_index, self.box_distance, self.box_fov
    
    def display_box(self):
        box_transf_index, box_distance, box_fov = self.read_camera_specifications()
        print(box_transf_index, box_distance, box_fov)
