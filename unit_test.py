import csp
from input_processor import Landscape
import unittest


class TestBushColorCounter(unittest.TestCase):
    
    test_file_path='test.txt'
   
      
    test_input=Landscape(test_file_path)
    test_problem=csp.Solver(test_input)

    def test_get_bush_colors(self):
        
        #number of tiles for all shapes is 0, bush color number equal to target bush color number
        
        self.assertEqual(self.test_problem.get_bush_colors(self.test_problem.landscape),self.test_input.targets)

    def test_get_average_bush_colors(self):
        #test input consists of one 4x4 grid, average_bush_colors=target_bush_colors
        
        self.assertEqual(self.test_problem.get_average_bush_colors(self.test_problem.landscape),self.test_input.targets)
   
    
if __name__ == '__main__':
    unittest.main()