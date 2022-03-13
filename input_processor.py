import re
from tile_processor import Tile

class Landscape:

    def __init__(self, path):
        with open(path, "r") as file:
            lines = file.readlines()

        self.lines = list(map(lambda x: re.sub('[\n]$', '', x), lines))
        self.indices=self.get_indices()
        self.landscape_size=self.get_landscape_size()
        self.bush_color_num = 4
        self.landscape_array = self.get_landscape()
        self.tiles = self.get_tiles()
        self.targets = self.get_targets()

#get indices of the lines where the corresponding inputs are given
    def get_indices(self):
        indices={'landscape_index':0, 'tile_index,':0,' target_index' :0}
        tiles_found = False

        for i, j in enumerate(self.lines):
            if j.startswith('# Landscape'):
                indices['landscape_index']= i + 1

            elif j.startswith('# Tiles:') and not tiles_found:
                indices['tile_index'] = i + 1
                tiles_found = True

            elif j.startswith('# Targets:'):
                indices['target_index'] = i + 1

        return indices
    
    
    def get_landscape_size(self):
        
        return len(self.lines[self.indices['landscape_index']])//2
    
    #generate the matrix of the landscape
    def get_landscape(self):
        landscape_string = self.lines[self.indices['landscape_index']:self.indices['landscape_index']+self.landscape_size]

        landscape_array = [[0] * self.landscape_size for _ in range(self.landscape_size)]

        for i in range(self.landscape_size):
            t = 0
            for j in range(0, 2*self.landscape_size, 2):
                if landscape_string[i][j] != ' ':
                    landscape_array[i][t] = int(landscape_string[i][j])
                t += 1

        return landscape_array


    def get_tiles(self):
        tile_index = self.lines[self.indices['tile_index']]

        tile_list = []
        tiles = re.sub('[\{\}]', '', tile_index)
        tiles = list(map(lambda x: x.strip(), tiles.split(',')))

        for tile in tiles:
            key, value = tile.split('=')
            tile_list.append(Tile((key, int(value))))
            
#sort the tiles in descending order bassed on the given number
        tile_list.sort(key=lambda x: x.number, reverse=True)

        return tile_list


    def get_targets(self):
        
        targets = self.lines[self.indices['target_index']:self.indices['target_index']+self.bush_color_num]

        taget_dict = {}

        for target in targets:
            key, value = target.split(':')
            taget_dict[key] = int(value)

        return taget_dict