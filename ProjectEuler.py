print "Enter the problem number:"

# Problem 4 - Largest palindrome

IsPalindrome(testNumber):
    

largestPalindrome=0
numberOne=999
numberTwo=999

while numberOne>99:

    while numberTwo>99:
        if IsPalindrome(numberOne * numberTwo):
            largestPalindrome=numberOne * numberTwo
            
        numberTwo-=
        
    numberOne-=
    numberTwo=numberOne

if largestPalindrome>0:
    print "Largest palindrome found: " largestPalindrome
else:
    print "No palindrome found."

