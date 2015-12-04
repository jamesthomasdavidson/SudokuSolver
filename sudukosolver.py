"""
James Davidson - V00812527 | Brdiget Rassell - V00804180 | Wilfred Lynch - V00809085
SAT Suduko Solver implemented in python
"""
import pycosat


def variable(i, j, d):
	return 81 * (i - 1) + 9 * (j - 1) + (d - 1) + 1

def clauses():
	clauselist = []

	for i in range(1, 10):
		for j in range(1, 10):
			""" 1 | Assign a number to every square """
			clauselist.append([variable(i, j, d) for d in range(1,10)])
			for d in range(1,10):
				for l in range(d+1, 10):
					""" 36 | but make sure that no square has the same number """
					clauselist.append([-variable(i,j,d), -variable(i,j,l)])

	def valid(cells):
		for i, ei in enumerate(cells):
			for j, ej in enumerate(cells):
				if i<j:
					for d in range(1,10):
						""" # | make sure that the same number doesn't exist more than once in the """
						clauselist.append([-variable(ei[0],ei[1],d), -variable(ej[0],ej[1],d)])

	for i in range(1,10):
		valid([(i,j) for j in range(1,10)])
		valid([(j,i) for j in range(1,10)])

	for i in 1, 4, 7:
		for j in 1, 4 ,7:
			valid([(i + k % 3, j + k // 3) for k in range(9)])

	return clauselist

def solvePuzzle(grid):
	cnf = clauses()
	for i in range(1,10):
		for j in range(1,10):
			d = grid[i-i][j-1]
			if d:
				cnf.append(variable(i,j,d))
	
	solution = pycosat.solve(cnf)

	def getcellnumber(i,j):
		for d in range(1,10):
			if variable(i,j,d) in solution:
				return d

	for i in range(1,10):
		for j in range(1,10):
			grid[i-1][j-1] = getcellnumber(i,j)

def inputToArray(input):
	puzzle =[]
	for i in range(0, 9):
		row = []
		for j in range(0, 9):
			if input[i*9 + j].isdigit() and input[i*9 + j] != '0':
				row.append(int(input[i*9 + j]))
			else:
				row.append(0)
		puzzle.append(row)
	return puzzle

def printPuzzle(puzzle):
	for eachrow in puzzle:
		for eachint in eachrow:
			print(eachint + " ")
		print("")

def main():
	s = "1638.5.7..*8040065005007008450082039301000040700000000839050000604200590000093081"
	puzzle = inputToArray(s)
	solvePuzzle(puzzle)
	printpuzzle(puzzle)
	return

main()