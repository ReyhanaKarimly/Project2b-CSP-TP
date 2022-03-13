from input_processor import Landscape
import csp
import time
from  output_printer import print_solution_key
import os

#this file runs the test files in a given directory and logs the given outputs in a output.dat file
if __name__ == '__main__':
    
    
    output_file_t=open("output.dat",mode="w",encoding="utf-8")
   
    folder_path='Tests'
    
    os.chdir(folder_path)
    
  
    
    for file in os.listdir():
   
    # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{file}"
            
           
            output_file_t.write(file_path)      
       
            input_data= Landscape(file_path)
            
            my_problem=csp.Solver(input_data)
            
            start_time=time.time()
            result=my_problem.backtrack(0,0)
            end_time=time.time()
            
            if(result):
                
                output_file_t.write("\nElapsed time (s): {:.2f}\n".format(end_time-start_time) )
                
                print_solution_key(my_problem.result,output_file_t)
                output_file_t.write("\nTarget bush colors: ")
                output_file_t.write(str(input_data.targets))
                output_file_t.write("\nObtained bush colors: ")
                output_file_t.write(str(my_problem.get_bush_colors(my_problem.landscape)))
                output_file_t.write("\n")
            else:
                output_file_t.write("Solution not found\n\n")
         
               
         
    output_file_t.close()     
   
        
