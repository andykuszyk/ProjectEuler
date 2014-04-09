print "Enter the problem number:"

# Problem 4 - Largest palindrome

def IsPalindrome(testNumber):
    testString = str(testNumber)

    # Test for even length
    if len(testString)%2 <>0:
        return False

    
    # Loop through characters until middle and match to end
    char=0
    while char< len(testString)/2:
        if testString[char] <> testString[len(testString)-char-1]:
            return False
        char+=1

    return True

largestPalindrome=0
numberOne=999
numberTwo=999

while numberOne>99:
    if largestPalindrome>0:
        break
    
    while numberTwo>99:
        print numberOne*numberTwo
        if IsPalindrome(numberOne * numberTwo):
            largestPalindrome=numberOne * numberTwo
            break
        
        numberTwo-=1
        
    numberOne-=1
    numberTwo=numberOne

if largestPalindrome>0:
    print "Largest palindrome found: " + str(largestPalindrome)
else:
    print "No palindrome found."

