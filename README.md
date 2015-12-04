# SudokuSolver

Authors
-------

William Lynch V00809085
James Davidson V00812527
Bridget Rassell V00804180

Description
-----------

sudokusolver.py encodes a sudoku puzzle represented as a string into CNF DIMACS, suitable for input into
MiniSAT, and conversely decodes the output of MiniSAT into a solved puzzle in a human readable format.

The run_solver.sh script automates the entire solving process, by running the encoding, miniSAT, and decoding steps
on all files within the tests/unencoded folder.


Dependencies
 -----------

 Python 2, MiniSAT, bash shell


Instructions
------------

Input: the file input to the encoder should be encoded as a string of size 9^2, with only digits, '*', or '?' characters.
       Digits represent numbers already filled in on the sudoku board. Unknown squares may be represented by 0, *, or ?.
Example:

..2..5..3
6.....74.
.7..1....
...3...89
...492...
39...1...
....4..5.
.34.....1
7..6..9..


To encode a specific file into CNF form, type in the following in the command line:
  python sudokusolver.py encode <filename>

To decode the results of the MiniSAT solver, type the following in the command line:
  python sudokusolver.py decode <filename>

To solve the puzzles in the tests/unencoded folder:
  Enter the command "chmod u+x solve.sh" to enable script execution
  Run ./run_solver
