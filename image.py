class SceneImage:
    def __init__(self, file_name_specifications):
        self.file_name_specifications = file_name_specifications
        self.width = None
        self.height = None
        self.background_color = None

    def read_image_specifications(self):
        with open(self.file_name_specifications) as file:
            lines = file.readlines()
            image_settings = 0
            image_flag = 0
            for line in lines:
                parts = line.strip().split()
                if 'Image' in parts:
                    image_flag = 1
                    continue
                if image_flag == 1 and '{' in parts:
                    image_settings = 1
                    continue
                if image_flag == 1 and image_settings == 1:
                    self.width = int(parts[0])
                    self.height = int(parts[1])
                    image_settings = 2
                    continue
                if image_flag == 1 and image_settings == 2:
                    image_settings = 0
                    self.background_color = tuple(int(float(val) * 255) for val in parts)
                if image_flag == 1 and '}' in parts:
                    image_flag = 0
                    image_settings = 0
                    continue
        return self.width, self.height, self.background_color

    def display_image(self):
        width, height, backgroundcolor = self.read_image_specifications()
        print("Image: ",width, height, backgroundcolor)
