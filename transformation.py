class Transformation:
    def __init__(self, file_name_specifications, transformation_selector):
        self.file_name_specifications = file_name_specifications
        self.transformation_selector = transformation_selector
        self.transformation_translation_x = None
        self.transformation_translation_y = None
        self.transformation_translation_z = None
        self.transformation_rotation_x = None
        self.transformation_rotation_y = None
        self.transformation_rotation_z = None
        self.transformation_scale = None
        self.transformation_index = -1

    def read_transformation_specifications(self):
        with open(self.file_name_specifications) as file:
            lines = file.readlines()
            transformation_flag = 0
            transformation_transf_flag = 0
            for line in lines:
                parts = line.strip().split()
                if 'Transformation' in parts:
                    self.transformation_index += 1
                    transformation_transf_flag = 1
                    continue
                if transformation_transf_flag == 1 and '{' in parts:
                    transformation_flag = 1
                    continue
                if transformation_transf_flag == 1 and transformation_flag == 1 and 'T' in parts and self.transformation_selector == self.transformation_index:
                    self.transformation_translation_x = parts[1]
                    self.transformation_translation_y = parts[2]
                    self.transformation_translation_z = parts[3]
                    continue
                if transformation_transf_flag == 1 and transformation_flag == 1 and 'Rx' in parts and self.transformation_selector == self.transformation_index:
                    self.transformation_rotation_x = parts[1]
                    continue
                if transformation_transf_flag == 1 and transformation_flag == 1 and 'Ry' in parts and self.transformation_selector == self.transformation_index:
                    self.transformation_rotation_y = parts[1]
                    continue
                if transformation_transf_flag == 1 and transformation_flag == 1 and 'Rz' in parts and self.transformation_selector == self.transformation_index:
                    self.transformation_rotation_z = parts[1]
                    continue
                if transformation_transf_flag == 1 and transformation_flag == 1 and 'S' in parts and self.transformation_selector == self.transformation_index:
                    self.transformation_scale = parts[1]
                    continue
                if transformation_transf_flag == 1 and '}' in parts and self.transformation_selector == self.transformation_index:
                    transformation_transf_flag = 0
                    continue
        return self.transformation_rotation_x, self.transformation_rotation_y, self.transformation_rotation_z, self.transformation_scale, self.transformation_translation_x, self.transformation_translation_y, self.transformation_translation_z
    
    def display_transformation(self):
        transformation_rotation_x, transformation_rotation_y, transformation_rotation_z, transformation_scale, transformation_translation_x, transformation_translation_y, transformation_translation_z = self.read_transformation_specifications()
        print("transformation: ",transformation_rotation_x, transformation_rotation_y, transformation_rotation_z, transformation_scale, transformation_translation_x, transformation_translation_y, transformation_translation_z)
