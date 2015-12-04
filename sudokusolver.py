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
			"""Assign every square a number 1-9 """
			clauselist.append([base_nine(i, j, d) for d in range(1, 10)])
			for d in range(1,10):
				for l in range(d+1, 10):
					"""Make sure no square holds more than one number"""
					clauselist.append([-base_nine(i, j, d), -base_nine(i, j, l)])

	def valid(cells):
		for i, ei in enumerate(cells):
			for j, ej in enumerate(cells):
				if i<j:
					for d in range(1,10):
						"""Make sure the number doesnt exist more than once in every row, column and grid"""
						clauselist.append([-base_nine(ei[0], ei[1], d), -base_nine(ej[0], ej[1], d)])
						
	"""Column and row clauses assigned here"""
	for i in range(1,10):
		valid([(i,j) for j in range(1,10)])
		valid([(j,i) for j in range(1,10)])
		
	"""Grid rules assigned here"""
	for i in 1, 4, 7:
		for j in 1, 4 ,7:
			valid([(i + k % 3, j + k // 3) for k in range(9)])

	return clauselist

def encodePuzzle(grid):
	cnf = clauses()

	# add already filled in squares
	for i in range(1,10):
		for j in range(1,10):
			d = grid[i-1][j-1]
			if d:
				cnf.append([base_nine(i, j, d)])
	return cnf

def decodePuzzle(encoded_string):
	encoded_list = encoded_string.split()
	number_list = []
	# get rid of SAT specifier at start of file
	encoded_list.pop(0)
	result_list = []
	for var in encoded_list:
		if int(var)>0:
			number_list.append(int(var))

	for i in range(1,10):
		row = []
		for j in range(1,10):
			for d in range(1, 10):
				if base_nine(i, j, d) in number_list:
					row.append(d)
		result_list.append(row)
	printPuzzle(result_list)

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
			print(str(eachint) + " "),
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
	if len(sys.argv) != 4:
		print "Improper number of cmd arguments. See README.md for instructions."
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
		output_file_name = sys.argv[3]
		writeEncodingToFile(cnf_list, output_file_name)

	elif sys.argv[1] == 'decode':
		input_file = open(sys.argv[2], "r")
		input_string = input_file.read()
		decodePuzzle(input_string)

	else:
		print ("improper command line argument " + sys.argv[1])

if __name__ == "__main__":
	main()
