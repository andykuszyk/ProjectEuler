class Problem4:
	
	def __init__(this):
		this._attempts = {1:this.AttemptOne,2:this.AttemptTwo}		

	def IsPalindrome(this, testNumber):
	    testString = str(testNumber)
	    char=0
	    while char< len(testString)/2:
		if testString[char] <> testString[len(testString)-char-1]:
		    return False
		char+=1
	    return True

	def IsAFactorOfThreeDigitNumbers(this, testNumber):
		a=999
		while a>99:
			if testNumber%a<>0:
				continue
			b=testNumber/a
			if len(str(a))==3 and len(str(b))==3 and int(b)==b:
				return True
			a-=1
		return False

	def Run(this):
		print "Please choose from the following attempts to run:"
		for attempt in this._attempts.keys():
			print attempt
		attemptSelection = input("Attempt to run: ")
		this.RunAttempt(attemptSelection)	

	def RunAttempt(this, attemptNumber):
		this._attempts[attemptNumber].invoke()

	def AttemptOne(this):
		testNumber = 999*999
		minNumber=100*100
		while testNumber>minNumber:
			if this.IsPalindrome(testNumber) and this.IsAFactorOfThreeDigitNumbers(testNumber):
				break
			testNumber-=1

		print testNumber

	def AttemptTwo(this):
		# Do nothing
		print "Attempt two."
