import ProblemBase
import math

class Problem6(ProblemBase.ProblemBase):
	
	def __init__(this):
		this._attempts = {1:this.AttemptOne}		

	def GetAttempts(this):
		return this._attempts

	def AttemptOne(this):
		n = input("Enter n:" )
		sumOfN = (n/2)*(n+1)
		squareOfSumOfN = math.pow(sumOfN,2)
		sumOfNSquared = (n/float(6))*(n+1)*(2*n + 1)
		print "The sum of the natural numbers from 1 to " + str(n) + " is: " + str(sumOfN)
		print "The square of the sum of the natural numbers from 1 to " + str(n) + " is: " + str(squareOfSumOfN)
		print "The sum of the squares of the natual numbers from 1 to " + str(n) + " is: " + str(sumOfNSquared)
		print "The difference between the square of the sums and the sum of the squares is: " + str(squareOfSumOfN - sumOfNSquared)		
		return

