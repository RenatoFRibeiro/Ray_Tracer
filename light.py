class Light:
    def __init__(self, file_name_specifications):
        self.file_name_specifications = file_name_specifications
        self.light_transf_index = None
        self.light_intensity = None

    def read_light_specifications(self):
        with open(self.file_name_specifications) as file:
            lines = file.readlines()
            light_intensity_flag = 0
            light_transf_flag = 0
            for line in lines:
                parts = line.strip().split()
                if 'Light' in parts:
                    light_transf_flag = 1
                    continue
                if light_transf_flag == 1 and '{' in parts:
                    light_intensity_flag = 1
                    continue
                if light_transf_flag == 1 and light_intensity_flag == 1:
                    self.light_transf_index = parts[0]
                    light_intensity_flag = 2
                    continue
                if light_transf_flag == 1 and light_intensity_flag == 2:
                    self.light_intensity = tuple(int(float(val) * 255) for val in parts)
                    light_intensity_flag = 0
                    continue
                if light_transf_flag == 1 and '}' in parts:
                    light_transf_flag = 0
                    continue
        return self.light_transf_index, self.light_intensity
    
    def display_light(self):
        light_transf_index, light_intensity = self.read_light_specifications()
        print("Light: ",light_transf_index, light_intensity)
