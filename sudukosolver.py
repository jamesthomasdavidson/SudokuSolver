"""
James Davidson - V00812527 | Brdiget Rassell - V00804180 | Wilfred Lynch - V00809085
SAT Suduko Solver implemented in python
"""

import sys

def base_nine(i, j, d):
	return 81 * (i - 1) + 9 * (j - 1) + (d - 1) + 1

def clauses():
	clauselist = []

	for i in range(1, 10):
		for j in range(1, 10):
			""" 1 | Assign a number to every square """
			clauselist.append([base_nine(i, j, d) for d in range(1, 10)])
			for d in range(1,10):
				for l in range(d+1, 10):
					""" 36 | but make sure that no square has the same number """
					clauselist.append([-base_nine(i, j, d), -base_nine(i, j, l)])

	def valid(cells):
		for i, ei in enumerate(cells):
			for j, ej in enumerate(cells):
				if i<j:
					for d in range(1,10):
						""" # | make sure that the same number doesn't exist more than once in the """
						clauselist.append([-base_nine(ei[0], ei[1], d), -base_nine(ej[0], ej[1], d)])

	for i in range(1,10):
		valid([(i,j) for j in range(1,10)])
		valid([(j,i) for j in range(1,10)])

	for i in 1, 4, 7:
		for j in 1, 4 ,7:
			valid([(i + k % 3, j + k // 3) for k in range(9)])

	return clauselist

def encodePuzzle(grid):
	cnf = clauses()
	for i in range(1,10):
		for j in range(1,10):
			d = grid[i-1][j-1]
			if d:
				cnf.append([base_nine(i, j, d)])
	return cnf
	#solution = pycosat.solve(cnf)

	# def getcellnumber(i,j):
	# 	for d in range(1,10):
	# 		if base_nine(i, j, d) in solution:
	# 			return d
    #
	# for i in range(1,10):
	# 	for j in range(1,10):
	# 		grid[i-1][j-1] = getcellnumber(i,j)

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
			print(str(eachint) + " ")
		print("")

def writeEncodingToFile(cnf_list, output_file_name):
	output_file = open(output_file_name, "w")
	output_file.write("")
	number_of_clauses = len(cnf_list)
	number_of_variables = base_nine(9,9,9)
	output_file.write("p cnf " + str(number_of_variables) + " " + str(number_of_clauses) + "\n")
	for clause in cnf_list:
		for num in clause:
			output_file.write(str(num) + " ")
		output_file.write("0\n")


def main():
	if len(sys.argv) != 3:
		print "Improper number of cmd arguments. See README."
		sys.exit()
	if sys.argv[1] == 'encode':
		input_file = open(sys.argv[2], "r")
		input_string = input_file.read()
		input_string_formatted = input_string.replace("\n", "").replace(" ", "")
		if len(input_string_formatted) != 9**2:
			print("Input file wrong length")
			sys.exit()
		#print input_string_formatted
		puzzle = inputToArray(input_string_formatted)
		cnf_list = encodePuzzle(puzzle)
		#print cnf_list
		output_file_name = sys.argv[2] + "CNF"
		writeEncodingToFile(cnf_list, output_file_name)

	elif sys.argv[1] == 'decode':
		print 'decoding'
	else:
		print ("improper command line argument " + sys.argv[1])

	#printPuzzle(puzzle)



if __name__ == "__main__":
	main()