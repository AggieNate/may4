

n = 17

# function to create pyramid
def triangle(n):
	# This sets the number of spaces
	spaces = 2 * n - 2

	for i in range(0,n):
		for j in range(0,spaces):
			print(end=" ")
		spaces = spaces - 1

		for j in range(0, i+1):
			print("* ", end="")

		print("\r")

triangle(n)





















# Assignment - Write a program to display a pyramid as shown below: