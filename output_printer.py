

def print_solution_key(solution,file=None):
    index=0

    
    for key in solution:
        if (file is None):
            print(f'{index} 4 {solution[key]}')
        else:
             file.write(f'{index} 4 {solution[key]}\n')
        index+=1
