from itertools import combinations

class Block:
    def __init__(self, dims):
        self.dims = dims
        
    def get_width(self):
        return self.dims[0]
    
    def get_length(self):
        return self.dims[1]
    
    def get_height(self):
        return self.dims[2]
    
    def get_volume(self):
        return self.dims[0] * self.dims[1] * self.dims[2]
    
    def get_surface_area(self):
        return 2 * sum(map(lambda x: x[0]*x[1], combinations(self.dims, 2)))
        