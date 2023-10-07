class Triangles:
    def __init__(self, file_name_specifications, triangle_selector):
        self.file_name_specifications = file_name_specifications
        self.triangle_selector = triangle_selector
        self.triangles_transf_index = None
        self.triangles_material_index = None
        self.vertice_one_coords = None
        self.vertice_two_coords = None
        self.vertice_three_coords = None
        self.triangles_dictionary = {}
        self.triangle_index = -1
        

    def read_triangles_specifications(self):
        with open(self.file_name_specifications) as file:
            lines = file.readlines()
            triangles_material_flag = 0
            triangles_transf_flag = 0
            yahoo = 0
            yehaw = -1
            index_dictionary = -1
            for line in lines:
                parts = line.strip().split()
                if 'Triangles' in parts:
                    triangles_transf_flag = 1
                    continue
                if triangles_transf_flag == 1 and '{' in parts:
                    self.triangle_index += 1
                    triangles_transf_flag = 2
                    triangles_material_flag = 1
                    continue
                if triangles_transf_flag == 2 and triangles_material_flag == 1 and self.triangle_index == self.triangle_selector:
                    if yahoo == 0 and len(parts)==1:
                        self.triangles_transf_index = parts[0]
                        yahoo += 3
                    elif len(parts)==1:
                        index_dictionary += 1
                        if index_dictionary not in self.triangles_dictionary:
                            self.triangles_dictionary[index_dictionary] = []
                        yahoo += 3
                        self.triangles_dictionary[index_dictionary].append(parts[0])
                    if len(parts)==3:
                        yehaw += 1
                        self.triangles_dictionary[index_dictionary].append(parts)
                    if yehaw == 3:
                        yehaw = -1
                if triangles_transf_flag == 2 and '}' in parts and self.triangle_index == self.triangle_selector:
                    triangles_transf_flag = 0
                    continue
        return self.triangles_transf_index, self.triangles_dictionary
    
    def display_triangles(self):
        triangles_transf_index, triangles_dictionary = self.read_triangles_specifications()
        print("triangles: ",triangles_transf_index,"\nVertex Apocalypse: ", triangles_dictionary)
