import ProblemBase

class Problem4(ProblemBase.ProblemBase):
	
	def __init__(this):
		this._attempts = {1:this.AttemptOne,2:this.AttemptTwo}		

	def GetAttempts(this):
		return this._attempts

	def Reverse(this,n):
		reverse=0
		print "n: " + str(n)
		while n>0:
			reverse = 10 * reverse + n%10
			n=n/10
		print "reverse: " + str(reverse)
		return reverse

	def IsPalindromeFromReversed(this,n):
		result =  n==this.Reverse(n)
		print "Is palindrome: " + str(result)
		return result

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



	def AttemptOne(this):
		testNumber = 999*999
		minNumber=100*100
		while testNumber>minNumber:
			if this.IsPalindrome(testNumber) and this.IsAFactorOfThreeDigitNumbers(testNumber):
				break
			testNumber-=1

		print testNumber

	def AttemptTwo(this):
		a=999
		largestPalindrome=0
		
		while a>=100:
			b=999
			while b>=100:
				print "a: " + str(a) + ", b: " + str(b)
				ab = a*b
				if(ab<=largestPalindrome): break
				
				if(this.IsPalindromeFromReversed(ab)): largestPalindrome=ab
				b-=1
			a-=1
		print "Largest palindrome is: " + str(largestPalindrome)








