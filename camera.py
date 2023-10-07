class Camera:
    def __init__(self, file_name_specifications):
        self.file_name_specifications = file_name_specifications
        self.camera_transf_index = None
        self.camera_distance = None
        self.camera_fov = None

    def read_camera_specifications(self):
        with open(self.file_name_specifications) as file:
            lines = file.readlines()
            camera_flag = 0
            camera_distance_flag = 0
            camera_fov_flag = 0
            camera_transf_flag = 0
            for line in lines:
                parts = line.strip().split()
                if 'Camera' in parts:
                    camera_flag = 1
                    continue
                elif camera_flag == 1 and '{' in parts:
                    camera_transf_flag = 1
                    continue
                elif camera_transf_flag == 1 and camera_flag == 1:
                    camera_flag = 2
                    camera_transf_flag = 2
                    camera_distance_flag = 1
                    self.camera_transf_index = parts[0]
                    continue
                elif camera_transf_flag == 2 and camera_distance_flag == 1 and camera_flag == 2:
                    self.camera_distance = float(parts[0])
                    camera_distance_flag = 2
                    camera_flag = 3
                    camera_transf_flag = 3
                    camera_fov_flag = 1
                    continue
                elif camera_transf_flag == 3 and camera_distance_flag == 2 and camera_flag == 3 and camera_fov_flag == 1:
                    self.camera_fov = parts[0]
                    camera_fov_flag = 0
                    camera_distance_flag = 0
                    camera_transf_flag = 0
                    continue
        return self.camera_transf_index, self.camera_distance, self.camera_fov
    
    def display_camera(self):
        camera_transf_index, camera_distance, camera_fov = self.read_camera_specifications()
        print("Camera:",camera_transf_index, camera_distance, camera_fov)
