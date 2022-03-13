from input_processor import Landscape
import csp
import time
import sys
from  output_printer import print_solution_key

if __name__ == '__main__':
    
    path=sys.argv[1]
  
    #path='Tests/tilesproblem_1326658924404900.txt'
    input_data= Landscape(path)
    
    my_problem=csp.Solver(input_data)
    
    start_time=time.time()
    result=my_problem.backtrack(0,0)
    end_time=time.time()
    
    if(result):
        print("Elapsed time (s): {:.2f}\n".format(end_time-start_time) )
        
        print_solution_key(my_problem.result)
        print("\nTarget bush colors: ")
        print(input_data.targets)
        print("Obtained bush colors: ")
        print(my_problem.get_bush_colors(my_problem.landscape))
    else:
        print("Solution not found")
        
        


    