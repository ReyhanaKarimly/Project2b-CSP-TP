class Tile:
    def __init__(self, tile):
        
        self.shape = tile[0]
        self.number = tile[1]
        self.size = 4
     


    def outer_boundary(self, landscape, x_position, y_position):
        landscape_copy = landscape.landscape.copy()
        for i in range(x_position, x_position + self.size):
            for j in range(y_position, y_position + self.size):
                if (i == x_position) or (i == x_position + self.size - 1) or (j == y_position) or (j == y_position + self.size - 1):
                    landscape_copy[i][j] = 0
        return landscape_copy

    def el_shape(self, landscape, x_position, y_position):
        landscape_copy = landscape.landscape.copy()
        for i in range(x_position, x_position + self.size):
            for j in range(y_position, y_position + self.size):
                if (i == x_position) or (j == y_position):
                    landscape_copy[i][j] = 0
        return landscape_copy
    
    def full_block(self, landscape, x_position, y_position):
        landscape_copy = landscape.landscape.copy()
        for i in range(x_position, x_position + self.size):
            for j in range(y_position, y_position + self.size):
                landscape_copy[i][j] = 0
        return landscape_copy
