## Sudoku_solver
Built a Sudoku solver in Python using backtracking algorithm.

**Backtracking** is a general algorithm for finding solutions by simply reverting back to the previous step or solution as soon as we determine that our current solution cannot be continued into a complete one.
I have used this principle of backtracking to built this Sudoku solver.

#### Steps for Backtracking Algorithm:

##### Starting with an incomplete board:
    1. Attempt to place the digits 1-9 in an empty space of the board
    2. Check if that digit is valid in the current spot based on the current board
      a.  If the digit is valid, recursively attempt to fill the board using steps 1-3.
      b.  If it is not valid, reset the square box we just filled and go back to the previous step.
    3. Once the board is full by the definition of this algorithm we have found a solution.
    
    
![](./Sudoku_solver_output.png)
![]()
