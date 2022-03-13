class Solver:
    def __init__(self, input_tile):
        self.landscape = input_tile.landscape_array
        self.tiles = input_tile.tiles
        self.tile_size=4
        self.targets = input_tile.targets
        self.landscape_size = input_tile.landscape_size
        self.result = {}
        self.average_bush_colors=self.get_average_bush_colors()


#calculate the average bush colors per the 4x4 square area
    def get_average_bush_colors(self, landscape=None):
        
        average_bush_colors = {'1' : 0, '2' : 0, '3' : 0, '4' : 0}
     
        if landscape is None:
            landscape = self.landscape

        for i in range(self.landscape_size):
            for j in range(self.landscape_size):
                if landscape[i][j]!=0:
                    average_bush_colors[str(landscape[i][j])] += 1
        
      
        number_of_squares=(self.landscape_size*self.landscape_size)//16

        
        for key in average_bush_colors:
            average_bush_colors[key]=average_bush_colors[key]//number_of_squares
     
        return average_bush_colors
    
    
    def get_bush_colors(self, landscape=None):
        
        bush_colors = {'1' : 0, '2' : 0, '3' : 0, '4' : 0}

        if landscape is None:
            landscape = self.landscape

        for i in range(self.landscape_size):
            for j in range(self.landscape_size):
                if landscape[i][j]!=0:
                    bush_colors[str(landscape[i][j])] += 1

        return bush_colors


    def draw_tile(self, tile, x_position, y_position):
        
        if tile.shape == 'OUTER_BOUNDARY':
            return tile.outer_boundary(self, x_position, y_position)
        
        elif tile.shape == 'EL_SHAPE':
            return tile.el_shape(self, x_position, y_position)
        
        elif tile.shape == 'FULL_BLOCK':
            return tile.full_block(self, x_position, y_position)

    def is_solution_found(self):
        bush_colors = self.get_bush_colors(self.landscape)
        
        return all(bush_colors[key] == self.targets[key] for key, val in bush_colors.items())


    def copy_landscape(self):
        
        copied_landscape = [[0] * self.landscape_size for _ in range(self.landscape_size)]

        for i in range(self.landscape_size):
            for j in range(self.landscape_size):
                copied_landscape[i][j] = self.landscape[i][j]
        
        return copied_landscape
    
    
#if by putting the tile we do not violate the target constraint,the tile can be put
    def ac3(self, tile, x_position, y_position):
        possible = self.draw_tile(tile, x_position, y_position)
        bush_colors = self.get_bush_colors(possible)

        for key, _ in bush_colors.items():
            if bush_colors[key] < self.targets[key]:
                return False
            
        return True

    def update_x_y_positions(self, x_position, y_position):
        if x_position + self.tile_size < self.landscape_size:
            x_position += self.tile_size
        else:
            x_position = 0

            if y_position + self.tile_size < self.landscape_size:
                y_position += self.tile_size
        return x_position, y_position
    

    def update_old_x_y_positions(self,x_position,y_position):
        
        new_x_position, new_y_position=self.update_x_y_positions(x_position,y_position)
        
        return x_position,y_position, new_x_position,new_y_position
        
   #get bush colors in the next square area 
    def heuristics_get_bush_colors(self,x_position,y_position):
        
        bush_colors = {'1' : 0, '2' : 0, '3' : 0, '4' : 0}
            
        for i in range(x_position,x_position+4):
            for j in range(y_position,y_position+4):
                if self.landscape[i][j]!=0:
                    bush_colors[str(self.landscape[i][j])] += 1

        return bush_colors

#if in the next square area the bush colors are less than average then put FULL_BLOCK
#if not put the next available tile
#the tiles are sorted based on their number constraint in descending order
    def heuristics(self, x_position,y_position):
        tile=self.tiles
       
        bush_colors= self.heuristics_get_bush_colors(x_position,y_position)

        less_than_average=True
        for key in bush_colors:
            if ( bush_colors[key]>self.average_bush_colors[key]):
               less_than_average=False
               return None
           
        if(less_than_average):      
            for tile in self.tiles:
                if(tile.shape=="FULL_BLOCK" and tile.number>0):
                    return  tile  
        return None
      
    
    def tile_constraint_check(self,tile):
        return tile[0].number==tile[1].number==tile[2].number==0
    


    def backtrack(self, x_position, y_position):
        
        #check if solution is found and tile constraint is met
        if self.is_solution_found() and self.tile_constraint_check(self.tiles): 
        
            return True

        for tile in self.tiles:
          
            temp_tile=self.heuristics(x_position,y_position)
            if( temp_tile is not None):
                    tile=temp_tile
                
            if tile.number == 0:
             continue
         
            #create the copy of the original landscape
            copied_landscape = self.copy_landscape()
            if self.ac3(tile, x_position, y_position):
                
            
                tile.number =tile.number - 1
                #update the landscape by putting the next tile
                self.landscape = self.draw_tile(tile, x_position, y_position)
                
                #update the solution key
                self.result[f'{x_position} {y_position}']=tile.shape

                old_x_position, old_y_position, x_position, y_position=self.update_old_x_y_positions(x_position,y_position)
                
                #if solution is found return true
                if self.backtrack(x_position, y_position):
                    return True
                
                #if solution is not found change the last step
                #updrate the number of tiles and the landscape
                x_position, y_position = old_x_position, old_y_position
                self.landscape = copied_landscape
                tile.number =tile.number + 1 

        return False
