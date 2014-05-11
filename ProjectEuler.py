import time

def IsPalindrome(testNumber):
    testString = str(testNumber)
    char=0
    while char< len(testString)/2:
        if testString[char] <> testString[len(testString)-char-1]:
            return False
        char+=1
    return True

def IsAFactorOfThreeDigitNumbers(testNumber):
	a=999
	while a>99:
		if testNumber%a<>0:
			continue
		b=testNumber/a
		if len(str(a))==3 and len(str(b))==3 and int(b)==b:
			return True
		a-=1
	return False

#startTime=time.time()
#result=IsPalindrome(123321)
#endTime= time.time()
#print result 
#print endTime-startTime

a=999
b=999
testNumber = a*b
minNumber=100*100
while testNumber>minNumber:
	if IsPalindrome(testNumber) and IsAFactorOfThreeDigitNumbers(testNumber):
		break
	testNumber-=1

print testNumber

#print time.time()-startTime
