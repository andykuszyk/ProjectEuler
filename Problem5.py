import ProblemBase

class Problem5(ProblemBase.ProblemBase):
	
	def __init__(this):
		this._attempts = {1:this.AttemptOne, 2:this.AttemptTwo, 3:this.AttemptThree}		

	def GetAttempts(this):
		return this._attempts

	def AttemptOne(this):
		testNumber=1
		while(True):
			#print "Testing: " + str(testNumber)
			if(this.IsDivisibleByNumbersUpToTwenty(testNumber)):
				print "The answer is: " + str(testNumber) + "!"
				break
			testNumber+=1	
		return

	def CanExpressAsAPowerOf(this,numberToExpress,numberToRaise,maxResult):
		result = 0
		power = 1
		while(result<=maxResult):
			result = numberToRaise ^ power
			if(result == numberToExpress):
				return power
			power +=1
		return 0

	def CanBeExpressedAsAProductOfTwoSmallerNumbers(this,numberToExpress):
		for n in xrange(2,numberToExpress-1):
			if(numberToExpress%n==0 and numberToExpress/n<numberToExpress):
				return True
		return False

	def AttemptTwo(this):
		maxNoToDivideBy = int(input("Enter the maximum number to divide by: "))
		listOfFactors = [1]

		# Can the number be expressed as a power of a smaller number? The resulting number
		# must be less than n or the power is too high. If the smaller number is used as a
		# power more than once, take only the instance of the highest power.
		# If so, eliminate the smaller number.

		# Can the number be expressed as a multiple of two smaller numbers?
		# If so, eliminate the number itself.

		factors = []
		for n in xrange(2,maxNoToDivideBy):
			shouldContinue = False
			# Can be expressed as a power
			for m in xrange(2,n):
				powerOfMToGiveN = this.CanExpressAsAPowerOf(n,m,maxNoToDivideBy)
				if(powerOfMToGiveN>0):
					factors.append(n)			
					shouldContinue = True
					if(m in factors):
						factors.remove(m)
					if(powerOfMToGiveN>2):
						for power in xrange(2,powerOfMToGiveN-1):
							if(m^power in factors):
								factors.remove(m^power)
					break
			if(shouldContinue): continue
			# Can be expressed as a product of two smaller numbers
			if(this.CanBeExpressedAsAProductOfTwoSmallerNumbers(n)):
				continue
			else:
				factors.append(n)			

		productOfFactors =1
		for factor in factors:
			productOfFactors = productOfFactors*factor

		print "The answer is: " + str(productOfFactors)
		print "The factors were:"
		for factor in factors:
			print str(factor)

	def IsDivisibleByNumbersUpToTwenty(this,n):
		for m in xrange(1,20):
			if(n%m<>0):
				return False
		return True

	def AttemptThree(this):
		factors = []
		maxNoToDivideBy = int(input("Enter the maximum number to divide by: "))
		for factor in xrange(2,maxNoToDivideBy):
			if(this.IsPrime(factor)):
				print "Found prime factor: " + str(factor)
				power = this.GetHighestPower(factor,maxNoToDivideBy)
				print "Highest power of factor is: " + str(power)
				factorToAdd = factor**power
				print "This yields a factor to add of: " + str(factorToAdd)
				factors.append(factorToAdd)
		print "Factors:"
		for factor in factors:
			print str(factor)
		answer = 1
		for factor in factors:
			answer = answer*factor
		print "Answer: " + str(answer)
	
	def IsPrime(this,n):
		factor = n-1
		while(factor>1):
			if(n%factor==0):
				return False
			factor-=1
		return True

	def GetHighestPower(this,n,maximumValue):
		power = 1
		while(True):
			if(n**power>maximumValue):
				return power-1
			power+=1

