# Project2b-CSP-TP

Run the main.py file from the terminal by providing the path to the test file as an argument.

The program will return the tile positions and their shapes as an output and the time taken for the alogrithm to find the solution.

# Search Problem
In this algorithm the tiles are drawn on the landscape using backtracking in which the given constraints are checked using forward propagation. The forward propagation ensures that by putting the next tile the bush target constraint is not violated. The backtracking algorithm returns True and updates the landscape if the solution is found and the constraints are satisfied. The tiles to be drawn are chosen based on the Least Constraining Value heuristics algorithm that returns the FULL_BLOCK tile if in the next square area of bushes, the colors are below the average number of bush colors per the square area.

#Results
The algorithm is tested using test.py program, which reads tests the files in the directory and writes in the output file the results and the elapsed time for each input. There are 10 files in the testing directory. The 8 out of 10 tests are passed in around 2 seconds. The output file (output.dat) is placed in the github repository, whereas the test files can be found under the Tests directory of the same repository.
