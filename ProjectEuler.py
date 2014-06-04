import Problem4
import Problem5

problems = {4: Problem4.Problem4(), 5: Problem5.Problem5()}

print "Welcome to Andy's Project Euler Solutions."
print "Please choose a solution to run from the following list:"
for problem in problems.keys():
	print problem
problemSelection = input("Problem selection: ")
problems[problemSelection].Run()
