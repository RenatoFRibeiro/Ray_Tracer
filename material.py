class Material:
    def __init__(self, file_name_specifications, material_counter):
        self.file_name_specifications = file_name_specifications
        self.material_color = None
        self.material_ambient = None
        self.material_difuse = None
        self.material_spec = None
        self.material_refr = None
        self.material_refr_index = None
        self.material_counter = material_counter

    def read_material_specifications(self):
        with open(self.file_name_specifications) as file:
            lines = file.readlines()
            material_flag = 0
            material_flag_2 = 0
            material_selector = -1
            for line in lines:
                parts = line.strip().split()
                if 'Material' in parts:
                    material_selector+=1
                    material_flag_2 = 1
                    continue
                if material_flag_2 == 1 and '{' in parts and material_selector == self.material_counter:
                    material_flag = 1
                    continue
                if material_flag_2 == 1 and material_flag == 1 and material_selector == self.material_counter:
                    self.material_color = tuple(int(float(val) * 255) for val in parts)
                    material_flag = 2
                    continue
                if material_flag_2 == 1 and material_flag == 2 and material_selector == self.material_counter:
                    self.material_ambient = parts[0]
                    self.material_difuse = parts[1]
                    self.material_spec = parts[2]
                    self.material_refr = parts[3]
                    self.material_refr_index = parts[4]
                    material_flag = 0
                    continue
                if material_flag_2 == 1 and '}' in parts and material_selector == self.material_counter:
                    material_flag_2 = 0
                    continue
        return self.material_color, self.material_ambient, self.material_difuse, self.material_spec, self.material_refr, self.material_refr_index
    
    def display_material(self):
        material_color, material_ambient, material_difuse, material_spec, material_refr, material_refr_index = self.read_material_specifications()
        print("Material: ",material_color, material_ambient, material_difuse, material_spec, material_refr, material_refr_index)
