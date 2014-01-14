from math import floor
#number encoded as a string, this function returns the integer value of the digit in a given decimal place
def check_Num(n):
	i=0
	while i<10:
		if n==str(i):
			return i
		i+=1
		
#Checks int
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
		
#Get user input	
noInt=True
while noInt:
	print "Input an integer to determine the sum of its digits"
	user=raw_input()
	if RepresentsInt(user):
		noInt=False
	
sum=0


for dig in user:
	sum+=check_Num(dig)

	
print sum

